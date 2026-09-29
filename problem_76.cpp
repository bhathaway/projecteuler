// Copied from projecteuler.net/problem=76
//
// It is possible to write five as a sum in exactly six different ways:
// 4 + 1
// 3 + 2
// 3 + 1 + 1
// 2 + 2 + 1
// 2 + 1 + 1 + 1
// 1 + 1 + 1 + 1 + 1
// How many different ways can one hundred be written as a sum of at least two positive integers?

// Concepts.
// It certainly will become unwieldy to write out all the sums, at least the closer the sum is
// to all `1`. So, at least for now I could represent these sums like this:
// 5:<1(5)>
// 4:<2(1), 1(3)>
// 3:<2(2), 1(1)>
// 3:<3(1), 1(2)>
// 2:<3(1), 2(1)>
// 2:<4(1), 1(1)>

// The number at start is the number of terms, and enclosed in < > is a list of strictly
// non-increasing terms, with the number of identical terms written in parentheses.

// High order strategy. I think we could start from all 1 and create a new generation of terms by
// combining terms from the current generation. I could walk us through solving `6` to see how this
// might work.
// [Start]
// 6:<1(6)> # In each solution there will be something like this to begin
// ---
// 5:<2(1), 1(4)> # It's easy to see there can only be one.
// ---
// 4:<2(2), 1(2)>
// 4:<3(1), 1(3)>
// ---
// 3:<2(3)>
// 3:<3(1), 2(1), 1(1)>
// 3:<4(1), 1(2)> # I've been thinking in terms of merge operations to produce these. We certainly
//                # will overcount by doing so, but I don't yet know how to avoid this.
// ---
// 2:<4(1), 2(1)>
// 2:<3(2)>
// 2:<5(1), 1(1)>

// The way I obtained next generations is by merging terms together in a methodical fashion.
// Always start from the lowest numbers and combine from the same terms if possible. Next try to
// combine two terms from the next term to the left, then move to the next term if there are
// multiple. In this way we're always merging from one or two term groups. What I haven't yet
// determined is if combining terms in this ordered way misses some combinations in the general
// sense. In other words, are there combinations which skip groups that wouldn't be covered by
// other generators? This will turn out to be important, because if there are "holes", it will
// make the algorithm not better than brute force.

// I've found a potentially much better way than the above. The central concept is the use of a
// state change operator, call it [-1, +1], that alters a sum at a specific position. A process
// is forbidden from violating the ordered nature of the sum.
// I'll copy my notes from paper here to give an example of how this could be done for `10`:

// FIXME: These hand verified sequences were missing values and mislead my validation.
// Number: `10`
// `2` terms
// <9, 1> - <8, 2> - <7, 3> - <6, 4> - <5, 5>
//
// `3` terms
// <8, 1, 1> - <7, 2, 1> - <6, 3, 1> - <5, 4, 1>
//                             |           |
//                         <6, 2, 2> - <5, 3, 2> - <4, 4, 2> - <4, 3, 3>
//
// `4` terms
// <7, 1(3)> - <6, 2, 1, 1> - <5, 3, 1, 1> - <4, 4, 1, 1>
//                                 |              |
//                            <5, 2, 2, 1> - <4, 3, 2, 1> - <4, 2, 2, 2> - <3, 3, 3, 1> - <3, 3, 2, 2>
//
// `5` terms
// <6, 1(4)> - <5, 2, 1(3)> - <4, 3, 1(3)> - <4, 2, 2, 1, 1> - <3, 3, 2, 1, 1>
//
// `6` terms
// <5, 1(5)> - <4, 2, 1(4)> - <3, 3, 1(4)> - <3, 2, 2, 1(3)>
//
// `7` terms
// <4, 1(6)> - <3, 2, 1(5)>
//
// `8` terms
// <3, 1(7)> - <2, 2, 1(6)>
//
// `9` terms
// <2, 1(8)>
//
// `10` terms
// <1(10)>

// Analysing the graph above, it should be clear that [-1, +1] is being applied to different
// positions of the sum to get different branches. If that operation would invalidate the
// strictly non-increasing invariant for sums, that branch is removed (not pictured above).
// As anticipated, it is possible to arrive at the same sum through different routes. _The_
// key question is whether there is always a way to choose not to branch based on whether a
// previous branch had been taken to avoid overcounting. If this is not possible, then
// memoization is the only remedy. In this case it's clear that at least the method proposed
// is efficient and doesn't overcount very much. In the spirit of pattern matching, I'll do
// another iteration:
//
// Number: `11`
// `2` terms
// <10, 1> - <9, 2> - <8, 3> - <7, 4> - <6, 5>
//
// `3` terms
// <9, 1, 1> - <8, 2, 1> - <7, 3, 1> - <6, 4, 1> - <5, 5, 1>
//                             |           |           |
//                         <7, 2, 2> - <6, 3, 2> - <5, 4, 2> 
//                                                     |
//                                                 <5, 3, 3>
//
// `4` terms
// <8, 1(3)> - <7, 2, 1, 1> - <6, 3, 1, 1> - <5, 4, 1, 1>
//                                 |              |
//                            <6, 2, 2, 1> - <5, 3, 2, 1> - <4, 4, 2, 1>
//                                                               |
//                                                          <4, 3, 3, 1>
//                                                               |
//                                                          <4, 3, 2, 2>
//
// `5` terms
// <7, 1(4)> - <6, 2, 1(3)> - <5, 3, 1(3)>    - <4, 4, 1(3)>
//                                 |                 |
//                            <5, 2, 2, 1, 1> - <4, 3, 2, 1, 1>
//
// `6` terms
// <6, 1(5)> - <5, 2, 1(4)> - <4, 3, 1(4)>
//                                 |
//                            <4, 2, 2, 1(3)> - <3, 3, 2, 1(3)>
//
// `7` terms
// <5, 1(6)> - <4, 2, 1(5)> - <3, 3, 1(5)>
//                                 |
//                            <3, 2, 2, 1(4)>
//
// `8` terms
// <4, 1(7)> - <3, 2, 1(6)>
//
// `9` terms
// <3, 1(8)> - <2, 2, 1(7)>
//
// `10` terms
// <2, 1(9)>
//
// `11` terms
// <1(11)>
//
// Okay, this proves that the method is broken, because I have the counter-example:
// We should have found <3(3), 2> above. If we had allowed the operator to operate over
// disparate indices, however, we would have found it, so perhaps that's the only
// modification necessary. It still seems like in general it would be good to identify
// subsequences whose range is 2 or greater, because that makes it a basic candidiate
// for the operator.


// Lets redo the above computation in a more "frontier" + "memoize" approach, allowing
// for expanding the operator to [0(L), -1, 0(M), +1, 0(N)], where L, M, N are possibly 0.
// `10`:
// <9, 1> + [-1, +1] =
// <8, 2> + [-1, +1] =
// <7, 3> + [-1, +1] =
// <6, 4> + [-1, +1] =
// <5, 5>
//
// <8, 1, 1>
//  ____
//
// <7, 2, 1>
//  ____
//
// <6, 3, 1>
//  _______
//
// <5, 4, 1>, <5, 3, 2>, <6, 2, 2>
//  _______    _______    ____
//
// <4, 4, 2>,  <4, 3, 3>
//     ____ 
//
//
// <7, 1(3)>
//

// I'm back after a really long time, because work is starting to dull my brain, especially with
// claude code doing so much work these days. I wonder if organizing by rank is the essential way
// to solve this problem. It seems clear that the "non-increasing" sequence requirement is a really
// good thing to keep. The "generator" for each rank should be obvious. Take `10` for instance:
// the rank 2 generator is <9, 1>, the rank 3 generator is <8, 1(2)>, the rank 4 generator is
// <7, 1(3)>, down to the rank 10 generator: <1(10)> which can't possibly create any new sequences.
// This reduces the problem to figuring out how to methodically count the non-increasing
// permutations starting with the generator.
//
// There may be substructure to take advantage of here. If we could theorectially know the rank
// counts for integers before this point, we could use those to know how many there should be for
// a certain starting integer in the sequence. For example, if we get to <5, ?, ?> for `10`, we
// should know that the count should match the solution for rank 2 for `5`. I think that might be a
// workable solution. The follow-up question would be: Is it possible to bootstrap the entire
// memoization from the first valid solution: `2` has only one sequence possible at <1(2)>,
// therefore rank 2 solutions adding to `2` are only 1. Moving on to three, starting with the
// generator <2, 1>. Why are we immediately stuck? I think it's because we actually need to
// generalize to rank 1 sequences. In other words, <1>, <2> etc, are still valid. Using this, we
// might be able to fully express a bootstrapping algorithm. I think we might need some new
// notation as well. I want to be able to express all sequences of a certain rank, maybe [n|r].
// Then count([n|1]) == 1 by definition. Then does it make sense to nest those? What would that
// look like? Using the example above of <5, ?, ?> getting to `10`, we could write as maybe
// <5, [5|2]>. This would be a rank 3 sequence. So, the algorithm for calculating [10|3] would be
// naively count([0|2]) + count([1|2]) + count([2|2]) + count([3|2]) + count([4|2]), etc. where the
// head of each sequence would be 10, 9, 8, 7, etc. such that the total count is 10. This
// does more than it needs to, but "not found" would result in 0, such that [0|2] and [1|2] return
// zero as expected.
//
// FINAL NOTES: This has been one of the hardest problems I've worked on for some reason. Everything
// seems more obvious in hindsight, but what strikes me as a useful takeaway is the role of
// projecteuler itself in providing feedback. Just a simple "wrong" is enough to get me to check
// my assumptions thoroughly, begging the question: What don't I check them earlier? I think if
// I got better at establishing invariants and being _sure_ that they're true would be a better
// foundation. What continues to be a good process for me is writing the code in a way that reflects
// the concepts that I'm using for the problem.

#include <iostream>
#include <map>
#include <cassert>

// The type aliases below are what I'm trying to use to help me do the data modeling correctly.

// The number of elements in a sum, strictly positive.
using Rank = std::size_t;

// The total that an NonIncreasingSequence sums to.
using Sum = std::size_t;

// The maximum element of a NonIncreasingSequence, which is its head by definition
using MaxElement = std::size_t; 

// A count of NonIncreasingSequence instances. There are different ways to group them, but
// probably the most useful to the algorithm is by all three of the above. With a little bit of
// thought, particularly for large numbers, it should be obvious that a given sum, rank, and
// maximum element can represent a fairly large number of NonIncreasingSequence.
using UniqueSequenceCount = std::size_t; 

// Represents a sum with a specific rank. This could have been done with a std::tuple, but
// I think this helps me think about the problem in a bit more detail.
class RankedSum {
public:
  // Atomic constructor
  RankedSum(Sum sum, Rank rank)
  : sum_(sum), rank_(rank) {
  }

  friend std::ostream& operator<<(std::ostream& out, const RankedSum& ranked_sum) {
    out << "[" << ranked_sum.sum_ << "|" << ranked_sum.rank_ << "]";
    return out;
  }

  // We define a strict ordering over elements for use with a mapping to sequence counts.
  bool operator<(const RankedSum& other) const {
    if (sum_ < other.sum_) {
      return true;
    } else if (sum_ > other.sum_) {
      return false;
    } else {
      return rank_ < other.rank_;
    }
  }

private:
  Sum sum_;
  Rank rank_;
};

using MaxToUniqueSequenceCount = std::map<MaxElement, UniqueSequenceCount>;
using UniqueSequences = std::map<RankedSum, MaxToUniqueSequenceCount>;

// This function must be called with increasing `target_sum` values starting from `1` in
// order to work correctly. That's a bit of a design flaw, but I don't really need to fix it
// to get the concept across.
//
// The inner loop over the initial new sequence element is the tricky bit. I had assumed, wrongly,
// that I could use the rank to cut off the looping, but of course the maximum value of a
// sequence can be much less than the initial <max, 1, 1, 1, etc.> pattern. This is what forced
// me to reimagine the mapping from ranked sums not just to a count, but to another map from
// maximum values to counts, so that the inner loop missing nothing. I failed to prove that this
// does not overcount, but it happens to not, a lucky accident.
UniqueSequenceCount
ComputeSum(UniqueSequences& all_sequences, Sum target_sum) {
  // This is the seed that fills in the entire family of sequences.
  all_sequences[RankedSum(target_sum, 1)][target_sum] = 1;
  const Rank max_sub_rank = target_sum - 1; // - 1 ensures we don't both with zeros

  for (Rank sub_rank = 1; sub_rank <= max_sub_rank; ++sub_rank) {
    for (MaxElement first_element = target_sum - sub_rank; first_element > 0; --first_element) {
      const Sum subsequence_sum = target_sum - first_element;
      RankedSum subseq(subsequence_sum, sub_rank);
      RankedSum new_sequences(target_sum, sub_rank + 1);
      for (auto pair : all_sequences[subseq]) {
        const MaxElement max = pair.first;
        if (first_element >= max) {
          const UniqueSequenceCount count = pair.second;
          auto& maxes = all_sequences[new_sequences];
          auto iter = maxes.find(first_element);
          if (iter == maxes.end()) {
            maxes[first_element] = count;
          } else {
            maxes[first_element] += count;
          }
        }
      }
    }
  }

  UniqueSequenceCount total_count = 0;
  for (Rank rank = 2; rank <= target_sum; ++rank) {
    for (auto pair: all_sequences[RankedSum(target_sum, rank)]) {
      const UniqueSequenceCount count = pair.second;
      total_count += count;
    }
  }

  return total_count;
}

int
main() {
  UniqueSequences all_sequences;

  const Sum value = 100;
  for (Sum sum = 1; sum < value; ++sum) {
    ComputeSum(all_sequences, sum);
  }

  UniqueSequenceCount answer = ComputeSum(all_sequences, value);
  std::cout << "The answer is " << answer << std::endl;
}


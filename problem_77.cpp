// Copied from projecteuler.net/problem=77
//
// It is possible to write ten as the sum of primes in exactly five different ways:
//
// 7 + 3
// 5 + 5 
// 5 + 3 + 2
// 3 + 3 + 2 + 2
// 2 + 2 + 2 + 2 + 2
//
// What is the first value which can be written as the sum of primes in OVER
// five thousand different ways?

// So naturally I'm wondering if I can borrow anything from the previous problem. Possibly, with
// maybe one complication: The frontier isn't necessarily smooth. I think we'll need to do a few
// examples using the same algorithmic approach as the previous problem to see what emerges

// n=2
//
// <2>

// n=3
//
// <3>

// n=4
//
// <2, 2>

// n=5
//
// <3, 2>

// n=6
// <3, 3>
// <2, 2, 2>

// n=7
// <5, 2>
// <3, 2, 2>

// n=8
// <5, 3>
// <3, 3, 2>
// <2, 2, 2, 2>

// n=9
// <7, 2>
// <5, 2, 2>
// <3, 3, 3>
// <3, 2, 2, 2>

// To me it seems like we might be able to memoize starting from two seeds: n=2 and n=3.

#include <iostream>
#include <map>
#include <cassert>
#include <vector>

bool
IsPrime(std::size_t i) {
    if (i < 2) {
        return false;
    }

    for (std::size_t divisor = 2; i / divisor >= divisor; ++divisor) {
        if (i % divisor == 0) {
            return false;
        }
    }

    return true;
}

std::vector<std::size_t>
PrimesUpTo(std::size_t max) {
  std::vector<std::size_t> result;
  for (std::size_t i = 2; i <= max; ++i) {
    if (IsPrime(i)) {
      result.push_back(i);
    }
  }

  return result;
}

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
ComputeSum(
    const std::vector<std::size_t>& primes,
    UniqueSequences& all_sequences,
    Sum target_sum) {

  if (target_sum < 2) {
    return 0;
  }
  // Here the new place for seeds
  if (IsPrime(target_sum)) {
    all_sequences[RankedSum(target_sum, 1)][target_sum] = 1;
  }

  const Rank max_sub_rank = target_sum - 1;

  for (Rank sub_rank = 1; sub_rank <= max_sub_rank; ++sub_rank) {
    for (std::size_t prime_index = 0;
         primes.at(prime_index) <= target_sum - sub_rank;
         ++prime_index) {

      const MaxElement first_element = primes[prime_index];
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
  const Sum value = 6000;
  std::vector<std::size_t> primes = PrimesUpTo(value);

  for (Sum sum = 1; sum <= value; ++sum) {
    UniqueSequenceCount count = ComputeSum(primes, all_sequences, sum);
    std::cout << "Count for n=" << sum << " is " << count << std::endl;
  }
}


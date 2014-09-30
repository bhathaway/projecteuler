// A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

// Find the largest palindrome made from the product of two 3-digit numbers.

// How fun! My basic Idea would be to traverse the upper triangular matrix from largest to smallest product.

//   1   2   3   4   5   6   7   8   9
//                                    
//       4   6   8  10  12  14  16  18
//                                    
//           9  12  15  18  21  24  27
//                                    
//              16  20  24  28  32  36
//                                    
//                  25  30  35  40  45
//                                    
//                      36  42  48  54
//                                    
//                          49  56  63
//                                    
//                              64  72
//                                    
//                                  81

// Notice that the lower left to upper right diagonals are strictly decreasing.. We can use this for a dynamic
// programming solution. The idea is to keep a frontier of integers that may be the next smallest product..

// The main question is, how many diagonals do we need to look at at any one time. I think the idea would be to
// look at the end of the new diagonal and include at many new diagonal starts as are necessary to cover the
// values in the current diagonal.

// Here's a useful concept, perhaps.. Diagonal rank. Just the sum of the indices.

#include <iostream>
#include <sstream>
#include <list>
#include <cassert>

using namespace std;

static inline
bool is_palindrone(unsigned number)
{
    stringstream ss;
    ss << number;
    string repr = ss.str();
    size_t size = repr.size();
    for (unsigned i = 0; i < size/2; ++i) {
        if (repr[i] != repr[size - i - 1]) {
            return false;
        }
    }

    return true;
}

class DiagonalCoordinate
{
public:
    DiagonalCoordinate(int r, int o) : rank(r), offset(o) { }

    int getValue() const
    {
        const int n = rank / 2;
        const int m = rank - n;

        return (m + offset) * (n - offset);
    }

    bool valid() const
    {
        const int n = rank / 2;
        const int m = rank - n;

        if (m > max_index || n < min_index) {
            return false;
        } else {
            return true;
        }
    }

    int lastValue() const
    {
        const int n = rank / 2;
        const int m = rank - n;

        // Do we hit m's limit first, or n?
        // m + offset cannot exceed max_index and
        // n - offset cannot be less than min_index
        const int last_offset = min(max_index - m, n - min_index);
        return (m + last_offset) * (n - last_offset);
    }

    int getRank() const
    {   return rank; }

    bool at_start() const
    {   return offset == 0; }
    
    bool at_end() const
    {
        const int n = rank / 2;
        const int m = rank - n;

        if (m + offset >= max_index || n - offset <= min_index) {
            return true;
        } else {
            return false;
        }
    }

    void increment()
    {
        if (!at_end()) {
            ++offset;
        }
    }

private:
    int rank;
    int offset;

public:
    static unsigned min_index;
    static unsigned max_index;
};

unsigned DiagonalCoordinate::min_index;
unsigned DiagonalCoordinate::max_index;


// Better would be to encapsulate the whole frontier concept into an iterator
// over the set of integers defined by the min_index to max_index box, which would
// borrow the code here.
int largest_palindrone(unsigned min_index, unsigned max_index)
{
    unsigned result = 0;
    DiagonalCoordinate::min_index = min_index;
    DiagonalCoordinate::max_index = max_index;

    // This is the magic. We're going to grow this dynamically
    // to keep track of the next smallest integer.
    list<DiagonalCoordinate> frontier;

    bool at_end = false;
    bool goal_reached = false;

    // Seed the frontier with the initial value.
    DiagonalCoordinate start(2*max_index, 0);
    if (!start.valid()) {
        return result;
    }
    frontier.push_back(start);

    unsigned iterations = 0;
    while (!at_end && !goal_reached) {
        int largest_value = 0;
        list<DiagonalCoordinate>::iterator ptr_to_max = frontier.end();
        for (list<DiagonalCoordinate>::iterator it = frontier.begin(); it != frontier.end(); ++it) {
            int test_value = it->getValue();
            if (test_value > largest_value) {
                largest_value = test_value;
                ptr_to_max = it;
            }
        }

        if (is_palindrone(largest_value)) {
            result = largest_value;
            goal_reached = true;
        } else {
            // The frontier should tell us what to do next..
            // If I'm correct, the frontier should never fragment, if any diagonal reaches the end,
            // it will be the largest value.
            if (ptr_to_max->at_end()) {
                assert(ptr_to_max == frontier.begin());
                if (frontier.size() == 1) {
                    DiagonalCoordinate next_diagonal(frontier.front().getRank() - 1, 0);
                    if (next_diagonal.valid()) {
                        frontier.push_back(next_diagonal);
                    } else {
                        at_end = true;
                    }
                }

                if (!at_end) {
                    frontier.pop_front();

                    // Add as many new diagonals are required to cover the front diagonal.
                    const int smallest_rank = frontier.back().getRank();
                    DiagonalCoordinate candidate(smallest_rank - 1, 0);

                    while (candidate.valid() && candidate.getValue() > frontier.front().lastValue()) {
                        frontier.push_back(candidate);
                        candidate = DiagonalCoordinate(candidate.getRank() - 1, 0);
                    }
                }
            } else {
                // This should be the usual case.
                ptr_to_max->increment();
            }
        }
        ++iterations;
    }

    cout << "Considered " << iterations << " iterations before finding the result.\n";

    return result;
}

int main()
{
    int largest = largest_palindrone(100, 999);
    cout << "The largest palindrone that is the product of two three digit numbers is " << largest << endl;
}


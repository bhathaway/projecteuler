// Find the largest prime under a million that is a sum of consecutive primes.
// Turns out there should be a dynamic programming solution to this problem,
// because for each sequence of consecutive primes of length N, the sum of the
// next consecutive sequence of length N+1 will be the previous sum plus
// the N+1th prime. The key structure we'll need is an array of consecutive
// primes under one million.

#include <iostream>
#include <vector>
#include <set>

using namespace std;

vector<unsigned> primes;
set<unsigned> prime_set;

bool is_prime(int i)
{
    if (i < 2) {
        return false;
    }

    for (unsigned divisor = 2; i / divisor >= divisor; ++divisor) {
        if (i % divisor == 0) {
            return false;
        }
    }

    return true;
}

void fillPrimes(vector<unsigned> & v, set<unsigned> & s, unsigned max)
{
    v.clear();
    for (unsigned i = 2; i <= max; ++i) {
        if (is_prime(i)) {
            v.push_back(i);
            s.insert(i);
        }
    }
}

struct ResultType
{
    unsigned index;
    unsigned sequence_length;
};

ResultType findLargest(vector<unsigned> & v, set<unsigned> & s, unsigned max)
{
    unsigned num_primes = v.size();
    vector<unsigned> consecutive_sums = v; // Begins as sums of sequence length 1.
    unsigned largest_index = 0;
    unsigned largest_sequence_length = 0;

    for (unsigned sequence_length = 2; sequence_length <= num_primes; ++sequence_length) {

        cout << "Trying sequence length " << sequence_length << "\r";
        cout.flush();
        // By going in reverse, we can modify the vector in place.
        for (unsigned i = num_primes - 1; i >= sequence_length - 1; --i) {
            unsigned sum = consecutive_sums[i-1] + v[i];

            // Overflow trap, a real issue with this algorithm.
            if (sum > consecutive_sums[i]) {
                consecutive_sums[i] = sum;
                if (s.find(sum) != s.end()) {
                    largest_sequence_length = sequence_length;
                    largest_index = i;
                }
            }
        }
    }

    ResultType result;
    result.index = largest_index;
    result.sequence_length = largest_sequence_length;

    return result;
}

int main()
{
    unsigned max = 999999;
    cout << "Filling prime array..\n";
    fillPrimes(primes, prime_set, max);
    cout << "There are " << primes.size() << " primes below " << max + 1 << ".\n";

    auto result = findLargest(primes, prime_set, max);

    unsigned sum = 0;
    for (unsigned i = result.index - result.sequence_length + 1; i <= result.index; ++i) {
        cout << primes[i] << endl;
        sum += primes[i];
    }

    cout << "\nSum: " << sum << endl;
    cout << "Terms: " << result.sequence_length << endl;
}


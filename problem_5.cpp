// 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
// What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

// This is easy. You should be able to build up this value by accumulating prime factors in a list.
// It hardly even deserves coding, except that it would be interesting to allow it to scale arbitrarily.

// Ok, basically, the running number is a list of primes, but the representation
// 2^a * 3^b * 5^c * 7^d ... is more usable, because we can look at the exponent to decide whether to
// add another prime factor.

#include <cstdlib>
#include <map>
#include <iostream>

using namespace std;

typedef map<unsigned long long, unsigned long long> ExponentMap_t;

ExponentMap_t prime_factors(unsigned long long value)
{
    ExponentMap_t result;

    for(unsigned long long i = 2; value != 1;) {
        if (value % i == 0) {
            ExponentMap_t::const_iterator found = result.find(i);
            if (found == result.end()) {
                result[i] = 1;
            } else {
                ++result[i];
            }
            value /= i;
        } else {
            ++i;
        }
    }

    return result;
}

int main(int argc, char * argv[])
{
    unsigned long long argument = strtoull(argv[1], NULL, 10);
    ExponentMap_t exponent_map;

    for (unsigned long long i = argument; i >= 2; --i) {
        ExponentMap_t current_factors = prime_factors(i);
        for (ExponentMap_t::const_iterator it = current_factors.begin(); it != current_factors.end(); ++it) {
            ExponentMap_t::iterator found = exponent_map.find(it->first);
            if (found == exponent_map.end()) {
                exponent_map[it->first] = it->second;
            } else {
                if (it->second > exponent_map[it->first]) {
                    exponent_map[it->first] = it->second;
                }
            }
        }
    }

    unsigned long long value = 1;
    for (ExponentMap_t::const_iterator it = exponent_map.begin(); it != exponent_map.end(); ++it) {
        for (unsigned long long i = 0; i < it->second; ++i) {
            value *= it->first;
        }
    }

    // Now that we've build the integer, reveal it!
    cout << "Largest integer that integers 1 through " << argument << " divide is " << value << ".\n";
}


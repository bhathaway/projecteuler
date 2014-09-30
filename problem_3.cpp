#include <iostream>
#include <cstdlib>

using namespace std;

// The prime factors of 13195 are 5, 7, 13 and 29.
// What is the largest prime factor of the number 600851475143 ?


// The idea here is to return the first smallest prime that divides the composite.
static inline
long unsigned int prune(long unsigned composite)
{
    long unsigned int result = 0; // 0 means the value is prime

    for (long unsigned int i = 2; composite / i >= i; ++i) {
        // Note, this is integer division..
        if ((composite / i) * i == composite) {
            result = i;
            break;
        }
    }

    return result;
}

long unsigned int largest_prime_factor(long unsigned int input)
{
    long unsigned int factor;
    do {
        factor = prune(input);
        if (factor) {
            input /= factor;
        }
    } while (factor);

    return input;
}

int main(int argc, char * argv[])
{
    long unsigned int value = strtoull(argv[1], NULL, 10);
    cout << "The largest prime factor of " << value << " is " << largest_prime_factor(value) << endl;
}

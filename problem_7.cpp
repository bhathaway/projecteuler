// By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
// What is the 10,001st prime number?

// This is hard. Brute force is the only easy way to solve this problem.

#include <iostream>

using namespace std;

bool is_prime(unsigned long long i)
{
    for (unsigned long long divisor = 2; i / divisor >= divisor; ++divisor) {
        if (i % divisor == 0) {
            return false;
        }
    }

    return true;
}

int main()
{
    unsigned found = 0, n;
    for (n = 2; found < 10001; ++n) {
        if (is_prime(n)) {
            cout << n << " is prime.\n";
            ++found;
        }
    }

    cout << "The 10,001st prime is " << n-1 << endl;
}

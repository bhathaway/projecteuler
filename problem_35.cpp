#include <iostream>
#include <cmath>

using namespace std;

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

bool is_circularly_prime(int i)
{
    if (!is_prime(i)) {
        return false;
    }

    int num_digits = log(i)/log(10) + 1;

    // Examine n-1 rotations.
    for (int n = 0; n < num_digits - 1; ++n) {
        i = (i % 10) * pow(10, num_digits - 1) + i / 10;
        if (!is_prime(i)) {
            return false;
        }
    }

    return true;
}

int N = 1000000;

int main()
{
    size_t count = 0;
    for (int i = 0; i < N; ++i) {
        if (is_circularly_prime(i)) {
            cout << i << endl;
            ++count;
        }
    }

    cout << "Total circular primes below " << N << ": " << count << endl;
}

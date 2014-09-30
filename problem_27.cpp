#include <iostream>

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

int consecutive_primes(int a, int b)
{
    int n = 0;
    while (is_prime(n*n + a*n + b)) {
        ++n;
    }

    return n;
}

int main()
{
    int longest_run = 0;
    int best_a, best_b;
    for (int a = -999; a <= 999; ++a) {
        for (int b = -999; b <= 999; ++b) {
            int c = consecutive_primes(a, b);
            if (c > longest_run) {
                longest_run = c;
                best_a = a; best_b = b;
            }
        }
    }

    cout << "Best a, b pair is (" << best_a << ", " << best_b << ") with a run of " << longest_run << " primes.\n";
}

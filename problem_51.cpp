#include <set>
#include <sstream>
#include <iostream>

using namespace std;

// This variation on is_prime adapts to the largest request seen. Performance will be best
// when the largest prime sought gradually increases.
bool is_prime(unsigned i)
{
    static unsigned max = 1;
    static set<unsigned> primes;

    if (i <= max) {
        return primes.find(i) != primes.end();
    } else {
        bool prime;
        for (unsigned k = max + 1; k <= i; ++k) {
            prime = true;
            unsigned result;
            for (unsigned divisor = 2; (result = k / divisor) >= divisor; ++divisor) {
                if (result * divisor == k) {
                    prime = false;
                    break;
                }
            }

            if (prime) {
                primes.insert(k);
            }
        }

        max = i;
        return prime;
    }
}

// Might as well attempt the stupid way first.
bool hasNFamily(unsigned number, unsigned n)
{
    // Step one, break the number down to digits.
    stringstream ss;
    ss << number;
    string starting_digits = ss.str();
    size_t num_digits = starting_digits.size();

    bool result = false;

    for (unsigned mask = 1; mask < (1 << num_digits); ++mask) {
        unsigned count = 0;
        for (auto replacement_digit = '0'; replacement_digit <= '9'; ++replacement_digit) {
            string test_string(starting_digits);
            for (unsigned place = 0; place < num_digits; ++place) {
                if (mask & (1 << place)) {
                    test_string[num_digits - place - 1] = replacement_digit;
                }
            }
            if (test_string[0] == '0') {
                continue;
            }
            unsigned test_number = strtoul(test_string.c_str(), NULL, 10);
            if (is_prime(test_number)) {
                ++count;
            }
        }


        if (count >= n) {
            result = true;
            cout << number << " has an " << n << " family with mask " << mask << endl;
            break;
        }
    }

    return result;
}

int main()
{
    if (is_prime(121313)) {
        cout << "121313 is prime" << endl;
    }
    /*
    unsigned n = 2;
    while (!is_prime(n) || !hasNFamily(n, 8)) {
        cout << n << '\r';
        cout.flush();
        ++n;
    }
    */
}

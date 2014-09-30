//A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

//A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.
//
//As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.
//
//Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.

#include <iostream>
#include <cstdlib>
#include <vector>

using namespace std;

vector<unsigned> abundant_numbers;
vector<bool> is_sum_of_abundant;

bool is_abundant(unsigned number)
{
    unsigned sum = 1;
    for (unsigned d = 2; number / d >= d; ++d) {
        if (number % d == 0) {
            if (d * d == number) {
                sum += d;
            } else {
                sum += d + number / d;
            }
        }
    }

    if (sum > number) {
        return true;
    } else {
        return false;
    }
}

int main(int argc, char * argv[])
{
    is_sum_of_abundant.resize(28124, false);

    for (unsigned i = 1; i <= 28123; ++i) {
        if (is_abundant(i)) {
            abundant_numbers.push_back(i);
        }
    }

    for (unsigned i = 0; i < abundant_numbers.size(); ++i) {
        for (unsigned k = 0; k < abundant_numbers.size(); ++k) {
            unsigned sum = abundant_numbers[i] + abundant_numbers[k];
            if (sum <= 28123) {
                is_sum_of_abundant[sum] = true;
            }
        }
    }

    unsigned total = 0;
    for (unsigned i = 0; i < is_sum_of_abundant.size(); ++i) {
        if (!is_sum_of_abundant[i]) {
            cout << i << endl;
            total += i;
        }
    }

    cout << "Sum of integers that aren't a sum of abundant numbers: " << total << endl;
}

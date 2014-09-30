
for numerator in range(10, 100):
    if numerator % 10 == 0:
        continue
    numerator_digits = [numerator / 10, numerator % 10]
    for denominator in range(numerator + 1, 100):
        denominator_digits = [denominator / 10, denominator % 10]
        false_value = 0
        try:
            if numerator_digits[0] == denominator_digits[0]:
                false_value = float(numerator_digits[1]) / denominator_digits[1]
            elif numerator_digits[0] == denominator_digits[1]:
                false_value = float(numerator_digits[1]) / denominator_digits[0]
            elif numerator_digits[1] == denominator_digits[0]:
                false_value = float(numerator_digits[0]) / denominator_digits[1]
            elif numerator_digits[1] == denominator_digits[1]:
                false_value = float(numerator_digits[0]) / denominator_digits[0]
        except ZeroDivisionError:
            pass
        actual_value = float(numerator) / denominator
        if actual_value == false_value:
            print("%d / %d" % (numerator, denominator))


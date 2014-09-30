for i0 in range(10):
    for i1 in range(10):
        for i2 in range(10):
            for i3 in range(10):
                for i4 in range(10):
                    for i5 in range(10):
                        for i6 in range(10):
                            number = 10**6 * i6 + 10**5 * i5 + 10**4 * i4 + 10**3 * i3 + 10**2 * i2 + 10**1 * i1 + i0
                            powersum = i6**5 + i5**5 + i4**5 + i3**5 + i2**5 + i1**5 + i0**5
                            if number == powersum:
                                print number


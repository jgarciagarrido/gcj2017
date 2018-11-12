def is_tidy(digits):
    if len(digits) == 1:
        return True
    for index in xrange(0, len(digits)-1):
        if digits[index] > digits[index+1]:
            return False
    return True


def last_tidy_number(digits):
    while (not is_tidy(digits)):
        if(digits[-1] == "9"):
            digits = last_tidy_number(digits[:-1])+"9"
        else:
            number = int(digits)-1
            digits = str(number)
    return digits


if __name__ == "__main__":
    t = int(raw_input())  # read a line with a single integer
    for i in xrange(1, t + 1):
        s = raw_input()
        last_tidy = int(last_tidy_number(s))
        print "Case #{}: {}".format(i, last_tidy)

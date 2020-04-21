
def fib(fib_index):
    n_minus_1 = 1
    n_minus_2 = 0
    if fib_index == 0:
        return n_minus_2
    elif fib_index == 1:
        return n_minus_1
    else:
        index = 2
        while index <= fib_index:
            new_number = n_minus_1 + n_minus_2
            # Update our variables aka the reset
            index += 1
            n_minus_2 = n_minus_1
            n_minus_1 = new_number

        return new_number


result = fib(10)
print(result)
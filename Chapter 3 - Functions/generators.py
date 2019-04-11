def fibonacci(count):
    # These seed values generate 0 and 1 when fed into the loop
    a, b = -1, 1

    while count > 0:
        # Yield the value for this iteration
        c = a + b
        yield c

        # Update values for the next iteration
        a, b = b, c
        count -= 1


fib = fibonacci(7)
print(list(fib))
print(list(fib))

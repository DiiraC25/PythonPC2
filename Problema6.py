def fibonacci(n):
    fibonacci_series = [0, 1]
    while fibonacci_series[-1] < n:
        next_number = fibonacci_series[-1] + fibonacci_series[-2]
        if next_number < n:
            fibonacci_series.append(next_number)
        else:
            break
    return fibonacci_series
fibonacci_series = fibonacci(50)
print("Serie de Fibonacci entre 0 y 50:")
print(fibonacci_series)
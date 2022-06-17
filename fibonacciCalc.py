# Fibonacci Calculation Algorithm
# Last updated 17 June 2022

# Non-recursive solution to calculate nth value for Fibonacci sequence 

def fibonacci(n):
     
    # taking 1st two fibonacci numbers as 0 and 1
    f = [0, 1]
     
     
    for i in range(2, n+1):
        f.append(f[i-1] + f[i-2])
    return f[n]
     
print(fibonacci(9))
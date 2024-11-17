def fibonacci(n):
    output = [0,1]
    for i in range(n+1):
        output.append(output[-1] + output[-2])
    print(output)

fibonacci(5)
def factorial(n:int):
    if n<2:
        return 1
    return n*factorial(n-1)

P_x = 0
for i in range(1,7):
    a = factorial(10-i)
    a *= factorial(5)*5
    a /= factorial(6-i)
    P_x+=a

print(P_x/factorial(10))
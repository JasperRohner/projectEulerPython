# Even Fibonacci numbers

res = 0
fib = [1, 2]
while fib[-1] <= 4_000_000:
    fib.append(fib[-2] + fib[-1])
fib.pop()
for elem in fib:
    res += elem if elem % 2 == 0 else 0

print(f"Resultat: {res}") 
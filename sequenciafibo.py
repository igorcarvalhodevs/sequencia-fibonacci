num = int(input("Digite um número: "))
a, b = 0, 1
while b < num:
    a, b = b, a + b
if b == num:
    print(f"{num} pertence à sequência de Fibonacci.")
else:
    print(f"{num} não pertence à sequência de Fibonacci.")
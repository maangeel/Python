#36. Programa que sume los n primeros números naturales. n Lo introduce el usuario
total = 0

num = int(input("Introduce el valor n: "))

for i in range(num+1):
    total += i #suma todos los valores naturales desde 0 hasta el valor n

print(f"La suma total de números naturales es: {total}")
# MI PRIMER SCRIPT.PY
print ("Hola Mundo!")
n = 1000
es_primo = [True] * (n + 1)
es_primo[0] = es_primo[1] = False

for i in range(2, int(n**0.5) + 1):
    if es_primo[i]:
        for j in range(i * i, n + 1, i):
            es_primo[j] = False

primos = [i for i in range(2, n + 1) if es_primo[i]]

print("Números primos entre 1 y 1000:")
print(primos)


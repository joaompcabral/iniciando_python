import random

numero = random.randint(1, 50)
print(f"esse é nosso numero {numero}")

primo = True

if numero <= 1:
    primo = False
else:

    for e in range(2, numero):
        if numero % e == 0:
            primo = False
            break

if primo:
    print(f"o numero {numero} é primo ")
else:
    print(f"o numero {numero} não é primo")

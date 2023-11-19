import random
from time import sleep

op = ["piedra", "papel", "tijeras"]
sep = "-" * 15

while True:
    user = input("elije: piedra. papel o tijeras: ").lower()
    sleep(0.9)
    if user not in op:
        print("\nMovimiento no valido")
        continue
    pc = random.choice(op)
    sleep(0.9)
    print(f"\nLa Pc Selecciono {pc}")
    sleep(0.9)
    if user == pc:
        print(f"\nEmpate, ambos seleccionaron {user}")
    if user == "piedra" and pc == "tijeras":
        print(f"\nganaste, {user} ganas en contra de {pc}")
    if user == "tijeras" and pc == "papel":
        print(f"\nganaste, {user} ganas en contra de {pc}")
    if user == "papel" and pc == "piedra":
        print(f"\nganaste, {user} ganas en contra de {pc}")
    else:
        print(f"\nPerdiste, {user} pierdes contra {pc}")
        sleep(0.9)
        print(f"{sep} fin del Juego {sep}")

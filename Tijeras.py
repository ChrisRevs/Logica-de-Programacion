import random
from time import sleep

op = ["piedra", "papel", "tijeras"]
sep = "-" * 15

while True: #Utilizo un codigo while true para repetir el juego de manera indefinida 
    user = input("elije: piedra. papel o tijeras: ").lower()
    sleep(0.9)
    if user not in op: #uso de if y not in de caracter tipo boolean
        print("\nMovimiento no valido")
        continue
    pc = random.choice(op)
    sleep(0.9) #sleep para provocar un tiempo de espera antes de mostrar el resultado 
    print(f"\nLa Pc Selecciono {pc}")
    sleep(0.9)
    if user == pc: #variante boolean tipo true 
        print(f"\nEmpate, ambos seleccionaron {user}")
    if user == "piedra" and pc == "tijeras":
        print(f"\nganaste, {user} ganas en contra de {pc}")
    if user == "tijeras" and pc == "papel":
        print(f"\nganaste, {user} ganas en contra de {pc}")
    if user == "papel" and pc == "piedra":
        print(f"\nganaste, {user} ganas en contra de {pc}")
    else: #variante boolean false 
        print(f"\nPerdiste, {user} pierdes contra {pc}")
        sleep(0.9)
        print(f"{sep} fin del Juego {sep}")

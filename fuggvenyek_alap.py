import random
import fuggvenyeim as f

x = f.szamot_beker("add meg az x értékét: ")
print(f'{x} tízszerese: {10 * x}')

y = f.szamot_beker("írj be egy másik számot is: ")
print(f'ez pedig a másik szám: {y}')


lista_1 = f.random_lista(10, 5, 100)
print(lista_1)

lista_2 = f.random_lista(200, 4, 10)
print(lista_2)
















# függvény
szam = random.randint(10, 100)

# eljárás (avagy olyan "függvény", ami nem tér vissza semmivel - azaz nem lehet/nincs értelme egyenlővé tenni egy értékkel/változóval)
print("hello!")

#ami a zárójelben van, azt úgy hívjuk, h 'paraméter'
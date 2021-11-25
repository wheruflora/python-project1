import random

menu = ["Americano","Latte","milk","Heytea","Allcoconut","water",]

print("Menu:",menu)

while True:
    name = input("Your name please (\'quit\' for quit): ")

    if name == 'quit':
        break

    if name == 'wheruflora':
        drink = 'Heytea'
    else:
        drink=random.choice(menu)

    print("Hello " + name + "! Enjoy your " + drink)

print('Bye')


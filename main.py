import random

choices = ['камень', 'ножницы', 'бумага']

print("Давай сыграем в камень ножницы бумага")

while True:
    print ()
    user_ans = input('Су-е-фа  ')
    random_choice = random.choice(choices)
    print(random_choice)

    if user_ans == 'камень' and random_choice == 'ножницы':
        print('Ты выиграл')
    elif user_ans == 'бумага' and random_choice == 'камень':
        print('Ты выиграл')
    elif user_ans == 'ножницы' and random_choice == 'бумага':
        print('Ты выиграл')

    else:
        print('Ты проиграл')

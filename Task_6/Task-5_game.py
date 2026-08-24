import random

random_num = random.randint(1, 20)
tries = 5

print(f'Я загадал число от 1 до 20. У тебя {tries} попыток!')

while tries > 0:
    guess = int(input(f'Попытка {6 - tries}: Введите число: '))
    tries -= 1
    if guess < random_num:
        print('Cлишком мало! Осталось попыток:', tries)
    elif guess > random_num:
        print('Cлишком много! Осталось попыток:', tries)
    else:
        print(f'Ты угадал! Отличная работа!')
        break
else:
    print(f'Ты не угадал. Я загадал число {random_num}.')
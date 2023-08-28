import random
pairs = {}
g = int(input("сколько слов хотите повторить? : "))
i = 0
while i != g :
    eng_word = input(f"Введите английское слово{i+1} : ")
    ru_word = input(f"Введите перевод для слова {eng_word}: ")
    pairs[ru_word] = eng_word
    i+=1

def slovar ():
    i = 0
    while i != g:
        random_keys = random.choice(list(pairs.keys()))
        translation = input(f"напишите перевод '{random_keys}': ")
        while translation !=pairs[random_keys] :
            translation = input("попробуйте еще раз ")
        print ("Правильно")
        del pairs[random_keys]
        i+=1
world = slovar()
print("Молодец, на этом всё")
print(world)



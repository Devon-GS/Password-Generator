import random
import string

def generate_password(user_input):
    characters = string.printable[:95]*10
    get_random_char = (random.sample(characters, user_input))
    shuffle_char = random.sample(get_random_char, user_input)
    password = " ".join(shuffle_char).replace(" ","")
    print(f"You Generated pasword is: {password}")

right_input = 0
while right_input != 1:
    try:
        user_input = int(input("Choose a lenght for password: (min. 6 and max. 25 characters): "))
        if user_input < 6 or user_input > 25:
            print(f"The number {user_input} is out of range!...Please choose a number between 6 and 25")
            continue
        right_input += 1
    except:
        print("Wrong input, only whole numbers allowed.")     


generate_password(user_input)

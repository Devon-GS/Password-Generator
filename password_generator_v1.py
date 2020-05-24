import random
import string

lis_cap = list(string.ascii_uppercase)
lis_letter = list(string.ascii_lowercase)
lis_special = ["!", "@", "#", "$", "%", "&", "*"]
lis_num = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]


get_cap = ""
get_letters = ""
get_special = ""
get_num = ""

cap = 0
letter = 0
special = 0
num = 0

cap_input = 0
letter_input = 0
special_input = 0
num_input = 0

user = input("Please select 8 or 12 characters long: ")

if user == "8":
    cap_input = 2
    letter_input = 4
    special_input = 1
    num_input = 1
else:
    cap_input = 4
    letter_input = 6
    special_input = 1
    num_input = 1   

while cap != cap_input:
    get_cap += random.choice(lis_cap)
    cap += 1
    
while letter != letter_input:
    get_letters += random.choice(lis_letter)
    letter += 1
    
while special != special_input:
    get_special += random.choice(lis_special)
    special += 1

while num != num_input:
    get_num += random.choice(lis_num)
    num += 1

gen_pass = get_cap + get_letters + get_special + get_num    

password = ''.join(random.sample(gen_pass, len(gen_pass)))
# print(f"Your generated password is: {password}")
print("Your generated password is: " + password)

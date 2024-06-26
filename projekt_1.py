"""

projekt_1.py: první projekt do Engeto Online Python Akademie

author: Jana Kučerová

email: vocurca@seznam.cz

discord: Jana Kučerová

"""
import re

from projekt_1_task_template import TEXTS

separation = "-" * 40

# zjištení počtu textů
TEXTS_count = len(TEXTS)

# registrovaní uživatelé
users = {
    "bob" : "123",
    "ann" : "pass123",
    "mike" : "password123",
    "liz" : "pass123"
}
# ověření uživatele
user = input("Enter username: ")
password = input("Enter password: ")
print(separation)

if (user in users) and (password == users[user]):
    print("Welcome to the app,", user)
    print("We have", TEXTS_count, "texts to be analyzed.")
    print(separation)
else:
    print("Unregistered user, terminating the program...")
    exit()

# výběr textu
try:
    text_number = int(input(f"Enter a number btw. 1 and {TEXTS_count} to select: "))
except:
    print(separation)
    print("This is not a number. Terminating the program...")
    exit()
else:
    print(separation)

if (text_number > 0) and (text_number <= (TEXTS_count)):
    selected_text = TEXTS[text_number-1]
    
    # očištění textu
    words = re.findall(r"\b[a-zA-Z0-9]+\b", selected_text)

    # počet slov
    print("There are", len(words), "words in the selected text.")   
    
    sum_title = []
    sum_upper = []
    sum_lower = []
    count_numbers = []
    sum_numbers = []

    for word in words:
        if word.isalpha():
            # počet slov s velkým písmenem na začátku
            if word.istitle() or word.isupper():
                sum_title.append(word)
        
            # počet slov kapitálkami
            if word.isupper():
                sum_upper.append(word)
        
            # počet slov malým písmenem
            if word.islower():
                sum_lower.append(word)
        
        elif word.isnumeric():
            number = int(word)
            
            # počet čísel
            count_numbers.append(number)
            
            # součet všech čísel
            sum_numbers.append(number)        

    print("There are", len(sum_title), "titlecase words.")  
    print("There are", len(sum_upper), "uppercase words.")
    print("There are", len(sum_lower), "lowercase words.")
    print("There are", len(count_numbers), "numeric strings.")
    print("The sum of all numbers is", sum(sum_numbers), "\b.")
  
    # hlavička grafu s délkou slov a počtem výskytu
    print(separation)   
    print("  LEN| OCCURENCES     |NR.") 
    print(separation)

    # počet výskytu
    list_lenghts = []
    for word in words:
        word_lenght = len(word)
        list_lenghts.append(word_lenght)
    
    dict_lenghts = dict()
    for number in list_lenghts:
        if number not in dict_lenghts:
            dict_lenghts[number] = 1
        else:
            dict_lenghts[number] += 1
    
    sorted_lenghts = dict(sorted(dict_lenghts.items()))
   
    # tisk hodnot do grafu
    values = list(sorted_lenghts.values())
    values.sort()
    
    for number in sorted_lenghts:
        if number < 10:
            print("  ", number, "|", "*" * sorted_lenghts.get(number), " " * ((values[-1] + 1) - sorted_lenghts.get(number)), "|", sorted_lenghts.get(number))
        else:
            print(" ", number, "|", "*" * sorted_lenghts.get(number), " " * ((values[-1] + 1) - sorted_lenghts.get(number)), "|", sorted_lenghts.get(number))
    print(separation)
    
else:
    print(f"{text_number} is not the number btw. 1 and {TEXTS_count}. Terminating the program...")
    exit()
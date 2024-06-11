"""

projekt_1.py: první projekt do Engeto Online Python Akademie

author: Jana Kučerová

email: vocurca@seznam.cz

discord: Jana Kučerová
        vocurcavocurca

"""

from projekt_1_task_template import TEXTS

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
separation = "-" * 40
print(separation)

if (user in users) and (password in users[user]):
    print("Welcome to the app,", user)
    print("We have 3 texts to be analyzed.")
    print(separation)
else:
    print("Unregistered user, terminating the program...")
    exit()

# výběr textu
text_number = int(input("Enter a number btw. 1 and 3 to select: "))
print(separation)

if (text_number > 0) and (text_number < 4):
    selected_text = TEXTS[text_number-1]
    
    # očištění textu
    uncleaned_words = list(selected_text.split())
    words = []
    for word in uncleaned_words:
        cleaned_word = word.strip(",.")
        words.append(cleaned_word)

    # počet slov
    print("There are", len(words), "words in the selected text.")
    
    # počet slov s velkým písmenem na začátku
    sum_title = []
    for word in words:
        if word.istitle():
            sum_title.append(word)
    print("There are", len(sum_title), "titlecase words.")

    # počet slov kapitálkami
    sum_upper = []
    for word in words:
        if word.isupper() and (word.isnumeric() or word.isalpha()):
            sum_upper.append(word)
    print("There are", len(sum_upper), "uppercase words.")

    # počet slov malým písmenem
    sum_lower = []
    for word in words:
        if word.islower():
            sum_lower.append(word)
    print("There are", len(sum_lower), "lowercase words.")
    
    # počet čísel
    count_numbers = []
    for word in words:
        if word.isnumeric():
            number = int(word)
            count_numbers.append(number)
    print("There are", len(count_numbers), "numeric strings.") 

    # součet všech čísel
    sum_numbers = []
    for word in words:
        if word.isnumeric():
            number = int(word)
            sum_numbers.append(number)
    print("The sum of all numbers is", sum(sum_numbers), "\b.")
  
    # hlavička grafu s délkou slov a počtem výskytu
    print(separation)   
    print("  LEN|  OCCURENCES    |NR.") 
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
   
    # tisk hodnot
    for number in sorted_lenghts:
        if number < 10:
            print("  ", number, "|", "*" * sorted_lenghts.get(number), " " * (13 - sorted_lenghts.get(number)), "|", sorted_lenghts.get(number))
        else:
            print(" ", number, "|", "*" * sorted_lenghts.get(number), " " * (13 - sorted_lenghts.get(number)), "|", sorted_lenghts.get(number))

    
else:
    print(text_number, "is not the number btw. 1 and 3. Terminating the program...")
    exit()
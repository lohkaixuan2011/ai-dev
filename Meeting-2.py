from logging import getLogRecordFactory
import random
import string

"""LIST"""

grocery_list = ['Bread', 'Cereal', 'Butter']
# print(grocery_list)

# print(grocery_list[0])
# print(grocery_list[1])
# print(grocery_list[2])

grocery_list.append('Sausage')  # Append = adding
grocery_list.append('Croissant')
grocery_list.remove('Bread')  # Remove = delete
# print(grocery_list)

grocery_list[1] = 'Strawberry Jam'
# print(grocery_list)
# print(len(grocery_list))

numbers = [130, 110, 140, 150, 190, 200, 250, 200, 230, 250]
numbers.sort()
# print(numbers)

grade_3 = numbers[:4]
# print(grade_3)
grade_2 = numbers[4:7]
# print(grade_2)
grade_1 = numbers[7:]
# print(grade_1)

ages = [14, 15, 8, 10, 17, 18, 20, 21, 19, 10, 25, 21, 10, 20, 15]
ages.sort()

new_ages = ages[7:15]
# print(new_ages)

temperature = [
    [25, 27, 28, 27],
    [23, 24, 26, 26],
    [24, 24, 27, 27],
    [22, 24, 25, 24]
]
# print(temperature)
# print(temperature[0])
# print(temperature[0][0])

temperature.append([23, 24, 24, 26])
# print(temperature)
# print(len(temperature))

temperature[2][1] = 27
# print(temperature[2])

"""TUPLE"""

subjects = ("Python", "C++", "JavaScript")
# print(subjects[-1])
# print(subjects[1])
# print(subjects[0:2])
# print("Python" in subjects)
# print("Java" in subjects)

# subjects[1] = "C++"
# print(subjects[1])

subject1, subject2, subject3 = subjects
# print(subject1)
# print(subject2)
# print(subject3)

"""DICTIONARY"""

movie = {
    'tittle': 'Jumanji : The  Next Level',
    'year': 2017,
    'genre': 'Adventure',
}

movie_2 = {
    'title': 'Frozen 2',
    'year': 2019,
    'genre': 'Family'
}

# print(movie['tittle'])

movie.update({'viewers': 44324578})
movie["genre"] = "Adventure/Comedy"
del movie['year']

movie_2.update({'viewers': 98698637})
movie_2["genre"] = "Family/Musical"

friends_list = ['Bryan', 'Cia', 'Petter', 'Drake']
random_name = random.choice(friends_list)
random_number = random.randint(10, 15)
# print(random_name)
# print(random_number)

# print("Welcome to Password Maker!")

adjectives_list = ["sleepy", "slow", "fluffy", "red", "yellow", "green", "blue"]
nouns_list = ["Dinosaur", "Ball", "Dragon", "Hammer", "Apple", "Duck", "Panda"]

adjective = random.choice(adjectives_list)
noun = random.choice(nouns_list)
number = random.randrange(0, 100)
char = random.choice(string.punctuation)

password = adjective + noun + str(number) + char
# print("Recommended password: " + password)

print("Welcome to the email maker")

username_list = ["Kaixuan", "Cobee", "Kaizen", "Kairo", "Kayson", "Kael", "Kian", "Kairox", "Kaiven"]
verbs_list = ["Create", "Build", "Code", "Explore", "Learn", "Discover", "Imagine", "Design", "Develop", "Create"]

username = random.choice(username_list)
verbs = random.choice(verbs_list)
number = random.randrange(0, 100)

email = username + verbs + str(number)

print("Recommended email: " + email + "@mail.com")
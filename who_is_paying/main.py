import random

# initiating the random number generator the importance of really using the random.seed is that we can control it
# therefore this means it is not totally random ....the number specified in the random module means that its
#  point of start

seed_number = int(input("create a seed number"))
random.seed(seed_number)

# using the split method

name = input("write everybody's name here separated by a comma ")
names = name.split(",")

# getting the number of people

num_people = (len(names))

# generating numbers between 0 and the last index

random_choice = random.randint(0, num_people - 1)
person_will_pay = names[random_choice]
print(person_will_pay + "the person who will pay is ")

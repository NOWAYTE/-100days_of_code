print("welcome to the love calculator")
name_1 = input("what is your name ")
name_2 = input("what is their name ")

combined_name = name_1 + name_2
lower_case_string = combined_name.lower()

t = lower_case_string.count("t")
r = lower_case_string.count("r")
u = lower_case_string.count("u")

true = t + r + u

l = lower_case_string.count("l")
o = lower_case_string.count("o")
v = lower_case_string.count("v")
e = lower_case_string.count("e")

love = l + o + v + e

compatibility = int(str(true) + str(love))

if (compatibility < 10) or (compatibility > 90):
    print(f"your love score is {compatibility}, you go together like coke and mentos ")

elif 40 <= compatibility <= 50:
    print(f"your love score {compatibility}, you are alright together ")

else:
    print(f"you score is {compatibility}, better get rolling ")

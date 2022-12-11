#100days python bootcamp
#love calculator
#3rd day

print("welcome to love calculator")
name1 = input("Enter 1st name : ")
name2 = input("Enter second name :")
combined_string = name1 + name2
lower_string = combined_string.lower()
print(lower_string)
t = lower_string.count("t")
r = lower_string.count("r")
u = lower_string.count("u")
e = lower_string.count("e")
true = t + r + u + e
l = lower_string.count("l")
o = lower_string.count("o")
v = lower_string.count("v")
e = lower_string.count("e")
love = l + o + v + e

love_score = int(str(true) + str(love))
if (love_score < 10) or (love_score > 90):
    print(f"your score is {love_score}, you are like coke and mentos . ")
elif (love_score >= 40) and  (love_score <=50):
    print(f"your score is {love_score}, you are good together . ")
else:
    print(f"your score is {love_score} , good")
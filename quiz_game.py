print("Welcome to Rob's Quiz Game!")
print("This is a Computer Knowledge Quiz Game!")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print("Okay! Let's play :) ")

#Question 1
answer = input("What does CPU stand for? ")
if answer == "central processing unit":
    print("Correct!")
else:
    print("Incorrect!")

#Question 2
answer = input("What does GPU stand for? ")
if answer == "graphics processing unit":
    print("Correct!")
else:
    print("Incorrect!")

#Question 3
answer = input("What does RAM stand for? ")
if answer == "random access memory":
    print("Correct!")
else:
    print("Incorrect!")

#Question 4
answer = input("What does LCD stand for? ")
if answer == "liquid crystal display":
    print("Correct!")
else:
    print("Incorrect!")

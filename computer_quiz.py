print("Welcome to my computer quiz!")

playing = input("Do yo want to play? ")
if playing.lower() != "yes":
    quit()
    
else:
    print("Okay! Let's play :)")
    score = 0
    answer = input("What does CPU stands for?")
    if answer.lower()== "central processing unit":
        print ('correct')
        score += 1
    else:
        print("Incorrect!")
    answer = input("What does RAM stands for ?")
    if answer.lower()=="random access memory":
        print('Correct!')
        score += 1
    else:
        print("Incorrect!")
    answer = input("What does PSU stand for?")
    if answer.lower() == "power supply":
        print('Correct!')
        score += 1
    else:
        print("Incorrect!")
print ("You got " + str(score) + "questions correct!")
print ("You got " +str(score/3*100) + "%")
                
                      
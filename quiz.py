import requests
import json
import random

wantsToPlay = True
user_score = 0
level = 1

print("================================")
print("Welcome to the Ultimate Quiz Challenge: ")
print("Here you can see what level of quiz knowledge you're on!")
print(" ")
print("Levels of Knowledge according to Points: ")
print("0 - 5 points: Beginner")
print("5 - 10 points: Expert Marksman")
print("10 - 35 points: Heavenly")
print("35 - 49 points: Devilish")
print("50 points: Godly King")
print(">50 points: Jack of All Trades || One Who Sees And Knows All")
print(" ")
print("Rules")
print(" ")
print("There will be a 3 level system based on the player score")
print("You are awarded 1 point for every correct answer")
print("After 35 points, 1 point will be deducted every wrong answer")
print(" ")
print("0 - 10 points: Level 1")
print("10 - 50 points: Level 2")
print(">50 points: Level 3")
print("Level 1 will have easy questions")
print("Level 2 will have mediumly tough questions")
print("Level 3 will have hard questions")
print("================================")
print(" ")
print(" ")


print("Have you read and Understood the rules")
choice = input("Type y for yes and n for no: ")

if(choice.lower() == "y" or choice.lower() == "yes"):
  wantsToPlay = True
  print("Lets get this game going then!")
elif(choice.lower() == "n" or choice.lower() == "no"):
  wantsToPlay = False
  print("Okay! We'll play later then I guess! Have a good day!")
else:
  print("Sorry! Invalid choice")

while(wantsToPlay):
  if(user_score >=0 and user_score <= 10):
    r = requests.get("https://opentdb.com/api.php?amount=1&difficulty=easy&type=multiple")
    response_text = json.loads(r.text)

    question = response_text['results'][0]['question']
    initial_answer_array = []
    correct_answer = response_text['results'][0]['correct_answer']
    initial_answer_array.append(correct_answer)
    for x in range(0,3):
      initial_answer_array.append(response_text['results'][0]['incorrect_answers'][x])
    
    random.shuffle(initial_answer_array)
    correct_answer_index = 0
    for y in range(0,3):
      if(initial_answer_array[y] == correct_answer):
        correct_answer_index = y

    index_array = ["A","B","C","D"]

    print(question)
    for x in range(0,len(initial_answer_array)):
      print(index_array[x]+" : "+initial_answer_array[x])

    user_answer = input("Type your answer here: ")
    if(user_answer.lower() == index_array[correct_answer_index].lower()):
      user_score = user_score + 1
      print("Wow! That was the correct answer! Good job!")
      print("Your current score is: "+str(user_score))
      print("You are on Level "+str(level))
    
    else:
      print("Sorry, the correct answer was: "+correct_answer)
      print("Your current score is: "+str(user_score))
      print("You are on Level "+str(level))

  elif(user_score >10  and user_score <= 35):
    level = 2
    r = requests.get("https://opentdb.com/api.php?amount=1&difficulty=medium&type=multiple")
    response_text = json.loads(r.text)

    question = response_text['results'][0]['question']
    initial_answer_array = []
    correct_answer = response_text['results'][0]['correct_answer']
    initial_answer_array.append(correct_answer)
    for x in range(0,3):
      initial_answer_array.append(response_text['results'][0]['incorrect_answers'][x])
    
    random.shuffle(initial_answer_array)
    correct_answer_index = 0
    for y in range(0,3):
      if(initial_answer_array[y] == correct_answer):
        correct_answer_index = y

    index_array = ["A","B","C","D"]

    print(question)
    for x in range(0,len(initial_answer_array)):
      print(index_array[x]+" : "+initial_answer_array[x])

    user_answer = input("Type your answer here: ")
    if(user_answer.lower() == index_array[correct_answer_index].lower()):
      user_score = user_score + 1
      print("Wow! That was the correct answer! Good job!")
      print("Your current score is: "+str(user_score))
      print("You are on Level "+str(level))
    
    else:
      print("Sorry, the correct answer was: "+correct_answer)
      print("Your current score is: "+str(user_score))
      print("You are on Level "+str(level))

  elif(user_score >35 and user_score <=50):
    level = 2
    r = requests.get("https://opentdb.com/api.php?amount=1&difficulty=medium&type=multiple")
    response_text = json.loads(r.text)

    question = response_text['results'][0]['question']
    initial_answer_array = []
    correct_answer = response_text['results'][0]['correct_answer']
    initial_answer_array.append(correct_answer)
    for x in range(0,3):
      initial_answer_array.append(response_text['results'][0]['incorrect_answers'][x])
    
    random.shuffle(initial_answer_array)
    correct_answer_index = 0
    for y in range(0,3):
      if(initial_answer_array[y] == correct_answer):
        correct_answer_index = y

    index_array = ["A","B","C","D"]

    print(question)
    for x in range(0,len(initial_answer_array)):
      print(index_array[x]+" : "+initial_answer_array[x])

    user_answer = input("Type your answer here: ")
    if(user_answer.lower() == index_array[correct_answer_index].lower()):
      user_score = user_score + 1
      print("Wow! That was the correct answer! Good job!")
      print("Your current score is: "+str(user_score))
      print("You are on Level "+str(level))
    
    else:
      print("Sorry, the correct answer was: "+correct_answer)
      print("Your current score is: "+str(user_score))
      print("You are on Level "+str(level))

  elif( user_score >= 50):
    level = 3
    r = requests.get("https://opentdb.com/api.php?amount=1&difficulty=hard&type=multiple")
    response_text = json.loads(r.text)

    question = response_text['results'][0]['question']
    initial_answer_array = []
    correct_answer = response_text['results'][0]['correct_answer']
    initial_answer_array.append(correct_answer)
    for x in range(0,3):
      initial_answer_array.append(response_text['results'][0]['incorrect_answers'][x])
    
    random.shuffle(initial_answer_array)
    correct_answer_index = 0
    for y in range(0,3):
      if(initial_answer_array[y] == correct_answer):
        correct_answer_index = y

    index_array = ["A","B","C","D"]

    print(question)
    for x in range(0,len(initial_answer_array)):
      print(index_array[x]+" : "+initial_answer_array[x])

    user_answer = input("Type your answer here: ")
    if(user_answer.lower() == index_array[correct_answer_index].lower()):
      user_score = user_score + 1
      print("Wow! That was the correct answer! Good job!")
      print("Your current score is: "+str(user_score))
      print("You are on Level "+str(level))
    
    else:
      user_score = user_score - 1
      print("Sorry, the correct answer was: "+correct_answer)
      print("Your current score is: "+str(user_score))
      print("You are on Level "+str(level))


  choice = input("Do you want to continue playing? If yes, then type y else type n: ")
  if(choice == "y"):
    continue
  elif(choice == "n"):
    print("===================================================")
    print("Your final score was: "+str(user_score))
    if(user_score >= 0 and user_score<=5):
      print("Your level of knowledge is: Beginner")
    elif(user_score >5 and user_score<=10):
      print("Your level of knowledge is: Expert Marksman")
    elif(user_score>10 and user_score<=25):
      print("Your level of knowledge is: Heavenly")
    elif(user_score>25 and user_score<=49):
      print("Your level of knowledge is: Devilish")
    elif(user_score == 50):
      print("Your level of knowledge is: Godly King")
    else:
      print("Your level of knowledge is: Jack of All Trades || One Who Sees And Knows All")


    print("Thanks for playing the game! Hope you enjoyed!")
    print("===================================================")
    user_score = 0
    break

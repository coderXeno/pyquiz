import requests
import json
import random

wantsToPlay = True
user_score = 0

while(wantsToPlay):
  r = requests.get("https://opentdb.com/api.php?amount=1&difficulty=easy&type=multiple")
  response_text = json.loads(r.text)

  question = response_text['results'][0]['question']
  initial_answer_array = []
  correct_answer = response_text['results'][0]['correct_answer']
  initial_answer_array.append(correct_answer)
  for x in range(0,3):
    initial_answer_array.append(response_text['results'][0]['incorrect_answers'][x])
  
  random.shuffle(initial_answer_array)
  index_array = ["A","B","C","D"]

  print(question)
  for x in range(0,len(initial_answer_array)):
    print(index_array[x]+" : "+initial_answer_array[x])

  user_answer = input("Type your answer here: ")
  if(user_answer == correct_answer):
    user_score = user_score + 1
    print("Wow! That was the correct answer! Good job!")
    print("Your current score is: "+str(user_score))
  
  else:
    print("Sorry, the correct answer was: "+correct_answer)
    print("Your current score is: "+str(user_score))

  choice = input("Do you want to continue playing? If yes, then type y else type n: ")
  if(choice == "y"):
    continue
  elif(choice == "n"):
    print("Your final score was: "+str(user_score))
    print("Thanks for playing the game! Hope you enjoyed!")
    user_score = 0
    break

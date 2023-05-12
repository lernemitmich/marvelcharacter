print("Let me guess! Which Marvel Movie character are you?")

correct_answer = False

ques1 = input("Do you like to hang around? ")
if ques1.lower() == "yes": 
  print("Then you are Spider-Man.")
  correct_answer = True

if not correct_answer:
  ques2 = input("Do you like bats? ")
  if ques2.lower() == "yes": 
    print("Then you are Batman.")
    correct_answer = True

if not correct_answer:
  ques3 = input("Are you a billionaire and inventor? ")
  if ques3.lower() == "yes": 
    print("Then you are Iron Man.")
    correct_answer = True

if not correct_answer:
  ques4 = input("Are you a soldier, skilled fighter, and leader? ")
  if ques4.lower() == "yes": 
    print("Then you are Captain America.")
    correct_answer = True

if not correct_answer:
  ques5 = input("Are you the God of Thunder and an Asgardian prince? ")
  if ques5.lower() == "yes": 
    print("Then you are Thor.")
    correct_answer = True

if not correct_answer:
  ques6 = input("Are you a neurosurgeon and master of mystics? ")
  if ques6.lower() == "yes": 
    print("Then you are Doctor Strange.")
    correct_answer = True

if not correct_answer:
  ques7 = input("Are you an expert thief and able to shrink and grow? ")
  if ques7.lower() == "yes": 
    print("Then you are Ant-Man.")
    correct_answer = True

if not correct_answer:
  print("Sorry, I couldn't guess which Marvel Movie character you are.")

name = input("Tell me your real name? ")
print("Welcome, " + name + "!")

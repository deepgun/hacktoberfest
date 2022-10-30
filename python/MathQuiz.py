import random
print("Welcome to the arithmetic quiz! When doing divison problems, be sure to round down.")
print("Well, have fun! Also, if you ever want to quit, just press \"q\".")
counter = 0
correct = 0
incorrect = 0
while True:
  num1 = random.randint(1, 10)
  num2 = random.randint(1, 10)
  op = random.randint(1, 6)
  if op == 1:
    op = "+"
  elif op == 2:
    op = "-"
  elif op == 3:
    op = "*"
  elif op == 4:
    op = "/"
  elif op == 5:
    op = "%"
  else:
    op = "**"
  checkForExceptions = num1 < num2 and op == "/" or num1 > num2 and num2 == 0 and op == "/" or num1 < num2 and op == "%" or num1 > num2 and num2 == 0 and op == "%"
  while checkForExceptions:
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    op = random.randint(1, 6)
    if op == 1:
      op = "+"
    elif op == 2:
      op = "-"
    elif op == 3:
      op = "*"
    elif op == 4:
      op = "/"
    elif op == 5:
      op = "%"
    else:
      op = "**"
  print(num1, op, num2, "=")
  question = input()
  if question == "q":
    break
  elif op == "+":
    correctAnswer = num1 + num2
    if int(question) == correctAnswer:
      print("Correct!")
      counter += 1
      correct += 1
    else:
      print("Incorrect!")
      counter += 1
      incorrect += 1
  elif op == "-":
    correctAnswer = num1 - num2
    if int(question) == correctAnswer:
      print("Correct!")
      counter += 1
      correct += 1
    else:
      print("Incorrect!")
      counter += 1
      incorrect += 1
  elif op == "*":
    correctAnswer = num1 * num2
    if int(question) == correctAnswer:
      print("Correct!")
      counter += 1
      correct += 1
    else:
      print("Incorrect!")
      counter += 1
      incorrect += 1
  elif op == "/":
    correctAnswer = int(num1 / num2)
    if int(question) == correctAnswer:
      print("Correct!")
      counter += 1
      correct += 1
    else:
      print("Incorrect!")
      counter += 1
      incorrect += 1
  elif op == "%":
    correctAnswer = num1 % num2
    if int(question) == correctAnswer:
      print("Correct!")
      counter += 1
      correct += 1
    else:
      print("Incorrect!")
      counter += 1
      incorrect += 1
  else:
    correctAnswer = num1 ** num2
    if int(question) == correctAnswer:
      print("Correct!")
      counter += 1
      correct += 1
    else:
      print("Incorrect!")
      counter += 1
      incorrect += 1
if counter == 0:
  print("Yay! You finished!")
  print("Correct: 0% (0/0)")
  print("Incorrect: 0% (0/0)")
  print("Bye!")
else:
  print("Yay! You finished!")
  correctPercent = 100 / counter
  correctPercent *= correct
  incorrectPercent = 100 / counter
  incorrectPercent *= incorrect
  print("Correct:", str(correctPercent) + "% (" + str(correct) + "/" + str(counter) + ")")
  print("Incorrect:", str(incorrectPercent) + "% (" + str(incorrect) + "/" + str(counter) + ")")
  print("Bye!")

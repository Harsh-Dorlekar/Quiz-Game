score = 0

print("Welcome to My Computer Quiz")

playing = input("Do you want to Play? ")

if playing != "yes":
    quit()

print("Okay! Let's Play")

answer = input("1. What is the capital of France? ")
if answer.lower() == "paris":
    print('Correct!')
    score = score +1
else:
    print("incorrect")
    print("Your Final Score is: ",score)

answer = input("2. What is the largest ocean in the world?  ")
if answer.lower() == "pacific ocean":
    print('Correct!')
    score = score +1
else:
    print("incorrect")
    print("Your Final Score is: ",score)

answer = input("3. What is the longest river in the world? ")
if answer.lower() == "nile river":
    print('Correct!')
    score = score +1
else:
    print("incorrect")
    print("Your Final Score is: ",score)

answer = input("4. What is the tallest mountain in the world? ")
if answer.lower() == "mount everest":
    print('Correct!')
    score = score +1
else:
    print("incorrect")
    print("Your Final Score is: ",score)

answer = input("5. How many colors are there in a rainbow? ")
if answer.lower() == "Seven":
    print('Correct!')
    score = score +1
else:
    print("incorrect")
    print("Your Final Score is: ",score)

answer = input("6. What is the most populous country in the world? ")
if answer.lower() == "china":
    print('Correct!')
    score = score +1
else:
    print("incorrect")
    print("Your Final Score is: ",score)

answer = input("7. How many continents are there in the world? ")
if answer.lower() == "seven":
    print('Correct!')
    score = score +1
else:
    print("incorrect")
    print("Your Final Score is: ",score)

answer = input("8. What is the coldest continent on Earth? ")
if answer.lower() == "antarctica":
    print('Correct!')
    score = score +1
else:
    print("incorrect")
    print("Your Final Score is: ",score)

answer = input("9. What is the most spoken language in the world? ")
if answer.lower() == "mandarin chinese":
    print('Correct!')
    score = score +1
else:
    print("incorrect")
    print("Your Final Score is: ",score)

answer = input("10. What is the chemical symbol for Iron? ")
if answer.lower() == "fe":
    print('Correct!')
    score = score +1
else:
    print("incorrect")
    print("Your Final Score is: ",score)

answer = input("11. What is the currency of Japan? ")
if answer.lower() == "japanese yen":
    print('Correct!')
    score = score +1
else:
    print("incorrect")
    print("Your Final Score is: ",score)

answer = input("12. What is the capital of India? ")
if answer.lower() == "new delhi":
    print('Correct!')
    score = score +1
else:
    print("incorrect")
    print("Your Final Score is: ",score)

answer = input("13. What is the capital of the United States? ")
if answer.lower() == "washington dc":
    score = score +1
else:
    print("incorrect")
    print("Your Final Score is: ",score)

answer = input("14. What is the biggest desert in the world? ")
if answer.lower() == "sahara desert":
    print('Correct!')
    score = score +1
else:
    print("incorrect")
    print("So Close Better luck Next Time!")
    print("Your Final Score is: ",score)

answer = input("15. What is the longest mountain range in the world? ")
if answer.lower() == "the andes":
    print('Correct!')
    score = score +1
else:
    print("incorrect")
    print("So Close Better luck Next Time!")
    print("Your Final Score is: ",score)

answer = input("16. What is the second-largest planet in the solar system? ")
if answer.lower() == "saturn":
    print('Correct!')
    score = score +1
else:
    print("incorrect")
    print("So Close Better luck Next Time!")
    print("Your Final Score is: ",score)

answer = input("17. How many sides does a triangle have? ")
if answer.lower() == "three":
    print('Correct!')
    score = score +1
else:
    print("incorrect")
    print("So Close Better luck Next Time!")
    print("Your Final Score is: ",score)

answer = input("18. What is the hottest planet in the solar system? ")
if answer.lower() == "venus":
    print('Correct!')
    score = score +1
else:
    print("incorrect")
    print("So Close Better luck Next Time!")
    print("Your Final Score is: ",score)

answer = input("19. What is the symbol for the element Oxygen? ")
if answer.lower() == "o":
    print('Correct!')
    score = score +1
else:
    print("incorrect")
    print("So Close Better luck Next Time!")
    print("Your Final Score is: ",score)

answer = input("20. What is the capital of Australia? ")
if answer.lower() == "canberra":
    print('Correct!')
    score = score +1
    print("CONGRATULATIONS!! YOU HAVE PASSES THE QUIZ!!")
    print("YOUR FINAL SCORE IS: ",score," out of 20")
else:
    print("incorrect")
    print("So Close Better luck Next Time!")
    print("Your Final Score is: ",score)


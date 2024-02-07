import random

print("Hello, what is ur name?")
ans = input()




scores = 0
pcscores = 0
again = "Yes"
while again == "yes":
    totaltry = 0
    NumToGuess = random.randint(1,101)
    print(f"Well, {ans}, I am thinking of a number between 1 and 100.")
    while NumToGuess < 102: #При вопросе почему именно 102,Отвечу - Потому что 
        user_num = int(input("Take a Guess: "))
        if user_num > NumToGuess:
            print("Lower")
            totaltry += 1
            pcscores += 1
        elif user_num < NumToGuess:
            print("Larger")
            pcscores += 1
            totaltry += 1
        elif user_num == NumToGuess:
            scores += 1
            totaltry += 1
            print("Gj")
            print("total trys: ", totaltry)
            print("Scores: ", scores, ":", pcscores)
            again = input("Do u want to play again(Yes,no)").lower()
            break
print('Thank you for playing')
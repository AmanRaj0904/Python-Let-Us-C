userGuessNo= int(input("Enter the Number to Guess\n"))
Attemts=0
while True:
    userInput= int(input("Enter The No to Match \n"))
    if userInput == userGuessNo:
        print("Hurray !! No Is Matched\n")
        break
    else:
        print("Not Matched")
        Attemts=Attemts+1
        

print("Total Attemts Taken to Complete the game is \n",Attemts)



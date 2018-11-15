import random
money = float(input("How many dollars do you have? "))
highestAmount = money
roll = 0
highestRoll = 0
while money >=0:
    if money == 0:
        print("You are broke after", roll, "rolls.\nYou should have quit after", highestRoll, "rolls when you had $" + str(highestAmount))
        break
    elif money > 0:
        decision = input("Press 1 to roll, or 0 if you are a quitter: ")
        if decision == "1":
            roll += 1
            diceOne = random.randint(1,6)
            diceTwo = random.randint(1,6)
            diceAmount = diceOne + diceTwo
            if diceAmount == 7:
                money += 4
                print("Congrats! You rolled", diceAmount, "You now have $" + str(money))
                if money > highestAmount:
                    highestAmount = money
                    highestRoll = roll
                    print("Good job! You just hit your highest amount!")
            elif diceAmount != 7:
                money -= 1
                print("So sad, you rolled", diceAmount, "You now have $" + str(money))
        elif decision == "0":
            print("I knew you didn't have the guts! Take your $" + str(money) + " and get out of here!")
            break
        else:
            decision = input("That was not one of your choices.\nPress 1 to roll, or 0 if you are a quitter: ")
    else:
        print("The casino has gone bankrupt, we will not be giving your money back.")

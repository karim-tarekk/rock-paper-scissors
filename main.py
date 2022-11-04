import random

if __name__ == '__main__':
    words = ["rock", "paper", "scissor"]
    user_score, computer_score = 0, 0
    while True:
        rand_num = random.randint(0, 2)
        computer_pick = words[rand_num]
        user_pick = input("Choose from rock/paper/scissor OR Q to end: ")
        if user_pick.lower() in words and user_pick.lower() != 'q':
            if user_pick.lower() == "rock" and computer_pick.lower() == "scissor":
                user_score += 1
                print("Computer chose (", computer_pick, "), YOU WON THIS ROUND!")
            elif user_pick.lower() == "paper" and computer_pick.lower() == "rock":
                user_score += 1
                print("Computer chose (", computer_pick, "), YOU WON THIS ROUND!")
            elif user_pick.lower() == "scissor" and computer_pick.lower() == "paper":
                user_score += 1
                print("Computer chose (", computer_pick, ",) YOU WON THIS ROUND!")
            elif user_pick.lower() == computer_pick.lower():
                print("Computer chose (", computer_pick, "), NOBODY WON THIS ROUND!")
            else:
                computer_score += 1
                print("Computer chose (", computer_pick, "), YOU LOST THIS ROUND!")
        else:
            if computer_score > user_score:
                print("Your Score is (", user_score, ")")
                print("Computer's Score is (", computer_score, ")")
                print("COMPUTER WON THIS GAME, HARD LUCK!!!")
            elif user_score > computer_score:
                print("Your Score is (", user_score, ")")
                print("Computer's Score is (", computer_score, ")")
                print("YOU WON THIS GAME, CONGRATULATIONS!!!")
            else:
                print("Game ended in a TIE, NOBODY WON!")
            user_new = input("Type R if you want to start a new game or Q to exit: ")
            if user_new.lower() == 'r':
                user_score, computer_score = 0, 0
                continue
            else:
                print("exiting the program")
                print(quit())




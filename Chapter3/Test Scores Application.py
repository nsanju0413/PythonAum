print("The Test Scores application\n")
print("Enter 3 test scores")
print("========================")

while True:
    score1 = int(input("Enter the score:\t"))
    if score1 < 0 or score1 > 100:
        print("Score can't be less than zero or greater than 100")
    else:
        break

while True:
    score2 = int(input("Enter the score:\t"))
    if score2 < 0 or score2 > 100:  # Fixed the condition (changed score1 to score2)
        print("Score can't be less than zero or greater than 100")
    else:
        break

while True:
    score3 = int(input("Enter the score:\t"))
    if score3 < 0 or score3 > 100:  # Fixed the condition (changed score1 to score3)
        print("Score can't be less than zero or greater than 100")
    else:
        break

print("========================")

total_score = score1 + score2 + score3
average = total_score / 3

print("Your Scores:\t", score1, " ", score2, " ", score3)
print("Total Score:\t", total_score)
print("Average Score:\t", round(average))
print("\nBye")

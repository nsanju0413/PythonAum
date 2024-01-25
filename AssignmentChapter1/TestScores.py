print("The Test Scores Application\n")

print("Enter 3 Test Scores")
print("====================")

subject1=int(input("Enter the test score:\t"))
subject2=int(input("Enter the test score:\t"))
subject3=int(input("Enter the test score:\t"))
print("====================")
print("Your Scores: "+str(subject1)+" "+str(subject2)+" "+str(subject3))
total=subject1+subject2+subject3
print("Total Score: "+str(total))

average=int(total/3)
print("Average Score: "+str(average))

print("\nBye!")
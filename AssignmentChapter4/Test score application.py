def test_score_application():
    print('The Test Score Application')
    print('Enter test scores\nEnter \'x\' to end input\n====================== ')
    test_scores = []

    user_input = 'a'
    while user_input != 'x':
        user_input = input("Enter test score (or 'x' to quit): ")
        if user_input != 'x' and user_input.isalpha() == False:
            score = int(user_input)
            if 0 < score <= 100:
                test_scores.append(score)
            else:
                print('Enter a valid number between 1 and 100')
        elif user_input != 'x' and user_input.isalpha() == True:
            print('Enter a valid number')

    total_score = sum(test_scores)
    average_score = int(total_score / len(test_scores))
    print('Total Score:', total_score)
    print('Average Score:', average_score)

test_score_application()
print('Bye')

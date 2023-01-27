import os

greetings = " **************************** WELCOME TO U&ME **************************** "
about = "\nYour partner will write 3 specific questions and the right answer about him/her and you'll have to answer objectively"
rules = ' \n1. Your partner write 3 questions and the respective answers. \
          \n2. You answer these 3 questions \
          \n3. You gain 1 point for a correct answer \
          \n4. There is 3 rounds for each individual \n'

print(greetings)
print(about)
print(rules)

def questions_maker():
    questions = []
    counter = 0
    print(f'Write 3 questions for your partner:')
    for question in range(3):
        print('\n')
        print(f'Question {counter + 1} of 3')
        questions.append(input())
        counter += 1
    return questions


def answer_maker(questions):
    answers = []
    print('\n')
    print(f'Write the answers for the questions you\'ve made for you partner:')
    for question in questions:
        print('\n')
        print(f'{question}?: ')
        answers.append(input())
    return answers


def questions_and_answers():
    questions = questions_maker()
    answers = answer_maker(questions)
    questions_answers = {key: value for key, value in zip(questions, answers)}
    return questions_answers


def game():
    qa = questions_and_answers()
    points = 0

    os.system('clear')

    print('\n')
    print(f'Answer the questions your partner made:\n')

    for question in qa.keys():
        print(question, ':')
        a = input()
        answer = qa[question]
        if a == answer:
            print('You answer was correct! +1 point')
            print('\n')
            points += 1
        else:
            print('You answer was incorrect! 0 point')
            print('\n')

    return print(f'Total points: {points}')


if __name__ == "__main__":
    game()


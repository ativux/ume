import os

def greetings_and_instructions():
    art_ume = ''' 
                uu      u    &&& &          mmm             m m    eeeeeeeeeeee
                uu      u    &&             mm  m         m   m    eee
                uu      u     &&       &    mm    m     m     m    eeeeeeeeeeee
                uu      u    &&& &   &      mm      mmm       m    eeeeeeeeeeee
                uu      u   &&     &        mm                m    eee
                 uuu u u    &&& & & & &     mm                m    eeeeeeeeeeee
                  uuuuu       &&&&&                mmmmm               eeeee '''
    about = "\n                 Welcome to the U&ME terminal game. \n                 Here comes the instructions:\n                 Your partner will write 3 specific questions about anything and you'll have to answer."
    rules = '\n1. Your partner write 3 questions and the respective answers. \
            \n2. You have to answer these 3 questions. \
            \n3. You gain 1 point for a correct answer. \n'

    print(art_ume)
    print(about)
    print('\n')
    print('** RULES **')
    print(rules)

def questions_maker():
    questions = []
    counter = 0
    print(f'Write 3 questions for your partner:')
    for question in range(3):
        print('\n')
        print(f'Question {counter + 1} of 3')
        questions.append(input().title())
        counter += 1
    return questions


def answer_maker(questions):
    answers = []
    print('\n')
    print(f'Write the answers for the questions you\'ve made for you partner:')
    for question in questions:
        print('\n')
        print(f'{question}?: ')
        answers.append(input().title())
    return answers


def questions_and_answers():
    questions = questions_maker()
    answers = answer_maker(questions)
    questions_answers = {key: value for key, value in zip(questions, answers)}
    return questions_answers


def game():

    greetings_and_instructions()
    qa = questions_and_answers()

    points = 0

    os.system('clear')

    print('\n')
    print(f'Answer the questions your partner made:\n')

    for question in qa.keys():
        print(question, ':')
        a = input().title()
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


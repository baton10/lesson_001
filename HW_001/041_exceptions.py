while True:

    user_say = input('Как дела? ')
    if user_say == 'Хорошо':
        print('Хорошо, что хорошо...')
        break
    else:
        print(f'Хорошо, что {user_say}, но все-таки, как дела?')

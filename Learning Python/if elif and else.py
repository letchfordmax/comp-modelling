while True:
    user_input: str = input('You: ') # if will only work with exact matches

    if user_input == 'hello':
        print('Bot: Hello!')
    elif user_input == 'how are you?':
        print('Bot: Good, how about you?')
    elif user_input == 'bye':
        print('Bot: Bye!')
    else:
        print('Bot: Sorry, I did not understand that.')
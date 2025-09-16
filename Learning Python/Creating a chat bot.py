bot_name: str = 'Bob'
print(f'Hello! I\'m {bot_name}! How can I assist you today?')

while True:
    user_input: str = input('You: ').lower()

    if user_input in ['hi', 'hello', 'hey']:
        print(f'{bot_name}: Hello! How can I help you?')
    elif user_input in ['bye', 'see you']:
        print(f'{bot_name}: Goodbye! Have a great day!')
    elif user_input in ['+', 'add', 'sum' , 'i want to add']:
        print(f'{bot_name}: Please provide two numbers to add.')
        try:
            num1: float = float(input('First number: '))
            num2: float = float(input('Second number: '))
            print(f'{bot_name}: The sum is {num1 + num2}')
        except ValueError:
            print(f'{bot_name}: Please enter valid numbers.')
    else:
        print(f'{bot_name}: I\'m sorry, I don\'t understand that. Please try again.')
def greet(name: str, greeting: str = 'Hi') -> None:
    # placing the = in line 1 after the string made it so that we didnt have to worry about defining greeting for every person.
    print(f'{greeting}, {name}!')


greet(name='Alice', greeting='Hello')
greet(name='Bob')




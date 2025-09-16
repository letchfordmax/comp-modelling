a, b = 10, 'fifteen'

try:
    print(a + b)
except TypeError as e:
    print('please enter a number in the form of an integer or a float!')
# you can add multiple except blocks
except Exception as e: # use Exception as a last resort, as it absorbs all errors
    print('Something else went wrong...')



print('Continuing with the program...')
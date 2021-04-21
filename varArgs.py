def foo(first, second, third, *therest):
    print(f'First: {first}')
    print(f'Second: {second}')
    print(f'Third: {third}')
    print(f'And all the rest... {list(therest)}')
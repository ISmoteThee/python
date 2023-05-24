# fill in this function
def fib():
    #pass #this is a null statement which does nothing when executed, useful as a placeholder.
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a+b
# testing code

if __name__ == "__main__":
    import types
    if type(fib()) == types.GeneratorType:
        print("Good, The fib function is a generator.")

        counter = 0
        for n in fib():
            print(n)
            counter += 1
            if counter == 20:
                break
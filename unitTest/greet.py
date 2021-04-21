from do_twice import do_twice

@do_twice
def greet(name):
    print(f"Hello {name}")

greet('world')

import sys
def linux_interaction():
    assert ('linux' in sys.platform), "Function can only run on Linux systems."
    print('Doing something.')

if __name__ == '__main__':
    try:
        linux_interaction()
    except:
        print('Not doing something.')
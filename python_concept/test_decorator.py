
def setup():
    print("Calling setup")

def tearDown():
    print("Calling teardown")


def run_with(func):
    def func_wrapper(*args,**kwargs):
        setup()
        func()
        tearDown()
    return func_wrapper


@run_with
def f1():
    print("I am the main function")

f1()

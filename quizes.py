def a():
    c()
    print("a")
def c():
    b()
    print("c")
def b():
    print("b")
a()
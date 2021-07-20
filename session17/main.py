
from pylog import *

@logger
def verdoppleWert(x):
    return x * 2

print(verdoppleWert(2))

vdw = verdoppleWert
print(vdw(4))


def auessereFunktion():
    def innereFunktion():
        print('innereFunktion')
    innereFunktion()

auessereFunktion()

@logger
def quadriereWert(x):
    return x * x

@logger
def addiereWert(x, y):
    return x + y

def rufeFunktionAuf(func, x):
    print(f"rufe Funktion {func.__name__} auf")
    return func(x)

print(rufeFunktionAuf(quadriereWert, 3))
print(rufeFunktionAuf(verdoppleWert, 3))


# Funktions Referenz als Rückgabewert
def pack(x):
    def func(y):
        return y + x + 2

    return func

p3 = pack(3)
p5 = pack(5)

print(p3(2))
print(p5(2))

@html('html')
@html('body')
@html('h1')
def getUserName():
    return "Hans"

@html('p')
def getAdmin():
    return "root"

#verdoppleWert = logger(verdoppleWert)
verdoppleWert(4)

#quadriereWert = logger(quadriereWert)
quadriereWert(4)

addiereWert(x=40, y=2)



print(getUserName())
print(getAdmin())
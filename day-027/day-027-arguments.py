## Unlimited Arguments (*args), critical part is *
## Practice to add all arguments

def add(*args):
    sum = 0
    for n in args:
        sum += n
    return sum

print(add(6, -2, 7, 3, 4.5))

## Many keyworded arguments (**kwargs)

def calculate(n, **kwargs):
    #print(type(kwargs))
    #for key, value in kwargs.items():
    #    print(f"{key}: {value}")

    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)


calculate(2, add=3, multiply=5)

class Car:

    def __init__(self, **kw):
        self.make = kw.get("make") ## use get method instead of kw['Make'] to avoid key errors
        self.model = kw.get("model")
        self.color = kw.get("color")
        self.seats = kw.get("seats")

my_car = Car(make='Nissan', model='GT-R')
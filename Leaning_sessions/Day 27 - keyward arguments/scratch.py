def simple_function():
    print("Simple Function")


simple_function()


#################################
def key_function(a):
    print(a)


key_function("keyfunction")


################################


def default_value(a=1, b=2, c=3):
    print(f"a:{a}, b:{b}, c:{c}")


default_value(b=14, c=77)

#################################

# *args
def args(*args):
    print(type(args))

args(77,99,22, "Hello")


def args_number(*args):
    total = 0
    for num in args:
        total += num
    return total

print(args_number(88, 4 , 43, 33))

#### keyward

def myFun(arg, *args):
    print(f"First args :{arg}")
    for i in args:
        print(f"This is *args:", i)


myFun(99, "Sushant", "Jadhav", "Rudra", "Ashvini")

### Keyword argument will accept the key and value.

def newFun(**kwargs):
    for k, value in kwargs.items():
        # print("%s == %s" % (k, value))
        print(f"{k} == {value}")


newFun(name="Sushant", lastName= "Jadhav", Hometown= "Jaysingpur")
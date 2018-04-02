def greeting(name, age =0):
    return 'Hello {}. You are {} years. old'.format(name, age)

print(greeting(age ='Chris', name = 22))# keyword arguments - a key and a value (*kwargs)

print(greeting('Chris', 22)) # arguments (*args)

#* and ** is important part, name can change from args and kwargs
# def add_numbers(*args, ** kwargs)

def add_numbers(*args):
    print(args[4:6])


def add_numbers(*args):
    return sum(args)

def add_numbers(*args):
    print(args[100])
    total = 0
    for i in args:
        if isinstance(i, int):
            total += 1
        else:
            raise ValueError('Must be int')
    return total

add_numbers(1, 'a', 3, 4, 5, 6, 7, 8)

#kwargs

def contacts(**kwargs):
    if 'name' in kwargs:
        print(kwargs['name'])# will come through as strings
    print(kwargs)


contacts(age=35, name='chris', phone=8675309)

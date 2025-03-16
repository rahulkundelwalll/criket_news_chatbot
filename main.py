def debug(func):
    def wrapper(*args, **kwargs):
        print(f'Calling {func.__name__} with args: {args}, kwargs: {kwargs}')
        return func(*args, **kwargs)
    return wrapper

@debug
def add(a, b):
    return a + b

print(add(1, 2))
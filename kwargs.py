def person(**kwargs):
    for key, value in kwargs.items():
        print(f"{key.capitalize()}: {value}")

person(name="Sam", age = 30, city="Kathmandu")


# Another *args example
def print_arguments(*args):
    for arg in args:
        print(arg)

print_arguments("Hello", "World", 42, True)
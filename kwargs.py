def person(**kwargs):
    for key, value in kwargs.items():
        print(f"{key.capitalize()}: {value}")

person(name="Sam", age = 30, city="Kathmandu")

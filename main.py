def to_upper(name):
    return name.upper()

def say_hello(name):
    print(f"Hello, {name}")

if __name__=='__main__':
    name="Aditya"
    say_hello(name)
    print(to_upper(name))
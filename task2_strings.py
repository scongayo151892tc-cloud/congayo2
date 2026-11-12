"""Task 2: Strings, escape sequences, f-strings, string methods  (lessons 1.3 to 1.6)

Complete each function. Keep the function names and parameters.
Run the checks with:  python -m unittest tests.test_tasks.Task2Strings -v
"""


def greet(name):
    return  f"Hello, {name}!"


def clean(text):
    return  text.strip().title()


def shout(text):
    return  text.upper() + "!"


def dialogue(speaker, line):
    return  speaker + 'says: "' + line + '"'


def receipt():
    return "Item\tPrice\nPen\t10"


def initials(full_name):
    words = full_name.split()
    result = ""

    for word in words:
        result = result + word[0].upper()

    return result


if __name__ == "__main__":
    print(greet("Ana"))
    print(clean(" Sanmuel Jan C. Congayo "))
    print(shout("hey"))
    print(dialogue("Maria", "Hi"))
    print(receipt())
    print(initials("Sanmuel Jan C. Congayo"))

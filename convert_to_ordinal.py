import inflect

def num2ord(number):
    p = inflect.engine()
    ordinal = p.ordinal(number)
    return ordinal

if __name__ == "__main__":
    num = int(input("Enter: "))
    ord = num2ord(num)
    print(ord)
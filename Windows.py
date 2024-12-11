
def pythagorean_theorem(a, b):

    c = (a**2 + b**2)**0.5
    return c


a = float(input("Length first leg: "))
b = float(input("Length second leg: "))

hypotenuse = pythagorean_theorem(a, b)

print(f"The length of the hypotenuse is: {hypotenuse}")

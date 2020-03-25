from math import pi



while True:
    R = input("please input radius:")
    radius = float(R)
    print(R)
    area = pi*radius*radius
    print(area)
    S=int(input("Do you want to continue? Type 1 for yes or 2 for no:"))

    print(S)

    if S == 1:
        continue
    elif S == 2:
        break
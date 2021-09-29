# Author JRI 9/29/21

x = input("How many points did the team have? ")

if int(x) >= 15:
    print("gold medal")
else:
    if int(x) >= 12:
        print("silver medal")
    else:
        if int(x) >= 9:
            print("bronze medal")
        else:
            print("no medal")

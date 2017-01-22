from dt import roadMap
def main():
    mapA = roadMap()
    if mapA.Matrix[0][0].hasCar():
        print("True")
    else:
        print("False")
main()

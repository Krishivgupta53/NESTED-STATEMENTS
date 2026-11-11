print("--------------------")
print("welcome to ride builder")
print("--------------------")
print("")
print("1-:bike")
print("2-:car")
CHOICE=int(input("enter the vehicle type choose 1 or 2"))
if CHOICE==1:
    print("you chose bike  choose the bike type")
    print("1-:scooty")
    print("2-:mountain bike")
    bike_type=int(input("enter bike type choose 1 or 2"))
    if bike_type==1:
        print("you chosen scooty")
        print("top_speed=120")
        print("best for city purpoces")
    else:
        print("you have chosen mountein bikes ")
        print("top_speed=80")
        print("best for moutain climbing")
elif CHOICE==2:
    print(" you have chosen car choose the car type")
    print("1-:sedan")
    print("2-:SUV")
    car_type=int(input("enter 1 or 2 "))
    if car_type==1:
        print("you have chosen sedan")
        print("seats : 5  passengers")
        print("best for family trips")
    else:
        print("you have chosen SUV")
        print("seats : 7 passengers")
        print("best for offroading")
else:
    print("invalid option")
print("")
print("------------------------")
print("your custom ride is ready")
print("enjoy your journy")
print("------------------------")





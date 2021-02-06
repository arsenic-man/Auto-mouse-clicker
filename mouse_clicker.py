from time import sleep
import pyautogui

list1 = []
list2 = []


def click(num):
    input("You can't do anything during the clicking ")
    input("You have 10 seconds to open the application you want to start clicking after press Enter button ")
    for i in range(0, num):
        for j in list2:
            print("Mouse 'X' position is '", str(j[0]), "' and mouse 'y' position is '", str(j[1]),
                  "' with '", str(j[2]), "' second(s) delay clicked !")
            pyautogui.click(int(j[0]), int(j[1]))
            sleep(float(j[2]))

    print("FINNISH !!!")


def get():
    a = input("Do you want to add new position (y/n) ? ")

    if a == "y":
        add_position()
    elif a == "n":
        num = int(input("Enter the number of repeation : "))
        click(num)
    else:
        get()


def add_position():
    global list2
    input("You have 10 seconds to move your mouse to the right position to get that after press Enter button ")

    for i in range(10, 0, -1):
        print(i)
        sleep(1)

    print("Done !")

    currentMouseX, currentMouseY = pyautogui.position()

    delay = input("Enter the delay between this click in seconds : ")

    list1 = [currentMouseX, currentMouseY, delay]

    print("Mouse 'X' position is ", str(currentMouseX), " and mouse 'y' position is ", str(currentMouseY), "with",
          str(delay), "second(s) delay successfully added !!!")

    list2.append(list1)

    get()


add_position()

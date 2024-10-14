#jump search,selection sort and strand sort

import random
import math
def list_numbers(list,n):
    for i in range(n):
        list.append(random.randint(0,1000))
    print("Your list:",list)
def menu():
    print("This is your menu")
    print("1.Generate a random list of n numbers")
    print("2.Search using the Jump search algorithm ")
    print("3.Sort using the Selection sort algorithm")
    print("4.Sort using the Strand sort algorithm")
    print("5.Exit the program")

def search(list,x,n):
    step=int(math.sqrt(n))
    prev=0
    if list[n-1]<x:
        print("Sorry,the list doesn't have the number you are looking for")
    elif list[0]>x:
        print("Sorry,the list doesn't have the number you are looking for")
    else:
        while list[min(step, n) - 1] < x:
            prev=step
            step=step+int(math.sqrt(n))
            if step>=n:
                print ("Sorry,the list doesn't have the number you are looking for")

        for i in range (prev,min(step,n)):
            if list[i]==x:
                print("The number",x,"is found at the position",i,"in the list")


def selection_sort(list,n,ns): #ns=number of steps shown
    count=0
    for step in range(n):
        mini= step
        for i in range(step + 1, n):
            if list[i] < list[mini]:
                mini = i
        (list[step], list[mini]) = (list[mini], list[step]) #How to Swap the elements -> list[pos1],list[pos2] =list[pos2],list[pos1]
        count=count+1
        if(count%ns==0):
            print("Your list at step: ",count," is ",list)
    print("YOUR FINAL LIST IS: ",list)

def start():
    sorted=False
    list_created=False
    while True:
        menu()
        command = input("Your choice: ")
        if command == "1":
            list=[]
            n=int(input("Enter how many random numbers the list will have: "))
            list_numbers(list,n)
            list_created=True
            sorted=False
        elif command == "2":
            if list_created==False:
                print("Sorry,you can't search without a list.")
            elif list_created==True and sorted==False:
                print("Sorry,you have to sort the list first,please choose 3 or 4")
            else:
                x=int(input("Enter the number you are looking for: "))
                search(list,x,n)
        elif command == "3":
            if list_created==False:
                print("Sorry,you can't sort without a list.You have to choose the first option before this one")
            elif sorted == True:
                print("Sorry,the list has already been sorted.Please generate a new one by choosing the first option")
            else:
                ns=int(input("Choose an n.Every n steps will be shown: "))
                selection_sort(list,n,ns)
            sorted=True
        elif command == "4":
            if list_created==False:
                print("Sorry,you can't sort without a list.You have to choose the first option before this one")
            elif sorted==True:
                print("Sorry,the list has already been sorted.Please generate a new one by choosing the first option")
            else:
                ns = int(input("Choose an n.Every n steps will be shown: "))
            sorted=True
        elif command == "5":
            print("You chose to exit the menu.Goodbye!")
            break
        else:
            print("Please choose a valid option")
start()
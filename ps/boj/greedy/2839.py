input = int(input())
bagType = [5, 3]
result = 0
isDone = False

if input <= bagType[0]:
    if input == 5 or input == 3:
        print(1)
        isDone = True
    else:
        result = -1
        print(-1)
        isDone = True
else:
    if input % bagType[0] == 0:
        result = input//bagType[0]
        print(result)
        isDone = True
    elif input % bagType[0] == 1:
        if input >= 6:
            result = input//bagType[0] + 1
            print(result)
            isDone = True
    elif input % bagType[0] == 2:
        if input >= 12:
            result = input//bagType[0] + 2
            print(result)
            isDone = True
    elif input % bagType[0] == 3:
        result = input//bagType[0] + 1
        print(result)
        isDone = True
    elif input % bagType[0] == 4:
        if input >= 9:
            result = input//bagType[0] + 2
            print(result)
            isDone = True

if isDone == False:
    print(-1)
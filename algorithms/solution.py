#정공법
def solution1():
    list = [1, 4, 6, 7, 1, 199, 8, 2]
    #list = [1, 2, 3, 4, 5, 6, 7]
    temp = 0

    if sortValidator(list):
        for i in range (len(list)-1):
            for j in range(i+1, len(list)):
                if list[i] >= list[j]:
                    temp = list[j]
                    list[j] = list[i]
                    list[i] = temp
        print("Sorted list")
    else:
        print("List had sorted already.")

    print("result", list)

def sortValidator(inputList):
    flag = False
    for i in range(len(inputList)-1):
        if inputList[i] > inputList[i+1]:
            flag = True
    return flag
    
solution1()


#list.append(0)
#0이면 정렬이 된놈
#1이면 정렬이 안된놈
#[1,2,3,4,5,6,7,0]
#객체지향적으로 해석하면,
#Sort라는 추상화 클래스를 만들어서,
#정렬을 하면 반드시 리스트 -1까지만 정렬하고,
#정렬을 하고 나면 반드시 리스트.length의 값을 0으로 수정한다.

#List 형태를 만들때 Sort 여부를 기록하는 것은 비효율적?
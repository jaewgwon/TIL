
def solution():
    input_text = input()
    dict = {}
    for i in range(len(input_text)):
        dict[input_text[i]] = 0
    for i in range(len(input_text)):
        dict[input_text[i]] = dict[input_text[i]] + 1
    
    print("Answer: ", dict)

solution()


def solution2():
    input_text = input()
    for i in range(1, len(input_text)+1):
        print(input_text[:len(input_text)-i] + "#"*i)

solution2()
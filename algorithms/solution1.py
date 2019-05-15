import operator

genres = ["classic", "jazz", "jazz", "classic", "pop"]
counts = [320, 600, 5, 170, 650]

def solution1():
    
    answer = {}
    for i in range(len(counts)):
        answer[i] = counts[i]
    #https://eslife.tistory.com/915
    answer = sorted(answer.items(), key=operator.itemgetter(1), reverse=True)
    
    #위에까지 하면 튜플 리스트 나오고 걍 튜플 값 뽑아서 출력하면,
    for i in range(len(answer)):
        answer[i] = answer[i][0]

    print(answer)

    #혹은 이걸로 genres를 같이 뽑으려면
    for i in range(len(answer)):
        inner = {}
        #이런식으로 answer[i] 대신 counts list의 값 넣어주면 index 말고 counts를 소팅할 수도 있음
        inner[genres[answer[i]]] = answer[i]
        answer[i] = inner


    print(answer)

solution1()
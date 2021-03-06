'''
삽입정렬
1. 알고리즘의 정석
   2)하나의 문제 여러가지 알고리즘
        (7) 삽입정렬 : 자신의 위치를 찾아 삽입함으로써 정렬을 완성하는 알고리즘
            => 두번째 데이터와 첫번째 데이터의 크기를 비교하여 위치를 정하고
            세번째 데이터와 그 앞 데이터들의 크기를 비교하여 삽입될 인덱스를 찾고 
            해당위치의 데이터들은 뒤로 보내는 것을 반복하여 숫자를 정렬한다.
'''
# 내 답안(못풀었음)
def insertion(lists):
    for i in range(1, 7):
        for chr in lists:
            if lists[i] < chr:
                temp = lists[i]
                lists[i] = chr
                chr = temp  
        i+1
    return lists

print(insertion([4,6,2,8,1,9,3]))


#윤아언니 답
def Insertion(lists):
    temp = 0
    for i in range(1, len(lists)):
        myIdx = i #내가 있어야할 인덱스
        for j in range(i-1, -1, -1):
            if lists[i]<lists[j]:
                myIdx = j
                
        if i != myIdx: #내위치가 바뀌어야할 경우
            temp = lists[i]
            for k in range(i, myIdx-1, -1):
                lists[k] = lists[k-1]
            lists[myIdx] = temp
            
    return lists



# 사이트 어떤 사람 답안인데 좀 이상함
def insertion_sorting(list):
    for i in range(1, len(list)):
        max_index = i

        for j in range(max_index):
            if list[max_index] < list[j]:
                temp = list[j]
                list[j] = list[max_index]
                list[max_index] = temp
    return list


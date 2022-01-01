'''
삽입정렬
1. 알고리즘의 정석
   2)하나의 문제 여러가지 알고리즘
        (7) 삽입정렬 : 자신의 위치를 찾아 삽입함으로써 정렬을 완성하는 알고리즘
            => 두번째 데이터와 첫번째 데이터의 크기를 비교하여 위치를 정하고
            세번째 데이터와 그 앞 데이터들의 크기를 비교하여 삽입될 인덱스를 찾고 
            해당위치의 데이터들은 뒤로 보내는 것을 반복하여 숫자를 정렬한다.
'''

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




# 사이트 답
def insertion_sorting(list):
    for i in range(1, len(list)):
        max_index = i

        for j in range(max_index):
            if list[max_index] < list[j]:
                temp = list[j]
                list[j] = list[max_index]
                list[max_index] = temp
    return list


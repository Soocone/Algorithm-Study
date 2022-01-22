'''
3. 알고리즘 패러다임
   2)Divide and Conquer
        (13) QuickSort 퀵정렬 함수 만들기 (Divide and Conquer 방식)
        quicksort는 파라미터로 리스트 하나와 리스트 내에서 정렬시킬 
        범위를 나타내는 인덱스 start와 인덱스 end를 받습니다.
        
        merge_sort 함수와 달리 quicksort 함수는 정렬된 새로운 리스트를 
        리턴하는 게 아니라, 파라미터로 받는 리스트 자체를 정렬시키는 것
        
        * swap_elements와 partition 함수는 이전 과제에서 작성한 그대로 사용하기!!
'''

# 두 요소의 위치를 바꿔주는 helper function
from operator import index, indexOf


def swap_elements(my_list, index1, index2):
    my_list[index1], my_list[index2] = my_list[index2], my_list[index1]

# 퀵 정렬에서 사용되는 partition 함수
def partition(my_list, start, end):
    pivot = end
    big = start
    
    for i in range(0, len(my_list)-1):
        if my_list[i]<= my_list[pivot]:
            swap_elements(my_list, i, big)
            big += 1
        
    swap_elements(my_list, big, pivot)
    pivot = big
    return pivot

    
# 퀵 정렬 (start, end 파라미터 없이도 호출이 가능하도록 수정해보세요!)
# 해답
def quicksort(my_list, start=0, end=None):
    if end == None:
        end = len(my_list) - 1

    # base case
    if end - start < 1:
        return

    # my_list를 두 부분으로 나누어주고,
    # partition 이후 pivot의 인덱스를 리턴받는다
    pivot = partition(my_list, start, end)

    # pivot의 왼쪽 부분 정렬
    quicksort(my_list, start, pivot - 1)

    # pivot의 오른쪽 부분 정렬
    quicksort(my_list, pivot + 1, end)


# 테스트 1
list1 = [1, 3, 5, 7, 9, 11, 13, 11]
quicksort(list1) # start, end 파라미터 없이 호출
print(list1)

# 테스트 2
list2 = [28, 13, 9, 30, 1, 48, 5, 7, 15]
quicksort(list2) # start, end 파라미터 없이 호출
print(list2)

# 테스트 3
list3 = [2, 5, 6, 7, 1, 2, 4, 7, 10, 11, 4, 15, 13, 1, 6, 4]
quicksort(list3) # start, end 파라미터 없이 호출
print(list3)

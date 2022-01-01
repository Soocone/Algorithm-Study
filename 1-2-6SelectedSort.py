'''
선택정렬
'''

def selected(lists):
    
    for i in range(0, 6):
        for j in range(0, 6-i):
            if lists[j] > lists[j+1]:
                temp = lists[j]
                lists[j] = lists[j+1]
                lists[j+1] = temp
            else: j+1
        i+1
    return lists

print(selected([4,6,2,8,1,9,3]))

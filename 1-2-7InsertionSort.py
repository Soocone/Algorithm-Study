'''
삽입정렬
'''

def insertion(lists):
    for i in range(1, 6):
        for chr in lists:
            if lists[i] < chr:
                temp = lists[i]
                lists[i] = chr
                chr = temp  
        i+1
    return lists

print(insertion([4,6,2,8,1,9,3]))

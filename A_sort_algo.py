'''
This code implements several sort algorithms:
1. Bubble Sort:  https://www.youtube.com/watch?v=xli_FI7CuzA
2. Insertion Sort:  https://www.youtube.com/watch?v=JU767SDMDvA
3. Selection Sort:  https://www.youtube.com/watch?v=g-PGLbMth_g
4. Quick Sort:  https://www.youtube.com/watch?v=Hoixgm4-P4M
5. Merge Sort:  https://www.youtube.com/watch?v=TzeBrDU-JaY

'''


# Bubble Sort
def Bubble_sort(list):
    for i in range(0,len(list)):
        for j in range(i+1, len(list)):
            # if list[i] > list[j]:    # asceding
            if list[i] < list[j]:    # desceding
                t = list[i]
                list[i] = list[j]
                list[j] = t

# Bubble sort2
def Bubble_sort2(list):
    for n in range(len(list)):
        for i in range(len(list)-n-1):
            if list[i] > list[i+1]:
                t = list[i]
                list[i] = list[i+1]
                list[i+1] = t

# Insertion Sort
def Insertion_sort(list):
    for n in range(1,len(list)):
        target = list[n]
        #  [0,n-1] [n,len]
        for m in range(n,0,-1):
            if target < list[m-1]:
                list[m] = list[m-1]
                list[m-1] = target


# Selection Sort
def Selection_sort(list):
    for n in range(0,len(list)-1):
        cur_min = list[n]
        cur_index = n
        for m in range(n,len(list)):
            if list[m] < cur_min:
                cur_min = list[m]
                cur_index = m
        if n != cur_index:
            t = list[n]
            list[n] = list[cur_index]
            list[cur_index] = t


# Quick Sort: Set the last element as pivot
def Partition(input_list, low, high):
    i = low -1
    pivot = input_list[high]
    for j in range(low, high):
        if input_list[j] <= pivot:
            i = i+1
            t = input_list[i]
            input_list[i] = input_list[j]
            input_list[j] = t
    y = input_list[i+1]
    input_list[i+1] = input_list[high]
    input_list[high] = y

    return i+1

def QuickSort(input_list, low, high):
    if low < high:
        p = Partition(input_list, low, high)
        QuickSort(input_list, low, p-1)
        QuickSort(input_list, p+1, high)


# merge sort
def Merge(left_list, right_list, list):
    nL = len(left_list)
    nR = len(right_list)
    i = 0
    j = 0
    n = 0
    while i < nL and j < nR:
        if left_list[i] < right_list[j]:
            list[n] = left_list[i]
            n = n+1
            i = i+1
        else:
            list[n] = right_list[j]
            n = n+1
            j = j+1

    if i < nL:
        for q in range(i, nL):
            list[n] = left_list[q]
            n = n+1
    if j < nR:
        for p in range(j, nR):
            list[n] = right_list[p]
            n = n + 1

def Merge_sort(list):
    n = len(list)
    if n < 2:
        return
    mid = int(n/2)
    left_list = []
    right_list = []
    for i in range(0, mid):
        left_list.append(int(list[i]))
    for j in range(mid, n):
        right_list.append(int(list[j]))
    Merge_sort(left_list)
    Merge_sort(right_list)
    Merge(left_list, right_list, list)



input_list = [19,2,31,45,6,11,121,27]
# Bubble_sort2(input_list)
# Insertion_sort(input_list)
# Selection_sort(input_list)
# low = 0
# high = len(input_list) - 1
# QuickSort(input_list, low, high)
Merge_sort(input_list)


print(input_list)
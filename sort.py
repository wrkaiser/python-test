

def bubble_sort(unsort_array):
    # 从上往下冒，大的沉到最底部
    for i in range(1, len(unsort_array)):
        for j in range(0, len(unsort_array)-i):
            if unsort_array[j] > unsort_array[j+1]:
                # temp = unsort_array[j + 1]
                # unsort_array[j + 1] = unsort_array[j]
                # unsort_array[j] = temp
                unsort_array[j], unsort_array[j + 1] = unsort_array[j + 1], unsort_array[j]
    return unsort_array

unsort_array_1 = [5,2,1,6,3,12,2]
print(bubble_sort(unsort_array_1))
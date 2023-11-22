import random
from Python.TestTime import test_time


@test_time
def sort(array: list) -> list:
    for i in range(1, array.__len__()):
        j = i
        while (j > 0) and (array[j] < array[j-1]):
            temp = array[j]
            array[j] = array[j-1]
            array[j-1] = temp
            j -= 1
    return array


@test_time
def ins_sort(aray):
    len_list = aray.__len__()
    for i in range(1, len_list):
        ref_value = aray[i]
        x = i
        while x>0 and aray[x-1] > ref_value:
            aray[x] = aray[x-1]
            x -= 1
        else:
            aray[x] = ref_value
    return aray


test_array = [random.randint(1,1000) for i in range(100)]
test_array_2 = [random.randint(1,1000) for i in range(100)]
print(sort(test_array))
print(ins_sort(test_array_2))

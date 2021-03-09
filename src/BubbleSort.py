def bubble_sort(array):
    array_size = len(array)
    for i in range(array_size):
        for j in range(i+1, array_size):
            if array[i] > array[j]:
                array[i], array[j] = array[j], array[i]
    return array


# The tests shows that this "naive" implementation is 2 times faster that the other one
# (at least with smalls arrays)
def bubble_sort_not_so_naive_implementation(array):
    while not array_is_ordered(array):
        bubble_first_value(array)

    return array


def array_is_ordered(array):
    for index, value in enumerate(array):
        if need_switch_with_next_value(index, array):
            return False
    return True


def bubble_first_value(array):
    for index, value in enumerate(array):
        if need_switch_with_next_value(index, array):
            switch_current_and_next_value(index, array)


def need_switch_with_next_value(index, array):
    return (index+1 < len(array)) and (array[index] > array[index+1])


def switch_current_and_next_value(index, array):
    (array[index], array[index+1]) = (array[index+1], array[index])


def bubble_sort(array):
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

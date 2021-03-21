
def task(array):
    list_from_array = list(array)
    count = 0
    for number in list_from_array:
        if number == '1':
            count += 1
        else:
            break
    return count

print(task("111111111111111111111111100000000"))
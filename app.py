# function that takes list & target
# variables (middle, start, end, steps)
# recursion or while loop
# increase steps each time a split is done
# conditions to track target position

def binary_search(list, target):
    middle = 0
    start = 0
    end = len(list)
    steps = 0

    while (start <= end):
        print("step", steps, ":", str(list[start:end+1]))

        steps = steps + 1
        middle = (start + end) // 2

        if (target == list[middle]):
            return middle
        elif (int(target) < int(list[middle])):
            end = middle - 1
        else:
            start = middle + 1
    return -1

my_list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

target = input("Enter a number between " + str(my_list[0]) + " and " + str(len(my_list)) + ": ")

binary_search(my_list, target)
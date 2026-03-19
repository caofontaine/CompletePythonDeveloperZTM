def highest_even(li):
    li.sort()
    list_index = len(li) - 1
    
    while list_index > 0:
        if li[list_index] % 2 == 0:
            return f"{li[list_index]} is the highest even number."
        list_index = list_index - 1

print(highest_even([10,2,3,4,8,11]))

# Solution
def highest_even(li):
    evens = []
    for item in li:
        if not item % 2 and item not in evens:
            evens.append(item)
    return max(evens)


print(highest_even([10, 2, 3, 4, 8, 11]))
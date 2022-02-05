array = [15, 6, 12, 56, 109, 81, 3]

for item in range(len(array)-1):
    selected_number = array[item]
    lowest_number = array[item+1]

    for number in range(item+1,len(array)):
        compared_number = array[number]
        if lowest_number > compared_number:
            lowest_number = compared_number
        
    if lowest_number < selected_number:
        lowest_number, selected_number == selected_number, lowest_number
        array[item] = lowest_number
        array[number] = selected_number


    

print(array)
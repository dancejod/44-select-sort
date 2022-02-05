array = [36,51,11,2,72,16,100]

for item in range(len(array)-1):
    selected_number = array[item]
    lowest_number = array[item+1]
    lowest_number_id = array.index(lowest_number)

    for number in range(item+1,len(array)):
        compared_number = array[number]
        if lowest_number > compared_number:
            lowest_number = compared_number
            lowest_number_id = array.index(lowest_number)
        
    if lowest_number < selected_number:
        lowest_number, selected_number == selected_number, lowest_number
        array[item] = lowest_number
        array[lowest_number_id] = selected_number


    

print(array)
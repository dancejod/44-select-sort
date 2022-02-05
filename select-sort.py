# Array, ktory chceme zoradit pomocou Selection Sort
sample_array = [32, 1, 156, 4, 81, 52, 100]

for index in range(len(sample_array)-1):
    # Zvoli sa prvok v zozname a prvok po nom, ktory sa porovnava so zvyskom array v dalsom cykle
    selected_number = sample_array[index]
    lowest_number = sample_array[index+1]
    lowest_number_id = index+1     

    for number in range(index+1,len(sample_array)):
        # Postupne zmensovanie rozsahu zoznamu, hladanie najmensieho cisla v zvysku zoznamu
        compared_number = sample_array[number]
        if lowest_number > compared_number:
            lowest_number = compared_number
            lowest_number_id = number
        
    if lowest_number < selected_number:
        # Prehodenie najmensieho cisla s prave zvolenym cislom v zozname podla indexov
        sample_array[index] = lowest_number
        sample_array[lowest_number_id] = selected_number

# Zoradeny array
print(sample_array)
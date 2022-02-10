import csv

# An empty list for numbers in the input file
sample_array = []
infilename = "random_numbers.csv"
outfilename = "sorted_numbers.csv"

# Input file validation
try:
    with open(infilename, encoding="utf-8", newline = "") as input:
        for row in csv.reader(input):
            sample_array.append(float(row[0]))

except IOError:
    print(f"File {infilename} does not exist. Check if the file is in the same directory as the script.")
    raise

except ValueError:
    print("File contains invalid (nonnumerical) characters. Repair the file and run the script again.")
    raise

except IndexError:
    print("File contains empty lines. Repair the file and run the script again.")
    raise

except:
    print("Something went wrong, the script will now terminate.")
    raise

# Print the list of input file numbers 
print("Input list: ", sample_array)

# Selection sort algorithm
for index in range(len(sample_array)-1):
    
    # Select the first element and scan the whole list sequentially,
    # store value and index of the next element
    selected_number = sample_array[index]
    lowest_number = sample_array[index+1]
    lowest_number_id = index+1     

    for number in range(index+1,len(sample_array)):
        
        # Scan each element that goes after currently selected element,
        # compare them and find and store the lowest value and its index
        compared_number = sample_array[number]
        if lowest_number > compared_number:
            lowest_number = compared_number
            lowest_number_id = number
        
    if lowest_number < selected_number:
        
        # Swap the lowest value with currently selected element,
        # then start over by selecting the next unsorted element
        sample_array[index] = lowest_number
        sample_array[lowest_number_id] = selected_number

# Export the sorted list to a new file
with open(outfilename, "w",encoding="utf-8",  newline = "") as output:
    writer = csv.writer(output)
    for sorted_number in sample_array:
        writer.writerow([sorted_number])

# Print the sorted list
print("\nSorted list: ", sample_array)
print(f"\nThe sorted list has been exported to a new file: {outfilename}" )
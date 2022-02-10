import csv

# An empty list for numbers in the input file
input_array = []

# Set the name of the input and output file. This is the default setting.
infilename = "random_numbers.csv"
outfilename = "sorted_numbers.csv"

def selection_sort(sample_array):
    '''
    Selection sort algorithm, takes an array of numbers,
    returns sorted array in ascending order.

    Parameters:
        sample_array(list): Input list of numbers.
    
    Returns:
        sorted(list): Sorted list of numbers.
    '''
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
        
    sorted = sample_array
    return sorted


def export_array(array):
    '''
    Export the sorted list to a new file.

    Parameters:
        array(list): Sorted list of numbers.
    '''
    with open(outfilename, "w",encoding="utf-8",  newline = "") as output:
        writer = csv.writer(output)
        for sorted_number in array:
            writer.writerow([sorted_number])

# Input file validation
try:
    with open(infilename, encoding="utf-8", newline = "") as input:
        for row in csv.reader(input):
            input_array.append(float(row[0]))

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
print("Input list: ", input_array)

sorted_array = selection_sort(input_array)
export_array(sorted_array)

# Print the sorted list
print("\nSorted list: ", sorted_array)
print(f"\nThe sorted list has been exported to a new file: {outfilename}" )
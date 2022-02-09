import csv

# Prazdny zoznam, do ktoreho sa zo vstupu zavolaju cisla
sample_array = []

# Overovanie vstupu
try:
    with open("random_numbers.csv", encoding="utf-8", newline = "") as input:
        for row in csv.reader(input):
            sample_array.append(float(row[0]))

except IOError:
    print("Subor neexistuje. Skontrolujte jeho nazov a umiestnenie a spustite skript znova.")
    raise

except ValueError:
    print("V subore sa nachadzaju nepovolene znaky. Opravte subor a spustite skript znova.")
    raise

except IndexError:
    print("V subore je chybajuci riadok. Opravte chybu a spustite skript znova.")
    raise

except:
    print("Nieco sa pokazilo, program sa teraz ukonci.")
    raise

# Vypisanie vstupneho zoznamu
print("Vstupny zoznam cisel: ", sample_array)

# Selection sort algoritmus
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

# Vypisanie zoradeneho zoznamu do noveho suboru
with open("sorted_numbers.csv", "w",encoding="utf-8",  newline = "") as output:
    writer = csv.writer(output)
    for sorted_number in sample_array:
        writer.writerow([sorted_number])

# Vypisanie zoradeneho zoznamu
print("Zoradeny zoznam cisel: ", sample_array)
print(f"Zoradeny zoznam bol vyexportovany do noveho suboru.")
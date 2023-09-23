#DATA MUNGING FOR NASA WEATHER DATA
import re

nasa = open('data/nasa_tabledata.txt','r', encoding="utf_8")

lines = nasa.readlines()

#remove text at top & bottom
all_lines = lines[7:166]

nasa_data = []

#remove line breaks and blank rows
for line in all_lines:
    line = line.strip()
    nasa_data.append(line)
    if line == '':
        nasa_data.remove('')

header = nasa_data[0]

# remove repeat header lines
for line in nasa_data:
    if str(line[0]).isalpha():
        nasa_data.remove(line)

# add back in header
nasa_data.insert(0, header)

clean_data = []

# remove random spaces and duplicate year at the end of each line
for line in nasa_data:
    update = re.sub('\s+', ',', line)
    update = update[:-5]
    clean_data.append(update)


# remove 2023 data as the year has not yet finished
clean_data = clean_data[:-1]

new_line = []

# replacing missing 1880 data
for line in clean_data:
    if "****" in line:
        line = line.split(',') #1880 list
        dec_1879_avg = (int(line[1])+int(line[2]))/2
        djf = format(((dec_1879_avg + (int(line[1])+int(line[2]))) / 3),".0f")
        avg_total = 0
        for item in line[1:11]:
            avg_total += int(item)
        d_n = format(((avg_total + dec_1879_avg)/12), ".0f")
        line[14] = str(d_n)
        line[15] = str(djf)
        new_line = ",".join(line)
        clean_data[1] = str(new_line)


# Function to convert Celsius to Fahrenheit
def anomaly_to_fahrenheit(temp):
    return (temp/100)*1.8

# Iterate through clean_data (assuming clean_data is a list of strings)
for index, line in enumerate(clean_data[1:]):  # Skip the header line
    line_parts = line.split(",")  # Split the line into parts
    updated_parts = []  # Create a list to store the updated parts

    # Skip the first element (assuming it's not a temperature)
    for i, part in enumerate(line_parts[1:]):
        temp_celsius = int(part)
        temp_fahrenheit = anomaly_to_fahrenheit(temp_celsius)
        new_format = format(temp_fahrenheit, ".1f")
        updated_parts.append(new_format)

    # Replace the temperature values in the original line with updated values
    line_parts[1:] = updated_parts

    # Reconstruct the line with updated temperature values
    updated_line = ",".join(line_parts)

    # Update the clean_data list with the modified line
    clean_data[index + 1] = updated_line  # Adding 1 to the index to account for skipping the header


with open('clean_data.csv', mode="w", encoding="utf_8") as file:
    # Iterate through your list and manually format and write each element as a row in the CSV file
    for item in clean_data:
        # file.write(f"{item}\n") 
        file.write(item + "\n")
nasa.close()
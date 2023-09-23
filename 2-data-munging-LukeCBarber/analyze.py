#Place code below to do the analysis part of the assignment.
import csv

# Initialize a dictionary reader for the CSV file
with open("clean_data.csv", "r") as file:
    csv_reader = csv.DictReader(file)

    # Initialize an empty list to store the averages
    averages = []

    # Iterate through the rows in the CSV file
    for row in csv_reader:
        # Convert the numeric values to floats and calculate the average
        temp_f = [float(row[key]) for key in row if key != 'Year' and key != 'J-D'and key != 'D-N' and key != 'DJF' and key!= 'MAM' and key!= 'JJA' and key!= 'SON']
        average_temp = sum(temp_f) / len(temp_f)
        averages.append(average_temp)
     # Condition if t


#decades average
print("The average temperature anomaly in degrees Farenheit for each decade since 1880")
a=0
sum=0
avg_clean=0
yr=1880
while a==0:
    for i in averages:
        a+=1
        sum+=i
        
        if a==10:
            yr+=10
            avg_clean = sum/10
            a=0
            formatted_a= format(avg_clean,".2f")
            if yr <2020:
                yr_dec = yr + 9
                print(str(yr)+ '-'+str(yr_dec) + ':'+str(formatted_a))
            else:
                yr_dec = yr + 2
                print(str(yr)+ '-'+str(yr_dec) + ':'+str(formatted_a))

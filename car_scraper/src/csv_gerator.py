import csv
from src.crud import read_properties

def file_genrate ():

    # Define the data
    data = read_properties()

    # Specify the file name
    filename = 'carData.csv'

    # Write to the CSV file
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data)

    print(f"{filename} has been created successfully.")


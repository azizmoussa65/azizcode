import csv
import panda
def calculate_average(file_path, column_name):
    try:
        with open(file_path, mode='r') as file:
            csv_reader = csv.DictReader(file)
            total = 0
            count = 0
            for row in csv_reader:
                if column_name in row:
                    total += float(row[column_name])
                    count += 1
                else:
                    print(f"Column '{column_name}' not found in the CSV file.")
                    return
            
            if count == 0:
                print("No valid entries found in the CSV file.")
                return
            
            average = total / count
            print(f"The average value in column '{column_name}' is {average:.2f}.")
    except FileNotFoundError:
        print("The specified file was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

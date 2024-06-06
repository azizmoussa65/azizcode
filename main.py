import sys
from csv_utils import calculate_average

def main():
    if len(sys.argv) != 3:
        print("Usage: python main.py <file_path> <column_name>")
        return

    file_path = sys.argv[1]
    column_name = sys.argv[2]
    calculate_average(file_path, column_name)

if __name__ == "__main__":
    main()

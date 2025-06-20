import csv
import os

def main():
    input_path = os.path.join('/data', 'sales.csv')
    if not os.path.exists(input_path):
        raise FileNotFoundError(f"{input_path} not found")
    with open(input_path, 'r') as f:
        reader = csv.reader(f)
        total_rows = sum(1 for _ in reader)
    print(f"Processed {total_rows} rows from {input_path}")

if __name__ == '__main__':
    main()

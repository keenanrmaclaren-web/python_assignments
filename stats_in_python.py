
import sys
import math

def load_data(filepath:str, column:int)->tuple[list, int]:
    numbers = []
    total_values = 0

    if column < 0:
        print("Error: Invalid column number.")
        sys.exit()

    with open(filepath, 'r') as infile:
        for line in infile:
            total_values += 1

            try:
                num = line.split("\t")[column]
            except IndexError:
                print("Error: Index is out bounds." )
                sys.exit()

            try:
                num = float(num)

                if not math.isnan(num):
                    numbers.append(num)
            except ValueError:
                continue
            

    if len(numbers) == 0:
        print("Error: No valid numbers found in the specified column.")
        sys.exit()
       
    return numbers, total_values

    pass

def calculate_average(numbers:list)->float:
    return sum(numbers) / len(numbers)
    pass

def get_max_and_min(numbers:list)->tuple[float, float]:
    return max(numbers), min(numbers)
    pass

def calculate_variance(numbers:list)->float:
    x = len(numbers)

    if x == 1:
        return 0.0

    average = calculate_average(numbers)
    squared_diffs = 0

    for i in numbers:
        squared_diffs += (i - average) ** 2

    return squared_diffs / (x - 1)

    pass

def calculate_std_dev(numbers:list)->float:
    return math.sqrt(calculate_variance(numbers))
    pass

def calculate_median(numbers:list)->float:
    numbers = sorted(numbers)
    x = len(numbers)
    middle_num = x // 2

    if x % 2 == 0:
        return(numbers[middle_num - 1] + numbers[middle_num]) / 2
    else:
        return float(numbers[middle_num])
    pass

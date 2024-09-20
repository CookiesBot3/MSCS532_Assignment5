from randomized_quicksort import quick_sort
from quickSort import quickSort
import random
import time
import tracemalloc

# Generate the dataset base on size and the flag.
# size is the size of the array and the values from 1 to size
# Flags are kept to all false by default.
def generate_data(size, random_flag=False, ascending=False, descending=False):
    # Generates Random numbers in the array according to the size
    if random_flag:
        return random.sample(range(1, size + 1), size)
    # Generates ascending numbers in the array according to the size
    if ascending:
        temp = []
        for i in range(size):
            temp.append(i+1)
        return list(temp) # list() is used to decouple the array for a deepcopy
    # Generates descending numbers in the array according to the size
    if descending:
        temp = []
        for i in range(size, 0, -1):
            temp.append(i)
        return list(temp) # list() is used to decouple the array for a deepcopy
    # Generate a list of random array with repeated elements.
    else:
        array_with_repeats = [random.choice(range(1, size+1)) for _ in range(size)]
        return array_with_repeats

def sort_runner(arr, deterministic ,arrayType = 0):
    type = "Randomized quick sort"
    array_data_type = ""

    #flags to determine which data type it is sorting.
    if arrayType == 1:
        array_data_type = "random"
    elif arrayType == 2 :
        array_data_type = "ascending"
    elif arrayType == 3:
        array_data_type = "descending"
    else:
        array_data_type = "random with repeated elements"

    print(array_data_type + " before: ", arr)
    start_time = time.process_time() #start the timer
    if deterministic:
        quickSort(arr)
    else :
        quick_sort(arr)# sort in place
    end_time = time.process_time() #end the timer
    #Print out the proper result
    if deterministic:
        type = "Deterministic quick sort"

    print(type + " time: ", end_time - start_time)

    print(array_data_type + " after sorted: ", arr)
    print('')

def simulate_run(arr_size, sort_type):
    # Generate all the array dataset according to the flag ie. Random, ascending, descending
    array_random = generate_data(arr_size, random_flag=True)
    array_ascending = generate_data(arr_size, ascending=True)
    array_descending = generate_data(arr_size, descending=True)
    array_repeated = generate_data(arr_size)

    # Run the Sorter for each type of the array for merge and quick sort
    sort_runner(array_random, sort_type, arrayType=1)
    sort_runner(array_ascending, sort_type, arrayType=2)
    sort_runner(array_descending, sort_type, arrayType=3)
    sort_runner(array_repeated, sort_type)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    arr_size = 450  # Size of the array and values from 1 to size
    simulate_run(arr_size, 1)
    simulate_run(arr_size, 0)
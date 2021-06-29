import random, timeit, logging
import sys


logging.basicConfig(filename="programLog.logger", format='%(asctime)s %(message)s', filemode='w')

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)


def selectionSort(arr: list):
    # print(arr)
    logger.info("Selection sort started.")
    for i in range(len(arr)):
        min = i
        for j in range(i + 1, len(arr)):
            if arr[min] > arr[j]:
                min = j
        #logger.warning("Values Swapped.")
        arr[i], arr[min] = arr[min], arr[i]
    logger.warning("List is converted to set to remove duplicate values.")
    arr = set(arr)
    logger.warning("Set is converted back to list for further use in program.")
    arr = list(arr)
    logger.info("Returns a sorted list with unique values.")
    return arr


def linearSearch(arr: list, key: int):
    logger.info("Linear search started.")
    for i in arr:
        if i == key:
            logger.info("Got index of the value present in list.")
            return arr.index(i)

    logger.warning("Value not found in the list.")
    return -1


try:
    logger.info("Program timer started.")
    start_time = timeit.default_timer()
    logger.warning("List initialized.")
    array = [0]
    logger.info("List populated with 10000 random values.")
    for i in range(10000):
        array.append(random.randrange(0, 10000))
    logger.info("Sorting function called, list is passed as an argument and result is stored in another list.")
    sortedArray = selectionSort(array)
    #print(sortedArray)
    logger.warning("Input taken from user that is to be searched in list.")
    x = int(input("Enter a number from 0 to 10000: "))
    if x < 0:
        logger.exception("Value enter by user is negative, it must be positive.")
        print("Value enter by user is negative, it must be positive.")
        sys.exit()
    logger.info("Searching function called, list and user input is passed as arguments.")
    output = linearSearch(sortedArray, x)

    if output != -1:
        print(f"\nThe number {x} is at index number {output}")
    else:
        print(f"\nEntered number does not exist in the array")
    logger.info("Program timer stopped.")
    end_time = timeit.default_timer()
    print(f"\nExecution time for this program is {end_time-start_time:.2f}ms")
    #print(f"Execution start time is {start_time}")
    #print(f"Execution end time is {end_time}")

except ValueError:
    logger.error("Entered value is invalid value for int()")
    print("Entered value is invalid value for int()")

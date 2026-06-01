import random

#Selection Sort
def selection_sort(numbers):
    n = len(numbers)
    for i in range(n - 1):
        min_index = i
        #Find the smallest element in the unsorted portion
        for j in range(i + 1, n):
            if numbers[j] < numbers[min_index]:
                #New smallest int found
                min_index = j

        #Swap the smallest element with the current position
        temp = numbers[i]
        numbers[i] = numbers[min_index]
        numbers[min_index] = temp
    return numbers


#Insertion Sort (loops)
def insertion_sort(numbers):
    n = len(numbers)
    for i in range(1, n):
        key = numbers[i]
        j = i - 1
        #shift larger elements to the right
        while j >= 0 and numbers[j] > key:
            numbers[j + 1] = numbers[j]
            j -= 1
        numbers[j + 1] = key
    return numbers


def main():
    # Generate 10 random integers
    numbers = [random.randint(1, 100) for _ in range(10)]
    print("Original list:", numbers)

    # Test Selection Sort
    selection_list = numbers.copy()
    selection_sort(selection_list)
    print("Selection Sort:", selection_list)

    # Test Insertion Sort
    insertion_list = numbers.copy()
    insertion_sort(insertion_list)
    print("Insertion Sort:", insertion_list)


if __name__ == "__main__":
    main()

def main():
    #ignore this, this is too print 10 ints into youre list
    numbers = [random.randint(1, 100) for _ in range(10)]
    print(numbers)

    #make a function that sorts a list in the given way above, in both a for loop and recursive
if __name__ == "__main__":
    main()

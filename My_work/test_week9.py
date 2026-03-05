def least_to_greatest(nums):
    n = len(nums)
    for i in range(n):
        #Find the index of the smallest number in the remaining part
        min_index = i
        for j in range(i + 1, n):
            if nums[j] < nums[min_index]:
                min_index = j
        #Swap the found minimum with the current position
        temp = nums[i]
        nums[i] = nums[min_index]
        nums[min_index] = temp
    return nums

def test_l_t_g():
    test_list = [5, 2, 9, 1, 7]
    expected = [1, 2, 5, 7, 9]

    result = least_to_greatest(test_list)

    if result == expected:
        print("Test passed!")
    else:
        print("Test failed.")


def main():
    #make a function that allows a user to input 10 numbers
        #this function will sort them from least to greatest 
    #answer the commented lines to help you build this function

    #lets break down the code :)
    input_list = []
    inputs_left = 0

    while inputs_left < 10:
        num = int(input(f"Enter the {inputs_left + 1}th number: "))
        input_list.append(num)
        inputs_left += 1

    sorted_list = least_to_greatest(input_list)
    print("Numbers from least to greatest:", sorted_list)


if __name__ == "__main__":
    main()

import random
import os

# The use of 'print()' is for aesthetic purpuse

def _random_even_number_list_generator():

    number_list = [] # Empty list

    lenght = int(input('Insert the desired lenght of the list: '))

    for i in range(lenght):

        number = random.randint(0,100) # Generates a random number between 0 and 100

        number_list.append(number) 

    even_numbers_list = [number for number in number_list if number % 2 == 0] 
    # ↑ appends only the even numbers of the list generated above(ps : i'm in love with list comprehension) 

    return even_numbers_list # Final random even number list  (disordered)


def quicksort_algorithm(number_list):

    if len(number_list) <= 1:

        return number_list # if the lenght of the list is equal to one it means that the number has been sorted

    else:

        pivot = number_list.pop() # pics the last item of the list as our pivot point
        higher_numbers = [] # here goes the numbers higher then pivot
        lower_numbers = [] # here goes the numbers lower or equal to the pivot

        for i in number_list:

            if i > pivot:

                higher_numbers.append(i)
            
            else:

                lower_numbers.append(i)
    
        return quicksort_algorithm(lower_numbers) + [pivot] + quicksort_algorithm(higher_numbers)
        # here we use recursion until our logic breaks ↑


def binary_search(sorted_list,target,low,high):
    """[Binary search]

    Args:
        sorted_list ([LIST]): [a list of numbers alredy sorted]
        target ([INT]): [The number we are looking for]
        low ([INT]): [The lowest number in a list (it starts at 0) and increses by one until we find (or not) the target]
        high ([INT]): [The highest number in a list (it starts at the bottom of the list) and decreses by one until we find (or not) the target]
    """

    found = False


    while low <= high:

        mid = (low + high)//2 #this is our pivot point, the middle of the list


        if target == sorted_list[mid]:

            found = True
            break

        elif target < sorted_list[mid]:

            high = mid - 1 # this makes our 'highest item' closer to the target
        
        elif target > sorted_list[mid]:

            low = mid + 1 # this makes our 'lowes item' closer to the target

    if found:

        print('Your number was found on the list!!')
    
    else: 

        print("Your number wasn't found on the list")


if __name__ == '__main__':

    os.system('cls') # Cleans our console

    target = int(input('Insert the even number to look for(it must be between 0 and 100): ')) # The even number we are looking for
    print() 
    sorted_list = quicksort_algorithm(_random_even_number_list_generator())
    print()

    binary_search(sorted_list,target, 0, len(sorted_list))

    print()

    print('used list: ')
    print('-'*10)
    print()
    print(sorted_list)
    print()

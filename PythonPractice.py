'''
Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

Bonus: Can you do this in one pass?
'''

def AddsToK(list, k):

    results = []
    counter = 1
    
    for i in list:

        for j in list[counter:]:

            if i + j == k:
                results.append([i,j])
        
        counter+=1


    print(results)

'''
Given an array of integers,
return a new array such that each element at index i of the new array
is the product of all the numbers in the original array except the one at i.

For example, if our input was [1, 2, 3, 4, 5], 
the expected output would be [120, 60, 40, 30, 24]. 
If our input was [3, 2, 1], the expected output would be [2, 3, 6].
'''

def ProductsOfArray(list):
    
    result = []

    for i in range(len(list)):

        newIndex = 1
        for j in range(len(list)):
            
            if j != i:
                
                newIndex *= list[j]
        result.append(newIndex)
    
    print(result)

       


        

def main():
    ProductsOfArray([1, 2, 3, 4, 5])

if __name__ == "__main__": 
    main()

'''
Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

Bonus: Can you do this in one pass?
'''

def addsToK(list, k):

    results = []
    counter = 1
    
    for i in list:

        for j in list[counter:]:

            if i + j == k:
                results.append([i,j])
        
        counter+=1


    print(results)

def main():
    addsToK([10, 15, 3, 7], 17)

if __name__ == "__main__": 
    main()

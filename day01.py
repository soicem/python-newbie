'''
lst = [3,2,9,4,5,6]
for i in lst:
    print(i)
    
print()
    
for i in range(0, len(lst)):
    print(lst[i]) # 0,1,2,3,4,5


print()
    
lst2 = [0, 5, 3, 2, 9]
for i in range(0, len(lst2)):
    print(lst2[i])
    
lst2D = [[0,1,2], [3,4,5], [6,7,8], [9,10,11]]

for i in range(0, len(lst2D)):
    for j in range(0, len(lst2D[i])):
        print(lst2D[i][j])

     
    
    
    
    
lst2D2 = [[0,1,2], [3,4,5], [6,7,8], [9,10,11], [12,13,14]]
for i in range(0, len(lst2D2)):
    for j in range(0, len(lst2D2[i])):
        print(lst2D2[i][j])
        
# len(lst2D2) => 5
# len(lst2D2[0]) => len([0,1,2]) => 3
# range(0, 3) -> 0 ~ 2
'''

#lst = [3,2,9,4,5,6], target = 7

# range(0, len(lst)), 0 1 2 3 4 5

'''
for i in range(0, len(lst)):
    for j in range(i + 1, len(lst)):
        a = lst[i]
        b = lst[j]
        c = a + b
        
        if c == target:
            print(a, b)
'''


            
            
            
            
            
            
            
            
            



lst = [3,2,9,4,5,6,10,17]
target = 27

for i in range(len(lst)):
    for j in range(i + 1, len(lst)):
        a = lst[i]
        b = lst[j]
        c = a + b
        
        if c == target:
            print(a, b)
   
'''
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
'''

nums = [2,7,11,15]
target = 9

for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        a = nums[i]
        b = nums[j]
        c = a + b
        
        if c == target:
            print(i, j)






















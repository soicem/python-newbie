# string comprehension
# string representation


s = "abcedfg"
    
# 앞에서부터 출력해보시오
for i in range(0, len(s), 1):
    print(s[i])
    
print()
    
# 뒤에서부터 출력해보시오
for i in range(len(s) - 1, -1, -1):
    print(s[i])
    
# two pointers     
left = 0
right = len(s) - 1 # 6

# left를 1씩 증가시키고, right를 1씩 감소를 동시에 시킬때, 두 값이 만나면 loop를 종료하시오

# true / false
'''
left = 0
right = 0

left>=0 && right<=6
left == right => true
left > right => false
left <= right => true
'''


# left보다 right가 더 클때만 loop를 돈다
# left<right

print()

left = 0
right = len(s) - 1
while left <= right:
    print(s[left], " ", s[right])
    left += 1
    right -= 1

    
    
    
    

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
# palindrome: 문자열 또는 숫자들이 좌우대칭 이루는 형태
'''
s = "abcba"  
left = 0
right = len(s) - 1

# base case
while left <= right:
    print(s[left] == s[right])
    left += 1
    right -= 1
'''

    
'''
ans = True
s2 = "abcba" 
left = 0
right = len(s2) - 1

while left <= right:
    # if를 써서 ans에 False를 저장
    if s2[left] != s2[right]:
        ans = False
    #print(s2[left] != s2[right])
    left += 1
    right -= 1

print(ans) 
'''   

print()
  
# odd, even(v)
ans = True
s3 = "abgcba"     
    
left = 0 # 0
right = len(s3) - 1 # 5
    
while left <= right:
    if s3[left] != s3[right]:
        ans = False
    left += 1
    right -= 1
    
print(ans)


    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

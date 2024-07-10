# 1.
# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. 
# The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000




# total = 0
# for i in range(1,1000):
#     if i%3 == 0 or i%5 == 0:
#         total += i

# print(total)







# 2.
# Mr. A is writing a bulletin board program
# Mr. A says he needs a program that 
# returns the total number of pages when the total number of posts and 
# the number of posts to be shown on one page are given as inputs.
# Input : m(total number of post), n(number of posts to be shown on one page)(n >= 1)
# Ouput : Total page 
# m         n       Output
# 0         1       0
# 1         1       1
# 2         1       2
# 1         10      1
# 10        10      1
# 11        10      2


# def board(m,n):
#     page = m // n # return quotient(intial estimate of the number of page) 1
#     if m % n != 0:
#         page = page + 1 # 1+1
#     return page

# a = board(11,10)
# print(a)








# 3. There is an array of n integers. 
# The array has both positive and negative integers. 
# Now you have to sort the array in a more special way.
# After alignment, the negative integers must be at the front and the positive integers at the back. 
# The order of positive and negative integers must also remain unchanged.
# Given data) Input : -1 1 3 2 -2 4
#             Output: -1 -2 1 3 2 4



# data=[-1,1,3,-2,2,4]
# ans1=[]
# ans2=[]
# for i in data:
#     if i < 0:
#         ans1.append(i)
#     else:
#         ans2.append(i)
#     # ans2.sort()
# ans=ans1+ans2
# print(ans)




# 4.
# The Fibonacci sequence refers to a sequence consisting of the sum of the previous two terms when the value of the first term is 0 and the value of the second term is 1.
# Write a program that outputs a Fibonacci sequence up to n when the input is an integer n (n>=3)
# Ex) 0,1,1,2,3,5,8,13
# Given data) fibonacci = [0,1]



# n = int(input("Enter the N : "))
# fibonacci = [0, 1]
# while fibonacci[-1] <= n: #fibonacci[-1] is the last element of the list
#     fibonacci.append(fibonacci[-1] + fibonacci[-2]) 

# print(fibonacci)





# 5.
# Caesar's code is a code created by the ancient Roman emperor Julius Caesar, for example, when you enter an alphabet A, the alphabet that follows n letters is printed. 
# For example, the word you want to change becomes CAT and HFY when n is designated as 5.

# Write a sentence to make a certain password and a program that produces and outputs a password when you type n.





# 5.
# key_input = input("Enter the N : ")
# str_input = input("Enter the password : ")
# result = ""
# for n in str_input : 
#     temp = ord(n) + (int)(key_input) #ord return unicode character -> unicode
#     result = result + chr(temp) # chr does the oppsite

# print(result)




# # 5. other solution
# a = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R","S", "T", "U", "V", "W", "X", "Y", "Z"]
# s = int(input("Enter the N : "))
# w = str(input("Enter the password : "))
# w = list(w)
# for q in range(0, len(w)):
#        for e in range(0, len(a)):
#               if w[q] == a[e]:
#                      d = (e + s) % 26 # 알파벳의 인덱스 범위 0-25. %26을 통해 다시 0부터 25사이의 인덱스로 변환.
#                      w[q] = a[d]
#                      break
# print("".join(w)) #리스트 형태의 변환된 단어를 문자열로 합쳐서 출력




# 6.
# The DashInsert function has the function of receiving a string composed of numbers, 
# adding - between the two numbers if odd numbers are continuous within the string, and adding * if even numbers are continuous
# Given data) Input : "4546793"
#             Output : "454*67-9-3"

# a="4546793"
# b=[]

# for i in range(0,len(a)-1):  
#     if (int(a[i])%2==0 and int(a[i+1])%2==0) : # even number
#         b.append(a[i]+"*")


#     elif (int(a[i])%2==1 and int(a[i+1])%2==1) : # odd number
#         b.append(a[i]+"-")

#     else :
#         b.append(a[i])

# print("".join(b)+a[len(a)-1])







# 7.
# Binary is to denote some natural numbers only as 0 and 1. 
# For example, 73 is expressed as 1001001 because it is 64(2^6)+8(2^3)+1(2^0). 
# Write a program that outputs a number in binary when it is entered.

# a = int(input("Enter the number : "))
# b = []
# while a: 
#     b.append(a%2) #binary 
#     a = a//2 # quotient 
# b.reverse()
# b = [str(x) for x in b] #list comprehension syntax : [expression for x in item]
# print("".join(b))





# 8.
# Make a program to distinguish the acute, right, and obtuse angles of a triangle with three angles.
# [60, 60, 60] = acute triangle
# [30, 60, 90] = right triangle
# [20, 40, 120] = obtuse triangle
# [0, 90, 90] = it's not triangle
# [60, 70, 80] = it's not triangle




# def search (x,y,z):
#     if x+y+z!= 180 or x==0 or y==0 or z==0:
#         print('It\'s not a triangle')


#     else:
#         if max(x,y,z)>90 :
#             print('obtuse')

#         elif max(x,y,z)==90:
#             print('right')

#         else:
#             print('acute')

#     return ''
# x=int(input('Enter the 1st angle :'))
# y=int(input('Enter the 2nd angle :'))
# z=int(input('Enter the 3rd angle :'))







# 9.
# Take three numbers as input and print out the number with a median value among the three numbers. 
# Ex1) 2, 5, 3 => 3 ex2) 4, 6, 4 => 4

# list = []
# i = 0
# while i <= 2:
#     number = int(input("Enter number : "))
#     list.append(number)
#     i += 1

# list.sort()
# print(list[1])




# 10. 
# Write a function that, given the points in one dimension, outputs pairs of the shortest of them. (Suppose that the arrangement of the points is all aligned.)
# For example, if S=[1, 3, 4, 8, 13, 17, 20] is given, the result value will be (3, 4).

# data = [1, 3, 4, 8, 13, 17, 20]

# def shortest(list):
#     result_list = []
#     for i in range(len(data)-1):
#         result_list.append(list[i+1] - list[i])   # find which pairs have the shortest distance.
#     index = result_list.index(min(result_list)) # shortest distance
#     return (list[index], list[index+1])   

# print(shortest(data))
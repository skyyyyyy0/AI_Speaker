# 1.
# total = 0
# for i in range(1,1000):
#     if i%3 == 0 or i%5 == 0:
#         total += i

# print(total)
 
# 2.
# def board(m,n):
#     page = m // n # return quotient
#     if m % n != 0:
#         page = page + 1
#     return page

# a = board(11,10)
# print(a)





# 3.
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
# n = int(input("Enter the N : "))
# fibonacci = [0, 1]
# while fibonacci[-1] <= n: #fibonacci[-1] is the last element of the list
#     fibonacci.append(fibonacci[-1] + fibonacci[-2]) 
# del fibonacci[-1] #To delete the last element
# print(fibonacci)


# 5.
# key_input = input("Enter the N : ")
# str_input = input("Enter the password : ")
# result = ""
# for n in str_input : 
#     temp = ord(n) + (int)(key_input) #ord return unicode character -> unicode
#     result = result + chr(temp) # chr does the oppsite

# print(result)

# 5. other solution
# a = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R","S", "T", "U", "V", "W", "X", "Y", "Z"]
# s = int(input("Enter the N : "))
# w = str(input("Enter the password : "))
# w = list(w)
# for q in range(0, len(w)):
#        for e in range(0, len(a)):
#               if w[q] == a[e]:
#                      d = (e + s) % 26 
#                      w[q] = a[d]
#                      break
# print("".join(w))



# 6.
# a="4546793"
# b=[]

# for i in range(0,len(a)-1):  
#     if (int(a[i])%2==0 and int(a[i+1])%2==0) : 
#         b.append(a[i]+"*")


#     elif (int(a[i])%2==1 and int(a[i+1])%2==1) : 
#         b.append(a[i]+"-")

#     else :
#         b.append(a[i])

# print("".join(b)+a[len(a)-1])


# 7.
# a = int(input("Enter the number : "))
# b = []
# while a: 
#     b.append(a%2) #binary 
#     a = a//2 # quotient
# b.reverse()
# b = [str(x) for x in b]
# print("".join(b))



# 8.
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

# print(search(x,y,z))



# 9.
# list = []
# i = 0
# while i <= 2:
#     number = int(input("Enter number : "))
#     list.append(number)
#     i += 1

# list.sort()
# print(list[1])


# 10.
# data = [1, 3, 4, 8, 13, 17, 20]

# def shortest(list):
#     result_list = []
#     for i in range(len(data)-1):
#         result_list.append(list[i+1] - list[i])   
#     index = result_list.index(min(result_list)) 
#     return (list[index], list[index+1])   

# print(shortest(data))






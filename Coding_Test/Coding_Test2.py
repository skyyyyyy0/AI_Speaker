# 1. 
# Mr. A has to solve a quadratic equation problem for his school homework. 
# But there is not much time left. Write a quadratic equation solving program to help Mr. A. 
# (However, the linear equation should use the root formula to find the solution by receiving a, b, and c from the equation ax^2 + bx + c = 0. 
# In addition, you should find the rounded value of an integer and find all the cases where there are no solutions or multiple solutions.)


# def fun(a,b,c):
#     D=b*b-4*a*c # we need to use this discriminant.
#     if D>0:
#         x1=round((-b-D**0.5)/2*a)
#         x2=round((-b+D**0.5)/2*a)
#         print("x","=",x1,",",x2)
#     elif D==0:
#         x=round(-b/2*a)
#         print("It's a multiple root")
#         print("x","=",x)
#     else:
#         print("It's an imaginary root")
# a=int(input("Input a : "))
# b=int(input("Input b : "))
# c=int(input("Input c : "))
# fun(a,b,c)











# 2. 
# It is said that about 2,000 years ago, soldiers were often trapped in caves by enemies in wars.
# It is said that they stood in a circle to prevent them from being taken prisoner, taking turns killing the third person, until the last person remained.
# The last person to be left was supposed to commit suicide, but it is said that they usually surrendered to their enemies.
# The problem you have to solve is to find out the position of the last surviving soldier given the total number of personnel (N) and the interval (K).
# For example, if there are a total of 10 soldiers and you take turns removing the third soldier, it is as follows:
# N = 10, K = 3
# In the above cases, soldiers are removed in the following order (bracket means soldiers removed)
# 1st round: 1 2 (3) 4 5 (6) 7 8 (9) 10
# 2nd round:                            1 (2) 4 5 (7) 8 10
# 3rd round:                                                (1) 4 5 (8) 10
# 4th round:                                                               4 (5) 10
# 5th round:                                                                        4 (10)
# The last surviving soldier in the above example is the fourth soldier.
# The input data are the total number of soldiers N and the interval K.
# The output data is the position of the soldier who survives to the end.
# (However, the initial start is from soldier number one.)
# Input/output examples are as follows:

# initial data:
# 10 3

# answer:
# 4

# def josephus(n, k):
#     # The range should be from 1 to n + 1. Because the range function doesn't include the last element.
#     soldiers = list(range(1, n + 1))
#     index = 0
    
#     # Repeat until one soldier is left. 
#     while len(soldiers) > 1:
#         # Remove a soldier from the position that has moved by (k-1) from the current index
#         index = (index + k - 1) % len(soldiers)
#         soldiers.pop(index)
#     # First while loop
#     # len = 10 
#     # index = (0 + 3 - 1) % 10 = 2 
#     # soldiers.pop(2) -> soldiers = [1,2,4,5,6,7,8,9,10] 
    
#     # Second while loop
#     # len = 9 
#     # index = (2 + 3 - 1) % 9 = 4 
#     # soldiers.pop(4) -> soldiers = [1,2,4,5,7,8,9,10]
    
#     # Third while loop
#     # len = 8
#     # index = (4 + 3 - 1) % 8 = 6 
#     # soldiers.pop(2) -> soldiers = [1,2,4,5,7,8,10]
#     # ...
    
    
#     return soldiers[0] # there's only one soldiers 

# N = 10
# K = 3

# print(josephus(N, K))






# 3.
# By receiving a character string and displaying the number of repetitions when the same character is repeated continuously, the character string is compressed.

# Input Example: aaabbccccca

# Output Example: a3b2c5a1

# s = "aaabbccccca"


# result = s[0] 
# count = 0 

# for i in s:
#     if i == result[-1]: 
#         count += 1
#     else:
#         result += str(count) + i 
#         count = 1
# result += str(count) 

# print(result)









# 4.
# Write a program that decodes the Morse code (dot: .dash:-) entered in string format and outputs it in English sentences.

# There are two spaces between letters and letters, and two spaces between words and words.

# For example, the following Morse code should be interpreted as "he sleep early." 

# .... .  ... .-.. . . .--. ...  . .- .-. .-.. -.--
# Morse Code Rule Table
# A	.-	    N	-.
# B	-...	O	---
# C	-.-.	P	.--.
# D	-..	    Q	--.-
# E	.	    R	.-.
# F	..-.	S	...
# G	--.	    T	-
# H	....	U	..-
# I	..	    V	...-
# J	.---	W	.--
# K	-.-	    X	-..-
# L	.-..	Y	-.--
# M	--	    Z	--..

# 4. 
# dic = {
#     '.-':'A','-...':'B','-.-.':'C','-..':'D','.':'E','..-.':'F',
#     '--.':'G','....':'H','..':'I','.---':'J','-.-':'K','.-..':'L',
#     '--':'M','-.':'N','---':'O','.--.':'P','--.-':'Q','.-.':'R',
#     '...':'S','-':'T','..-':'U','...-':'V','.--':'W','-..-':'X',
#     '-.--':'Y','--..':'Z'
# }

# def morse(src):
#     result = []
#     for word in src.split("  "):
#         for char in word.split(" "):
#             result.append(dic[char])
#         result.append(" ")
#     return "".join(result)


# print(morse('.... .  ... .-.. . . .--. ...  . .- .-. .-.. -.--'))











# 5.
# Some programming languages, such as Python, are said to prefer Pothole_case.

# Example:

# codingDojang --> coding_dojang

# numGoat30 --> num_goat_3_0

# Make a function that changes the CameleCase to the Pothole_case as shown above

# def case(l):
#     a = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789" # base36
#     return "".join(["_" + c.lower() if c in a else c for c in l])
#                     # (This is if ternary operator) Syntax = A if condition else B 
# print(case('numGoat30'))







# 6.
# Print out 20150111

# You only need to meet four terms

# There must be no numbers in the code.
# File name or path should not be used.
# Time, date functions should not be used.
# Error number output should not be used.





# string='aacddddd'
# a=string.count('a')        
# b=string.count('b')
# c=string.count('c')
# d=string.count('d')
# print(int(str(a)+str(b)+str(c)+str(d)+str(b)+str(c)+str(c)+str(c)))


# x=ord('e')+ord('d')
# y=ord('d')+ord('d')+ord('d')+ord('d')+ord('e')
# z=ord('o')
# array=[x,y,z]
# print("".join(array))





# print(int('bzvxb',ord('$'))) #base36 to decimal


# 7.
# Write a program that lets the user enter in an odd positive integer (you may assume the input is always valid),
# and prints out an ASCII art letter N made using the character N.

# If the input is 1, the output is:
# N

# If the input is 3, the output is:

# N N
# NNN
# N N

# If the input is 5, the output is:
    
# N   N
# NN  N
# N N N
# N  NN
# N   N

# def N(n):
#     for i in range(n):
#         print(''.join(["N" if j in [0,i,n-1] else " " for j in range(n)]))
# N(5)

# First if loop 
# i = 0 : [0,0,4]        N   N
# Second if loop
# i = 1 : [0,1,4]        NN  N
# Third if loop
# i = 2 : [0,2,4]        N N N
# Fourth if loop
# i = 3 : [0,3,4]        N  NN
# Fifth if loop
# i = 4 : [0,4,4]        N   N

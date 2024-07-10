# 1.
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
# def josephus(n, k):
#     # 초기 병사 리스트 생성 (1번 병사부터 n번 병사까지)
#     soldiers = list(range(1, n + 1))
    
#     # 제거할 병사의 인덱스를 추적할 변수
#     index = 0
    
#     # 병사가 한 명 남을 때까지 반복
#     while len(soldiers) > 1:
#         # 현재 인덱스에서 (k-1)만큼 이동한 위치의 병사를 제거
#         index = (index + k - 1) % len(soldiers)
#         soldiers.pop(index)
    
#     # 마지막으로 남은 병사의 번호 반환
#     return soldiers[0]

# # 예시 입력
# N = 10
# K = 3

# # 마지막으로 살아남는 병사의 위치 출력
# print(josephus(N, K))




# 3.
# s = "aaabbccccca"

# #초기값을 설정합니다.
# result = s[0] #반복문 실행되는 동안 문자열 형태로 반환되는 결과들을 담을 변수
# count = 0 #반복되서 나오는 문자 수만큼 카운팅되는 값을 담을 변수

# for i in s:
#     if i == result[-1]: #result변수 마지막 문자와 비교합니다. else에서 result변수에 값이 추가되기 때문에 마지막 문자[-1]와 비교.
#         count += 1
#     else:
#         result += str(count) + i #마지막 글자와 i가 다를 경우 카운팅된 값을 문자열 형태로 result 변수 마지막에 추가 해주고 i를 마지막 문자로 추가합니다.
#         count = 1
# result += str(count) #결과들이 담긴 변수에 마지막으로 카운팅된 값을 문자열 형태로 추가합니다.

# print(result)


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
# def do(l):
#     a = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
#     return "".join(["_" + c.lower() if c in a else c for c in l])
#                     # (This is if ternary operator) Syntax = A if condition else B 
# print(do('numGoat30'))



# 6.
# string='aacddddd'
# a=string.count('a')        
# b=string.count('b')
# c=string.count('c')
# d=string.count('d')
# print(int(str(a)+str(b)+str(c)+str(d)+str(b)+str(c)+str(c)+str(c)))



# print(int('bzvxb',ord('$')))

# 7.
# def N(n):
#     for i in range(n):
#         print(''.join(["N" if j in [0,i,n-1] else " " for j in range(n)]))
# N(7)




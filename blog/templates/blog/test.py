#Hello, I 938&d love programming, I like 81 python programming

# str = 'Hello, I 938&d love programming, I like 81 python programming'
# str1 = ''
# for i in range(0,len(str)):
#     # if int(str[i]) <= 0 and int(str[i]) <=9:
#     #     str.replace(str[i],'')
#     if not ord(str[i])<= 33 and not ord(str[i])>=58:
#         # print(ord(str[i]))
#         str.replace(str[i],'')
        
#     else:
#         str1 += str[i]

# print(str1)

str1 = 'I like python programming language'
start ='like'
end ='language'
new = ''
j =0

list1 = []
for i in range(0,len(str1)):
    
    if str1[i] == " ":
        list1.append(new.strip())
        new = ''
    new += str1[i]

if new.strip():
    list1.append(new.strip())
print(list1)
print(list1[4]==end)
ans = ''
for i in range(0,len(list1)):
    if list1[i] == start:
        j = i+1
        print(j)
        while list1[j] != end and j <= len(list1):
            ans += list1[j]+" "
            j+=1
        break
    else:
        pass
    # print(start==list1[1])
print(ans)




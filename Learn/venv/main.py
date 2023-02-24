# Comment ctrl + /
# print("Hello World!", end="\n") #standart end of line
# print("Результат: ", 6, 7, ".", sep="|", end="") #sep changes separate simbols
# print("Second \" Line")
# print('Third \' \\ line') # \t = tab
# print(5 // 3)
# print("Результат: ", min(1, 3 ,-0, 12, -2))
# print(pow(5, 3))
# print(round(5 / 3)) #округление к ближайшему
# input("Введите свой возраст: ")

# print("Result:", number) # float
# del number

# number = 5 # int
# boolean = False # bool
# digit = 4.123523
# word = "Result:" # string
# str_num = '4' #str
#
# # print(word + str(digit))
#
# print(word + str(number + int(str_num)))

# num1 = int(input('Введите первое число:'))
#
# num2 = int(input('Введите второе число:'))
#
# print('Result:', num1 + num2)
# print('Result:', num1 * num2)
# print('Result:', num1 / num2)
# print('Result:', num1 - num2)
# print('Result:', num1 ** num2)
#
# num1 += 5
# print(num1)

# word = 'hi!'
# print(word * 2)

# userData = int(input("Number:"))
# isHappy = True
#
# if isHappy and userData == 6: # or
#     print('User is happy')
# elif userData == 5:
#     print('number = 5')
# elif userData == 8:
#     print('number = 8')
# else:
#     print('User is not happy')

# if  userData == 5:
#     print("yep")
#     if userData >= 6:
#         print("Number is bigger than 5")
#
#
# data = input()
# if data == "Five":
#     number = 5
# else:
#     number = 0
#
# number = 5 if data == "Five" else 0
#
# print(number)

# for i in range(1, 6, 2):
#     print(i)

# count = 0
# word = "Hello World!"
# for i in word:
#     if i == "l":
#         count += 1
# print("count", count)
#
# i = 5
# isHasCar = True
# while isHasCar:
#     if input("enter data") == "Stop":
#         isHasCar = False

# for i in range(1, 11):
#     if i >= 5:
#         break
#     if i % 2 == 0:
#         continue
#     print(i)

# found = None
# for i in "Hello":
#     if i == "e":
#         found = True
#         break
# else:
#     found = False
# print(found)

# nums = [0, 8, 5.45, True, "Hola", [4, 5, 2, 3]]
#
# nums[0] = 5
#
# # print(nums[-1][2])
#
# numbers = [5, 2, 7]
# numbers.append(100)
# numbers.insert(1, True)
#
# b = [5, 6, 8]
# numbers.extend(b)
#
# # numbers.reverse()
# numbers.sort()
#
# numbers.pop()
# numbers.remove(6)
# # numbers.clear()
#
# print(len(numbers))

# nums = [5, 2, 7, "50", False]
#
# for element in nums:
#     element *= 2
#     print(element)
#
# n = int(input("Enter length:"))
# user_list = []
#
# i = 0
# while i < n:
#     string = "Enter element #" + str(i + 1) + ": "
#     user_list.append(input(string))
#     i += 1
# user_list.sort()
# print(user_list)
#
# word = 'Football, basketball, skate'
# # print(word.capitalize())
# # print(word.find('g'))
# hobby = word.split(', ')
# # print(hobby[1])
# for i in range (len(hobby)):
#     hobby[i] = hobby[i].capitalize()
# print(hobby)
#
# result = ", ".join(hobby)
# print(result)
# word = 'football'
# print(word[1:-1:2])

# lis = [6, 4 , 'Stroka', True, 6.5]
# print(lis[2:5:2])
# print(lis[::-2])

# # tuple
# data = (4, 6, 7, 3, 6, True, 5.6, 'Hello')
# # data[0] = 5 - no
# print(data[1:5])
# print(data)
# data1 = (5, 7, True)
# data = 4,
# print(data)
# print(data1)
# data = (4, 6, 7, 3, 6, True, 5.6, 'Hello')
#
# for el in data:
#     print(el)
#
# nums = [5,7,8]
#
# new_data = tuple(nums)
#
# word = "Hello world"
# word1 = tuple(word)
# print(word1)
# print('test\'')

print(True)
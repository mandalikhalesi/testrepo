# coding: UTF-8

#println("first trial again")

#year_str = input('your birth year in four digits: ')
#year = int(year_str)
#number_of_eto = (year + 8) % 12
#print('your eto year is', number_of_eto, '... ', end = '¥n')


#f-string using Python3

name = 'グイド'
age = 63
text = f'My name is {name} and I am {age} years old'
print(text)
text2= f'Next year I will be {age+1} years old'
print(text2)

eto_list = ['子', '丑', '寅', '卯', '辰', '巳', '午', '未', '申', '酉', '戌', '亥']
year_str = input('Please input your year of birth... ')
year = int(year_str)
number_of_eto = (year + 8) % 12
eto_name = eto_list[number_of_eto]
print(eto_name)
#print(f'your eto sign is: {eto_name}!)

# coding: UTF-8
#!/usr/local/bin/python3

#simple list repetition
#point_list = [50, 66, 99]
#for point in point_list:
#    print(f'点数は {point}です')
#print('繰り返し終了')

#list average
#weight_list = [50, 66, 99]
#total = 0
#for weight in weight_list:
#    total = total + weight
#number_of_weights = len(weight_list)
#average = total / number_of_weights
#print(f'平均体重は{average}です。')

#enumeration
#for index, color in enumerate(['red','green','blue']):
#    print(f'No.{index} is {color}...')

#if elif and BMI

weight_str = input('Input your weights (in kg) separated by a comma: ')
weight_str_list = weight_str.split(',')

weight_list = []
for weight_str in weight_str_list:
    weight = int(weight_str)
    weight_list.append(weight)

height_str = input('Input your height (in cm): ')
height = int(height_str)

for weight in weight_list:
    bmi = weight / (height / 100) ** 2
    if bmi >= 25:
        result = 'Overweight'
    elif bmi >= 18.5:
        result = 'Regular weight'
    else:
        result = 'Underweight'

    print(f'For a height of {height}cm and weight of {weight}kg, your BMI is: {bmi}.')
    print(f'Diagnostic result is: {result}')

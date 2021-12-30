# Part 1
file = open('Day 3/day3.in', 'r')

input_array = [line for line in file.readlines()]

input_array

input_array_2 = list(map(lambda s: s.strip(), input_array))

input_array_2

gamma = []

for bit in range(12):
  num1 = 0
  num0 = 0
  for number in input_array_2:
    if number[bit] == '1':
      num1 = num1+1
    else:
      num0 = num0+1
      
  if num1 > num0:
    gamma.append(1)
  elif num0 > num1:
    gamma.append(0)
  else:
    gamma.append(2)
      

print(gamma)
epsilon = []
for gamma_bit in gamma:
  if gamma_bit == 0:
    epsilon.append(1)
  else:
    epsilon.append(0)
    
print(epsilon)

def binary_decimal_convertor(binary_list):
  decimal = 0
  length = len(binary_list)
  for i in range(length):
    decimal = decimal + (2**(length-i-1))*binary_list[i]
    
  return decimal

gamma_number = binary_decimal_convertor(gamma)
gamma_number
epsilon_number = binary_decimal_convertor(epsilon)
epsilon_number
final_answer = gamma_number*epsilon_number
final_answer
# Correct answer

# Part 2

temp_list = input_array_2
oxygen_generator_rating = ''
# oxygen generator rating
for bit in range(12):
  num1 = 0
  num0 = 0
  num1_flag = False
  new_list = []
  for number in temp_list:
    if number[bit] == '1':
      num1 = num1+1
    else:
      num0 = num0+1
      
  if num1 >= num0:
    num1_flag = True
    print('bit 1')
  else:
    num1_flag = False
    print('bit 0')
    
  if num1_flag == True:
    print(bit, num1_flag)
    for number in temp_list:
      if number[bit] == '1':
        new_list.append(number)     
  else:
    print(bit, num1_flag)
    for number in temp_list:
      if number[bit] == '0':
        new_list.append(number)
  
  temp_list = new_list
  
  print(len(new_list))
  
  if len(new_list) == 1:     
    oxygen_generator_rating = new_list[0]
    break
    
oxygen_generator_rating_array = []
for i in range(12):
  oxygen_generator_rating_array.append(int(oxygen_generator_rating[i]))

oxygen_generator_rating_array

oxygen_generator_rating_number = binary_decimal_convertor(oxygen_generator_rating_array)
oxygen_generator_rating_number

# CO2 Scrubber Rating

temp_list = input_array_2
co2_scrubber_rating = ''

for bit in range(12):
  num1 = 0
  num0 = 0
  num0_flag = False
  new_list = []
  for number in temp_list:
    if number[bit] == '1':
      num1 = num1+1
    else:
      num0 = num0+1
      
  if num0 <= num1:
    num0_flag = True
    print('bit 0')
  else:
    num0_flag = False
    print('bit 1')
    
  if num0_flag == True:
    print(bit, num0_flag)
    for number in temp_list:
      if number[bit] == '0':
        new_list.append(number)     
  else:
    print(bit, num0_flag)
    for number in temp_list:
      if number[bit] == '1':
        new_list.append(number)
  
  temp_list = new_list
  
  print(len(new_list))
  
  if len(new_list) == 1:     
    co2_scrubber_rating = new_list[0]
    break
    
co2_scrubber_rating_array = []
for i in range(12):
  co2_scrubber_rating_array.append(int(co2_scrubber_rating[i]))

co2_scrubber_rating_array

co2_scrubber_rating_number = binary_decimal_convertor(co2_scrubber_rating_array)
co2_scrubber_rating_number

final_answer = oxygen_generator_rating_number*co2_scrubber_rating_number
# Correct Answer
import math

# Maximum Litres
max_litres = int(input())

# Litres of paint required for each digit
digit_list = list(map(int, input().split(" ")))

digit_dict = {1:digit_list[0], 2:digit_list[1], 3:digit_list[2], 4:digit_list[3], 5:digit_list[4], 6:digit_list[5], 7:digit_list[6], 8:digit_list[7], 9:digit_list[8]}

max_digit_usage_dict = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0}

numbers_can_be_painted = False

final_list_digits = []

final_number = ''

# Maximum of instances of the number that can be painted
def how_many_times_each_digit(local_dict, max_litres):
    local_dict = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0}
    #print("max_litres:", max_litres)
    for i in range(1,10):
        local_dict[i] = int(math.floor(max_litres/digit_dict[i]))
        #print("digit:", i, "required_litre", digit_dict[i], "max_turns", local_dict[i])
        #print("dictionary:", i, local_dict)
        
    return local_dict
        

# Check if no numbers can be painted
def can_numbers_be_painted(number_paint_value):
    for key, values in max_digit_usage_dict.items():
        #print(values)
        if values > 0:
            number_paint_value = True
            break
            
    return number_paint_value

# Let Igor Paint
def igor_is_painting(max_digit_usage_dict, max_litres, digit_dict, final_list_digits):
    max_value = max(max_digit_usage_dict.values())
    max_keys = [key for key, value in max_digit_usage_dict.items() if value == max_value]
    high_freq_digit = max(max_keys)
    #print("digit_dict", digit_dict)
    #print("igor is painting", high_freq_digit, "using", digit_dict[high_freq_digit], "litres")
    final_list_digits.append(str(high_freq_digit))
    max_litres = max_litres - digit_dict[high_freq_digit]
    #print("igor has ", max_litres, "litres left")
    max_digit_usage_dict = how_many_times_each_digit(max_digit_usage_dict, max_litres)
    numbers_can_be_painted = False
    numbers_can_be_painted = can_numbers_be_painted(numbers_can_be_painted)
    if max_litres > 0 and numbers_can_be_painted == True:
        igor_is_painting(max_digit_usage_dict, max_litres, digit_dict, final_list_digits)
        
max_digit_usage_dict = how_many_times_each_digit(max_digit_usage_dict, max_litres)
# print("max digit usage:", max_digit_usage_dict)
numbers_can_be_painted = can_numbers_be_painted(numbers_can_be_painted)    
if numbers_can_be_painted == False:
    print(-1)

else:
    igor_is_painting(max_digit_usage_dict, max_litres, digit_dict, final_list_digits)
    final_list_digits.sort(reverse = True)
    final_number = ''.join(final_list_digits)
    print(final_number)

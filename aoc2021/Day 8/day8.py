file = open('day8.in', 'r')

coded_messages = [line for line in file.readlines()]

sum = 0

for input_output_code in coded_messages:
    input_message_raw = input_output_code.split(" | ")[0]
    input_message_split = input_message_raw.split(" ")
    input_message_array = list(map(lambda s: s.strip(), input_message_split))
    
    #print("input message", input_message_array)
    #print("input message", list(map(lambda s: ''.join(sorted(s)), input_message_array)))
    
    one = ""
    two = ""
    three = ""
    four = ""
    five = ""
    six = ""
    seven = ""
    eight = ""
    nine = ""
    zero = ""
    
    for num in input_message_array:
        if len(num) == 2:
            one = ''.join(sorted(num))
            
        if len(num) == 3:
            seven = ''.join(sorted(num))
        
        if len(num) == 4:
            four = ''.join(sorted(num))
    
        if len(num) == 7:
            eight = ''.join(sorted(num))
            
    for num in input_message_array:
        if len(num) == 6:
            if (four[0] in num) and (four[1] in num) and (four[2] in num) and (four[3] in num):
                nine = ''.join(sorted(num))
                
            elif (one[0] in num and one[1] not in num) or (one[1] in num and one[0] not in num):
                six = ''.join(sorted(num))
                
            else:
                zero = ''.join(sorted(num))
                
    for num in input_message_array:                
        if len(num) == 5:
            if (one[0] in num and one [1] in num):
                three = ''.join(sorted(num))
                
            elif (num[0] in six and num[1] in six and num[2] in six and num[3] in six and num[4] in six):
                five = ''.join(sorted(num))
                
            else:
                two = ''.join(sorted(num))
                
    '''
    print("1: ", one)
    print("2: ", two)
    print("3: ", three)
    print("4: ", four)
    print("5: ", five)
    print("6: ", six)
    print("7: ", seven)
    print("8: ", eight)
    print("9: ", nine)
    print("0: ", zero)'''
        
    output_message_raw = input_output_code.split(" | ")[1]
    output_message_split = output_message_raw.split(" ")
    output_message_array = list(map(lambda s: s.strip(), output_message_split))
    
    #print("output_message: ", output_message_array)
    
    code_dict = {}
    code_dict[one] = 1
    code_dict[two] = 2
    code_dict[three] = 3
    code_dict[four] = 4
    code_dict[five] = 5
    code_dict[six] = 6
    code_dict[seven] = 7
    code_dict[eight] = 8
    code_dict[nine] = 9
    code_dict[zero] = 0
        
    output0 = ''.join(sorted(output_message_array[0]))
    output1 = ''.join(sorted(output_message_array[1]))
    output2 = ''.join(sorted(output_message_array[2]))
    output3 = ''.join(sorted(output_message_array[3]))
    
    #print(code_dict)
    
    #print(output0, output1, output2, output3)       
    actual_coded_output = code_dict[output0]*1000 + code_dict[output1]*100 + code_dict[output2]*10 + code_dict[output3]
    
    sum = sum + actual_coded_output


print(sum)
    
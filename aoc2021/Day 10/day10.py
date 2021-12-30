
# Part 1
file = open('day10.in', 'r')

syntax_lines = [line for line in file.readlines()]

character_dict = {'>' : 0, '}' : 0, ')' : 0, ']' : 0}

for line in syntax_lines:
    stack = []
    line_1 = line.strip()
    for syntax in line_1:
        if syntax in ('<', '{', '(', '['):
            stack.append(syntax)
            
        else:
            popped_item = stack.pop()
            if popped_item == '<' and syntax == '>':
                pass
                
            elif popped_item == '{' and syntax == '}':
                pass
                
            elif popped_item == '(' and syntax == ')':
                pass
                
            elif popped_item == '[' and syntax == ']':
                pass
                
            else:
                character_dict[syntax] = character_dict[syntax] + 1
                break
                

sum = 3*character_dict[')'] + 57*character_dict[']'] + 1197*character_dict['}'] + 25137*character_dict['>']

print(sum)
# Correct Answer

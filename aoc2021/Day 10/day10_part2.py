# Part 2
file = open('day10.in', 'r')

syntax_lines = [line for line in file.readlines()]

incomplete_lines = []

for line in syntax_lines:
    incorrect_line = False
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
                incorrect_line = True
                break
                
    if incorrect_line == False and len(stack) != 0:
        incomplete_lines.append(line_1)
        
        

scores = []
print("incomplete_lines: ", len(incomplete_lines))
for line in incomplete_lines:
    line_score = 0
    stack = []
    for syntax in line:
        if syntax in ('<', '{', '(', '['):
            stack.append(syntax)
        else:
            stack.pop()
            
    while len(stack) !=0:
        popped_item = stack.pop()
        if popped_item == '<':
            line_score = line_score*5+4
            
        elif popped_item == '{':
            line_score = line_score*5+3
            
        elif popped_item == '(':
            line_score = line_score*5+1
            
        elif popped_item == '[':
            line_score = line_score*5+2
            
    scores.append(line_score)
    
scores.sort()

print("total scores: ", len(scores))

middle_index = int((len(scores)-1)/2)

print(middle_index)

print(scores[middle_index])

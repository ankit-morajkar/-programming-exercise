class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = deque()
        
        for letter in s:
            if len(stack) == 0:
                stack.append([letter,1])
            else:
                if stack[-1][0] == letter:
                    stack[-1][1] += 1
                    if stack[-1][1]==k:
                        stack.pop()
                else:
                    stack.append([letter,1])
                    
        ans = ""
        if len(stack) == 0:
            return ans
        
        for item in stack:
            ans = ans + item[0]*item[1]
            
        return ans


# Naive Approach
# class Solution:
#     def removeDuplicates(self, s: str, k: int) -> str:
#         update_flag = True
#         while(update_flag):
#             update_flag = False
#             N = len(s)
#             prev_ele = ''
#             cons_check = 1
#             for i in range(N):
#                 if prev_ele == s[i]:
#                     cons_check += 1
#                 else:
#                     cons_check = 1
#                     prev_ele = s[i]

#                 if cons_check == k:
#                     update_flag = True
#                     if i<N:
#                         s = s[:(i-k+1)]+s[i+1:]
#                     else:
#                         s = s[:(i-k+1)]
#                     break
                    
            
#         return s
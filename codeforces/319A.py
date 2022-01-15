input_binary = input()

n= len(input_binary)
deci = int(input_binary,2)

print(deci*pow(2,n-1))
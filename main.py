num = input('Enter a number (decimal or integer): ')
# type your code here
num = num.strip()
num_check = num.replace(".",'')
num_check = num_check.strip()
num_check = num_check.lstrip("0")
sf = len(num_check)



# do not change any code beyond this point
print('The number', num, 'has', sf, 'significant figures.')

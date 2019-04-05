last_name = 'Smith'
count = 0

for letter in last_name:
    print(letter, ' ', count)  # note a space between ' '
    count += 1

print('---and the second loop----')

count = 0

while count < 5:
    print(last_name[count], ' ', count)
    count += 1

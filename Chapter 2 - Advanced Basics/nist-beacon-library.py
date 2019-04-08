# Get a 512 hex value from the beacon and display it
from nistbeacon import NistBeacon

record = NistBeacon.get_last_record()
v = record.output_value  # 512 hex
r = record.pseudo_random  # pick a pseudo random number

print('Your random follows: ')
print(r.randint(1, 10))  # print 1 - 10 random #random()) for floats .0 to 1.0
print()
print('Hex original value:\n', v, '\n')
d = int(v, 16)  # convert to decimal
print('Hex value converted to decimal:\n', d)

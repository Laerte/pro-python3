from nistbeacon import NistBeacon
import time

print()
print('Coin flip 0 or 1 tails or heads')
print()
print('Run five times')

for count in range(5):
    time.sleep(66)  # wait for new beacon every 66 seconds
    h = NistBeacon.get_last_record()
    v = h.output_value  # 512 hex
    d = int(v, 16)  # convert to decimal
    coin = d % 2  # modulus of record (0 or 1)

    if coin == 0:
        print('tails')
    else:
        print('heads')

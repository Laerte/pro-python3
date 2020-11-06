import struct

# uppercase letters indicate unsigned values
# lowercase letters indicate signed values


# B , b = 1 byte
print(struct.pack(b'B', 65))
print(struct.pack(b'B', 33))
print(struct.pack(b'BBBBBBB', 69, 120, 97, 109, 112, 108, 101))
print(struct.pack(b'b', 65))
print(struct.pack(b'Bb', 65, -23))
print(struct.pack(b'B', 130))

# H, h = 2 bytes
print(struct.pack(b'Hh', 42, -137))
print(struct.unpack(b'H', b'*\x00'))
print(struct.unpack(b'H', b'\x00*'))
print(struct.unpack(b'Hh', struct.pack(b'Hh', 42, -42)))
print(struct.pack(b'Hh', *struct.unpack(b'Hh', b'*\x00\x00*')))

# "<" = little-endian, ">" = big-endian
print(struct.pack(b'<H', 42))
print(struct.pack(b'>H', 42))
print(struct.unpack(b'<H', b'*\x00'))
print(struct.unpack(b'>H', b'*\x00'))

# I, i = 4 bytes
# Q, q = 8 bytes

# s format code, combined with a numeric prefix, to
# indicate the size of the string to read or write
print(struct.pack(b'7s', b'example'))
print(struct.unpack(b'7s', b'example'))
print(struct.pack(b'10s', b'example'))

first_name = 'Laerte'
last_name = 'Pereira'
age = 25

data = struct.pack(b'10s10sB', bytes(first_name, 'utf8'), bytes(last_name, 'utf8'), age)

print(data)
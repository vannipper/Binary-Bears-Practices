import sys

file = sys.stdin
lines = file.readlines()

line_count = 0
bytes = 0
words = 0

line_count = len(lines)

for line in lines:
    bytes += len(line)
    words += len(line.split(' '))

print(f"Lines = {line_count}")
print(f"Words = {words}")
print(f"Bytes = {bytes}")
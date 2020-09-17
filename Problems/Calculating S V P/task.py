# put your python code here
length = int(input())
width = int(input())
height = int(input())

print(4 * (length + width + height))  # Sum of lengths of all edges: s=4(a+b+c)
print(2 * (length * width + width * height + length * height))  # Surface area: S=2(ab+bc+ac)
print(length * width * height)  # Volume: V=abc

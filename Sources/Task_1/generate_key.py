import random
s = "abcdefghijklmnopqrstuvwxyz"
list = random.sample(s, len(s))
key = "".join(list)
print("Key:",key)
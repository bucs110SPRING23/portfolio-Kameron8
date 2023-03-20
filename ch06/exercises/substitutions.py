import json

file_pointer = open("news.txt", "r")
file_pointer2 = open("subs.json", "r")
data = json.load(file_pointer2)
for ch in file_pointer:
    x = 2

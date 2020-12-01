# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

tab = []
first = 0
second = 0

with open("input.txt") as f:
        lines = []
        for line in f:
            tab.append(line.rstrip())

for element in tab:
    for next in tab:
        if(int(element)+int(next)==2020):
            first=element
            second=next

print(first)
print(second)

print(int(first) * int(second))





# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

tab = []
mina = 0
maxa = 0

lookFor = ""
numberOfPolicyPasswords = 0


def check_contains(min_w, max_w, letter, checked_string):

    print("Looking for " + min_w + " - " + max_w + " letters " + letter + " in checked string: " + checked_string)
    found = 0
    new_max = int(max_w)
    new_min = int(min_w)
    new_string = checked_string[new_min-1:new_min]
    print("String index letter " + new_string)
    new_string = checked_string[new_max-1:new_max]
    print("String index letter " + new_string)
    print("Looking for letter " + letter + " on positions " + str(new_min-1) + " - " + str(new_max-1))
    if checked_string[new_min-1:new_min] == letter and checked_string[new_max-1:new_max] != letter or checked_string[new_min-1:new_min] != letter and checked_string[new_max-1:new_max] == letter:
        print("taaaaaaaaaaaaak")
        return True
    else:
        print("nooooooooooooo")
        return False

    # if found in range(min_w,max_w):
    #   return True
    # else:
    #   return False


with open("input.txt") as f:
    lines = []
    for line in f:
        tab.append(line.rstrip())
        string_length = len(line.rstrip())
        pause_position = (line.rstrip()).find("-", 0)
        whitespace = (line.rstrip()).find(" ", 0)
        twodots = line.rstrip().find(":", 0)
        mina = (line.rstrip()[0:pause_position:1])
        maxa = (line.rstrip()[pause_position+1:(whitespace+1 - pause_position + 1):1])
        lookFor = line.rstrip()[whitespace:string_length + -(string_length - twodots):1][1:2:1]
        password = (line.rstrip()[twodots + 2:string_length:1])
        if check_contains(mina, maxa, lookFor, password):
            numberOfPolicyPasswords = numberOfPolicyPasswords + 1
        else:
            print("Not found")

# for line in tab:
# print(line)


print("num" + str(numberOfPolicyPasswords))

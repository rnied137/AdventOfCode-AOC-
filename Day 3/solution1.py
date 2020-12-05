# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

tab = []
mina = 0
maxa = 0

lookFor = ""
numberOfPolicyPasswords = 0


def traverse_slope(tab):
    numb_of_trees = 0
    curr_x = 0
    curr_y = 0
    for slope in tab:
        check_tree = slope[curr_x+3:curr_x+4]
        print(check_tree)




    # if found in range(min_w,max_w):
    #   return True
    # else:
    #   return False


with open("input.txt") as f:
    lines = []
    for line in f:
        tab.append(line.rstrip())


# for line in tab:
for f in tab:
    print(f)

traverse_slope(tab)



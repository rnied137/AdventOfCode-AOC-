tab = []
mina = 0
maxa = 0
lineSize = 0

lookFor = ""
numberOfPolicyPasswords = 0


def traverse_slope(tab):
    numb_of_trees = 0
    curr_x = 0
    curr_y = 0
    i=0
    tabLenght = (len(tab))
    while i<tabLenght:
        lineSize = len(tab[i])
        check_tree = tab[i][curr_x + 3:curr_x + 4]
        i=i+1;

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

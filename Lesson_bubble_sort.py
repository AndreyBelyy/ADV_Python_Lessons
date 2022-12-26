test_l = [9, 56, 14, 0, 1, 129, 41]

def bubble(test_list):
    last_item = len(test_list) - 1
    for t in range(0, last_item):
        for u in range(0, last_item):
            if test_list[u] > test_list[u+1]:
                test_list[u], test_list[u+1] = test_list[u+1], test_list[u] # swap current index value with next one

    return test_list

bubble(test_l)
new_l = bubble(test_l).copy()
print(new_l)
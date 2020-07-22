n_list = [10, 2, 26, 15 , 10, 5, 7, 10, 2, 1]
n_listCopy = []
for number in n_list:
    if number not in n_listCopy:
        n_listCopy.append(number)
print(n_listCopy)
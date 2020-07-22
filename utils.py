def find_max(number_list):
    max = number_list[0]
    for i in number_list:
        if i > max:
            max = i
        return max


def func(my_list,desired_num):
    my_list.sort()
    
    i = 0
    j = len(my_list) - 1
    prev_pair = None
    while i < j:
        value = my_list[i] * my_list[j]
        if(value == desired_num):
            if(prev_pair == None or prev_pair != (my_list[i] , my_list[j])):
                yield (my_list[i] , my_list[j])
                prev_pair = (my_list[i] , my_list[j])
            i += 1
            j -= 1
        elif(value < desired_num):
            i += 1
        else:
            j -= 1

liste = [1,2,3,6,5,4] # 1 2 3 4 5 6

for pair in func(liste,6):
    print(pair)
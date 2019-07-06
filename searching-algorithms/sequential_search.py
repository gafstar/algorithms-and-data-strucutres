def seq_search(a_list, item):
    pos = 0
    found = False
    
    while pos < len(a_list) and not found:
        if a_list[pos] == item:
            found = True
        else: 
            pos +=1
    return found

test_list = [1, 2, 3, 4, 5, 6,12, 52, 23]
print (seq_search(test_list, 4))
print (seq_search(test_list, 13))
def merge_lists (list_1,list_2) :
    index_1 = 0
    index_2 = 0
    result = []
    
    while index_1 < len(list_1) or index_2 < len(list_2) :
           
        if index_1 == len(list_1) : 
            result.append(list_2[index_2])
            index_2 += 1
            #print("index_1 -- ",index_1,"/n index_2 -- ",index_2)
        elif index_2 == len(list_2) : 
            result.append(list_1[index_1])
            index_1 += 1
            #print("index_1 -- ",index_1,"/n index_2 -- ",index_2)
        elif list_1[index_1] < list_2[index_2] :
            result.append(list_1[index_1])
            index_1 += 1
            #print("index_1 -- ",index_1,"/n index_2 -- ",index_2)
        else :
            result.append(list_2[index_2])
            index_2 += 1
            #print("index_1 -- ",index_1,"/n index_2 -- ",index_2)

    return result

def main () :
    print(merge_lists([1,3,10],[0,4,7,9]))
    print(merge_lists([20,24],[0,4,7,9]))
    print(merge_lists([7,15,20,40],[2,10,23,30,35,44]))
    print(merge_lists([20,24],[20,21,22,23,24]))
    print(merge_lists([10,10,10],[10]))


if __name__ == "__main__" :
    main()
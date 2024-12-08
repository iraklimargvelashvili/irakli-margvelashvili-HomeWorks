
friendship_dict = {}

def friends_fairing() :
    friends_names = input("Write who is who's firnd or FINISH: ")

    if friends_names == 'FINISH' :
        #print(friendship_dict)
        return friendship_dict
    
    new_friends_list = friends_names.split('-')
    
    if friendship_dict.get(new_friends_list[0]) :
        friendship_dict[new_friends_list[0]] += f', {new_friends_list[1]}'
    else :
        friendship_dict[new_friends_list[0]] = new_friends_list[1]
        
    if friendship_dict.get(new_friends_list[1]) :
        friendship_dict[new_friends_list[1]] += f', {new_friends_list[0]}'
    else :
        friendship_dict[new_friends_list[1]] = new_friends_list[0]
    
    friends_fairing()
    return friendship_dict

def main():
    key_value = friends_fairing()
    for key, value in key_value.items():
        print(key,"-",value)    
    
if __name__ == "__main__" :
    main()
 


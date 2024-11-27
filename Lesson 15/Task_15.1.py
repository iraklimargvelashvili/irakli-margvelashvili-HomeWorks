from random import randint

def count_odd_even(list) :
    count_dict = {
        'odd' : 0,
        'even' : 0
    }
    
    for numb in list :
        if(numb % 2 == 0) :
            count_dict['even'] += 1
        else :
            count_dict['odd'] += 1
            
    return count_dict

def main() :
    numb_list = [randint(1,1000) for _ in range(100)]
    print(numb_list)
    print(count_odd_even(numb_list))

if __name__ == "__main__" :
    main()
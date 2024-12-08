def count_simbols(text) :
    simbols_dict = {}
    for chr in text :
        simbols_dict[chr] = (simbols_dict.get(chr) or 0) + 1
    return simbols_dict

def main() :
    string = input("Write anything: ")
    print(count_simbols(string))

if __name__ == "__main__" :
    main()
    

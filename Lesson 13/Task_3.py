def main() :
    text_list = ['aka','data','eka','tika','eva','ia','tina','liza','ema']
    print([word.upper() for word in text_list if len(word) <= 3])

if __name__ == "__main__" :
    main()
def car_info (brand, year = 2024, *countries, **options) :
    country = ''
    
    if countries :
        for place in countries :
            country += f' {place}, '
        text = f"{brand} sells cars in the following countries:{country}which are manufactured from {year} year."
        print(text)
    else :
        print(f"We coudn't find any country, where {brand} cells cars.")
        
    if options :
        print(f'{brand} manufactured cars with different options: ')
        for key,value in options.items() :
            print(f'{key} - {value}')
    else :
        print('As soon as we receive information on the options, we will upload it.')
    
car_info('BMW',1996,'Germany', 'USA', 'France', model = 'E 320', engine = 400)


    
    
    

    
#choose the car name and price of the most expensive car out of the list

car_prices= [('toyota prius',189000),('Mazda rx07',165000),('Lexus ls100',240000),('benz compressor',280000)]

def most_expensive_car(price_list):
    car_name=''
    maximum_car_price= 0

    for car,price in price_list:
        if maximum_car_price < price:
            car_name=car
            maximum_car_price =price

        else:
            pass

    return car_name,maximum_car_price

car,price = most_expensive_car(car_prices)

print(f'The most expensive car of the list is {car} with a price tag of SEK {price}')







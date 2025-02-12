import json
path = "cars.json"
with open(path, 'r') as cars_file:
    # cars = cars_file.read()
    cars = json.load(cars_file)
    # updatading the price of last row's values
    cars['cars'][2]['Price'] = '000'
    for car in cars['cars']:
        print("year: " + car['Year'] + "\n" + "Make: " + car['Make'] + "\n" + "Model: " + 
              car['Model'] + "\n" + "Price: " + car['Price'] + "\n" )
    # for row in cars['cars'] :
    #     print(list(row.values()))

    

 
# print(cars)
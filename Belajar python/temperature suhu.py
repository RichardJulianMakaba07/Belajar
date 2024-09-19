def weather():
    print('Welcome to Weather Today')
    
    name_user = input('Please Enter Your Name: ')
    while name_user == '':
        name_user = input('Please Enter Your Name: ')
        
    temperature = int(input(f"Hallo {name_user} Enter the current temperature to find out today's weather (°C): "))
    
    if 25 <= temperature <= 30:
        print("It's good weather\nEnjoy your day")
    elif 30 < temperature <= 35:
        print("It's a hot day\nDrink plenty of water")
    elif 15 <= temperature < 25:
        print("It's a cold day\nWear warm clothes")
    else:
        print('Extreme')
        
__name__ = '__main__'
weather()
# Conversão de temperatura

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5)+ 32

def celsius_to_kelvin(celsius):
    return celsius + 273.15
def main():
    celsius = float(input("Qual a temperatura está por aí?"))

    fahrenheit = celsius_to_fahrenheit(celsius)
    kelvin = celsius_to_kelvin(celsius)

    print(f"{celsius}ºC em fahrenheit é {fahrenheit}ºF")
    print(f"{celsius}ºC em kelvin é {kelvin}k")
    
if __name__=="__main__":
    main()

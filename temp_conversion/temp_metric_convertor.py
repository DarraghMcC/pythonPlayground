
class TempConvertor():

    def farenheitToCelcius(self, temp):
        return (int(temp) - 32) * 5.0/9.0

    def celciusToFarenheit(self, temp):
        return 9.0/5.0 * int(temp) + 32

def getTempValue(debugging=False):
        convertor = TempConvertor()
        temperature = raw_input("Enter a temperature: ")
        if isCelciusValue(temperature) and not isFarenheitValue(temperature):
            outputACelciusValue(stripTemperatureText(temperature), convertor)
        elif isFarenheitValue(temperature) and not isCelciusValue(temperature):
            outputAFarenheitValue(stripTemperatureText(temperature), convertor)
        elif not isFarenheitValue(temperature) and not isCelciusValue(temperature) and temperature.isdigit():
            print"[WARNING] You have not specified a temperature type, converting both"
            outputAFarenheitValue(temperature, convertor)
            outputACelciusValue(temperature, convertor)
        else:
            print"[WARNING] it seems an invlaid temperature value  been entered please try again"

def isFarenheitValue(temp):
    return "f" in temp.lower() or "fahrenheit" in temp.lower()

def stripTemperatureText(temp):
    return temp.lower().strip("f").strip("c").strip("fahrenheit").strip("celcius")

def isCelciusValue(temp):
    return "c" in temp.lower() or "celcius" in temp.lower()

def outputAFarenheitValue(temp, convertor):
        print "Temperature:", temp, "Fahrenheit = ", convertor.farenheitToCelcius(temp), " C"

def outputACelciusValue(temp, convertor):
        print "Temperature:", temp, "Celcius = ", convertor.celciusToFarenheit(temp), " F"


if __name__ == "__main__":
    getTempValue()

degrees_f_str = input("Temperature in Fahrenheit: ")
# Convert degrees_f_str to an integer
# Convert to °C
# Round to nearest whole number

degrees_f_int = int(degrees_f_str)

degrees_c = round((degrees_f_int - 32) * 5/9)


print("That's", degrees_c, "degrees Celcius")
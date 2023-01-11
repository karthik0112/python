weight = int(input("enter the weight"))
unit = (input("(L)bs or (K) g"))
if unit.upper() == "L":  # unit == "l"
    converted = weight * 0.45
    print(f'You are {converted} in kilos')
else:
    converted = weight / 0.45
    print(f'You are {converted} in pounds')

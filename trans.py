kilometres = float(input("Enter the distance in kilometres: "))
price = int(input("Enter the price: "))

if price >= 1000 and kilometres > 700:
    mode = "Car and Bike"
elif  price < 500 and kilometres < 699:
    mode = "Bus and train"
else:
    print("No suitable transportation available")

signal = input("Enter the traffic signal color (red/green/orange): ")

if signal == "red":
    action = "Stop"
elif signal == "green":
    action = "Run"
elif signal == "orange":
    action = "Pause"
else:
    action = "Invalid signal"

if mode !="no sutiable transport is available":
     print(f"For {kilometres} km at rupees {price} price, the mode of transportation is: {mode}.")
     print(f"Signal is :{signal}. Action is : {action}.")

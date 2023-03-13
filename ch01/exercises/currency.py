rate = float(input("Enter the current exchange rate going from the Euro to the US Dollar"))
amount = float(input("How many Euros would you like to exchange?"))
total = amount/rate 
result = (total-3)
print("You will recieve", result, "USD after the service fee is applied")
def calculate_discount(price,discount_percentage): #Defining the function and its parameters
    if discount_percentage >= 20: #Checking the condition of the discount pecentage
        discount_amount = (price * discount_percentage)/100 #calculating the discounted price
        new_price = price - discount_amount #checking the new price without the discounted price
        return new_price #showing the new price
    else:
        return price #showing the default price
actual_price = float(input('enter_the_price: ')) #capturing the product price
percent = float(input('enter the discount as a percentage: ')) #capturing the price percentage
Mutengo = calculate_discount(actual_price, percent ) #calling the price (Mutengo only means price in a native SA language)
print(Mutengo)
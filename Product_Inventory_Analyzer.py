total_products = int(input("How many products are there?"))

products = []
prices = []
quantities = [] 

total_inventory_value = {}
low_stock_items = {}

for i in range (total_products):
    product_name = str(input("Product Name :"))
    products.append(product_name)
    price_of_product = int(input("Price :"))
    prices.append(price_of_product)
    number_of_product = int(input("No. of Items :"))
    quantities.append(number_of_product)
    print()


# print(products)
# print(prices)
# print(quantities)

# Pythom creates it and immediately discards it ( In loop zip() is doing the zipping and letting you proceed with the program, so the standalone line is unnecessary)
# zip(products,prices,quantities)   

# for item in zip(products,prices,quantities):
#     print(item)

# print(list(zip(products,prices,quantities)))

for product,price,quantity in zip(products,prices,quantities):
    inventory_value = price * quantity
    total_inventory_value[product] = inventory_value

    if(quantity < 5):
        low_stock_items[product] = quantity

print()
print()
print("****************** TOTAL INVENTORY VALUE ***********************")
print(total_inventory_value)
print()
print()
print("******************* LOW STOCK ITEMS *************************")
print(low_stock_items)
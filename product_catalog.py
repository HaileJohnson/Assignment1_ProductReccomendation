from product_data import products
# TODO: Step 1 - Print out the products to see the data that you are working with.

print(products)

# TODO: Step 2 - Create a list called customer_preferences and store the user preference in this list.

customer_preferences =[]

response = ""
while response != "N":
    print("Input a preference:")
    preference = input()
   
    # Add the customer preference to the list
    customer_preferences.append(preference)

    response = input("Do you want to add another preference? (Y/N): ").upper()
  

# TODO: Step 3 - Convert customer_preferences list to set to eliminate duplicates.

customer_preferences = set(customer_preferences)
print(customer_preferences)

# TODO: Step 4 - Convert the product tags to sets in order to allow for faster comparisons.
converted_products = []

for product in products:
    product_new = product.copy()
    product_new['tags'] = set(product['tags'])
    converted_products.append(product_new)

print(converted_products)

# TODO: Step 5 - Write a function to calculate the number of matching tags
def count_matches(product_tags, customer_tags):
    '''
    Args:
        product_tags (set): A set of tags associated with a product.
        customer_tags (set): A set of tags associated with the customer.
    Returns:
        int: The number of matching tags between the product and customer.
    '''
    count = 0

    for tag in product_tags:
        if tag in customer_tags:
            count += 1
    return count



# TODO: Step 6 - Write a function that loops over all products and returns a sorted list of matches
def recommend_products(products, customer_tags):
    recommendations = []
    
    for product in products: 
        match_count = count_matches(product['tags'], customer_tags)
        recommendations.append({
            'name': product['name'],
            'match_count': match_count
        })

    recommendations.sort(key=lambda x: x['match_count'], reverse = True)

    return recommendations 

results = recommend_products(converted_products, customer_preferences)
print("\nRecommended Products (sorted by match count):")
for product in results:
    print(f"{product['name']} - Matches: {product['match_count']}")

    '''
    Args:
        products (list): A list of product dictionaries.
        customer_tags (set): A set of tags associated with the customer.
    Returns:
        list: A list of products containing product names and their match counts.
    '''
    pass



# TODO: Step 7 - Call your function and print the results

# [{'name': 'Eco Water Bottle', 'tags': ['eco-friendly', 'durable', 'recyclable']}, {'name': 'Trail Backpack', 'tags': ['durable', 'water-resistant', 'lightweight']}, {'name': 'Vegan Leather Wallet', 'tags': ['vegan', 'stylish', 'compact']}, {'name': 'Bamboo Toothbrush', 'tags': ['eco-friendly', 'vegan', 'biodegradable']}, {'name': 'Smartwatch', 'tags': ['tech', 'durable', 'stylish']}, {'name': 'LED Desk Lamp', 'tags': ['energy-efficient', 'adjustable', 'stylish']}, {'name': 'Running Shoes', 'tags': ['lightweight', 'durable', 'comfortable']}, {'name': 'Bluetooth Speaker', 'tags': ['portable', 'tech', 'wireless']}, {'name': 'Portable Charger', 'tags': ['tech', 'travel-friendly', 'reliable']}, {'name': 'Noise-Cancelling Headphones', 'tags': ['tech', 'quiet', 'comfortable']}, {'name': 'Compost Bin', 'tags': ['eco-friendly', 'kitchen', 'odor-resistant']}, {'name': 'Yoga Mat', 'tags': ['fitness', 'non-slip', 'lightweight']}, {'name': 'Reusable Grocery Bags', 'tags': ['eco-friendly', 'reusable', 'foldable']}, {'name': 'Ergonomic Office Chair', 'tags': ['comfortable', 'adjustable', 'supportive']}, {'name': 'Air Purifier', 'tags': ['tech', 'health', 'quiet']}, {'name': 'Gaming Mouse', 'tags': ['tech', 'responsive', 'ergonomic']}, {'name': 'Fitness Tracker', 'tags': ['tech', 'fitness', 'wearable']}, {'name': 'Standing Desk', 'tags': ['adjustable', 'ergonomic', 'modern']}, {'name': 'Mini Projector', 'tags': ['portable', 'tech', 'entertainment']}, {'name': 'Cast Iron Skillet', 'tags': ['durable', 'kitchen', 'versatile']}, {'name': 'Electric Kettle', 'tags': ['kitchen', 'tech', 'energy-efficient']}, {'name': 'Foldable Bike', 'tags': ['eco-friendly', 'portable', 'fitness']}, {'name': 'Smart Thermostat', 'tags': ['tech', 'energy-efficient', 'smart-home']}, {'name': 'Wool Blanket', 'tags': ['warm', 'natural', 'cozy']}, {'name': 'Digital Notebook', 'tags': ['tech', 'reusable', 'stylish']}, {'name': 'Bamboo Cutlery Set', 'tags': ['eco-friendly', 'reusable', 'compact']}, {'name': 'Compact Air Fryer', 'tags': ['kitchen', 'tech', 'compact']}, {'name': 'Solar Phone Charger', 'tags': ['eco-friendly', 'tech', 'travel-friendly']}, {'name': 'Insulated Lunch Box', 'tags': ['kitchen', 'portable', 'durable']}, {'name': 'Smart Light Bulbs', 'tags': ['tech', 'energy-efficient', 'smart-home']}, {'name': 'Laptop Stand', 'tags': ['tech', 'ergonomic', 'portable']}, {'name': 'Electric Bike', 'tags': ['eco-friendly', 'tech', 'fitness']}, {'name': 'Digital Pen', 'tags': ['tech', 'writing', 'portable']}, {'name': 'Silicone Food Storage Bags', 'tags': ['kitchen', 'reusable', 'eco-friendly']}, {'name': 'UV Sanitizer Box', 'tags': ['tech', 'health', 'compact']}, {'name': 'Virtual Reality Headset', 'tags': ['tech', 'entertainment', 'immersive']}, {'name': 'Hydroponic Indoor Garden', 'tags': ['eco-friendly', 'tech', 'kitchen']}, {'name': 'Wireless Charging Pad', 'tags': ['tech', 'convenient', 'modern']}, {'name': 'Magnetic Whiteboard', 'tags': ['office', 'reusable', 'functional']}, {'name': 'LED String Lights', 'tags': ['decor', 'energy-efficient', 'stylish']}, {'name': 'Adjustable Dumbbells', 'tags': ['fitness', 'compact', 'durable']}, {'name': 'Weighted Blanket', 'tags': ['cozy', 'health', 'comfortable']}, {'name': 'Camping Stove', 'tags': ['portable', 'outdoors', 'reliable']}, {'name': 'Touchless Trash Can', 'tags': ['kitchen', 'tech', 'convenient']}, {'name': 'Electric Toothbrush', 'tags': ['tech', 'health', 'rechargeable']}, {'name': 'Noise Machine', 'tags': ['health', 'sleep', 'portable']}, {'name': 'Pet Water Fountain', 'tags': ['tech', 'pet', 'eco-friendly']}, {'name': 'Motion Sensor Light', 'tags': ['tech', 'smart-home', 'safety']}, {'name': 'Smart Door Lock', 'tags': ['tech', 'security', 'smart-home']}, {'name': 'Cold Brew Coffee Maker', 'tags': ['kitchen', 'compact', 'durable']}]
# Input a preference:
# cozy
# Do you want to add another preference? (Y/N): y
# Input a preference:
# pet
# Do you want to add another preference? (Y/N): y
# Input a preference:
# tach
# Do you want to add another preference? (Y/N): y
# Input a preference:
# tech
# Do you want to add another preference? (Y/N): y
# Input a preference:
# pet
# Do you want to add another preference? (Y/N): n
# {'tach', 'pet', 'cozy', 'tech'}
# [{'name': 'Eco Water Bottle', 'tags': {'eco-friendly', 'recyclable', 'durable'}}, {'name': 'Trail Backpack', 'tags': {'lightweight', 'water-resistant', 'durable'}}, {'name': 'Vegan Leather Wallet', 'tags': {'stylish', 'vegan', 'compact'}}, {'name': 'Bamboo Toothbrush', 'tags': {'eco-friendly', 'biodegradable', 'vegan'}}, {'name': 'Smartwatch', 'tags': {'stylish', 'tech', 'durable'}}, {'name': 'LED Desk Lamp', 'tags': {'energy-efficient', 'stylish', 'adjustable'}}, {'name': 'Running Shoes', 'tags': {'lightweight', 'durable', 'comfortable'}}, {'name': 'Bluetooth Speaker', 'tags': {'wireless', 'portable', 'tech'}}, {'name': 'Portable Charger', 'tags': {'travel-friendly', 'tech', 'reliable'}}, {'name': 'Noise-Cancelling Headphones', 'tags': {'comfortable', 'quiet', 'tech'}}, {'name': 'Compost Bin', 'tags': {'eco-friendly', 'kitchen', 'odor-resistant'}}, {'name': 'Yoga Mat', 'tags': {'lightweight', 'fitness', 'non-slip'}}, {'name': 'Reusable Grocery Bags', 'tags': {'eco-friendly', 'reusable', 'foldable'}}, {'name': 'Ergonomic Office Chair', 'tags': {'comfortable', 'supportive', 'adjustable'}}, {'name': 'Air Purifier', 'tags': {'quiet', 'tech', 'health'}}, {'name': 'Gaming Mouse', 'tags': {'responsive', 'tech', 'ergonomic'}}, {'name': 'Fitness Tracker', 'tags': {'fitness', 'tech', 'wearable'}}, {'name': 'Standing Desk', 'tags': {'modern', 'ergonomic', 'adjustable'}}, {'name': 'Mini Projector', 'tags': {'portable', 'tech', 'entertainment'}}, {'name': 'Cast Iron Skillet', 'tags': {'versatile', 'kitchen', 'durable'}}, {'name': 'Electric Kettle', 'tags': {'energy-efficient', 'kitchen', 'tech'}}, {'name': 'Foldable Bike', 'tags': {'portable', 'eco-friendly', 'fitness'}}, {'name': 'Smart Thermostat', 'tags': {'energy-efficient', 'tech', 'smart-home'}}, {'name': 'Wool Blanket', 'tags': {'natural', 'cozy', 'warm'}}, {'name': 'Digital Notebook', 'tags': {'reusable', 'tech', 'stylish'}}, {'name': 'Bamboo Cutlery Set', 'tags': {'eco-friendly', 'reusable', 'compact'}}, {'name': 'Compact Air Fryer', 'tags': {'kitchen', 'tech', 'compact'}}, {'name': 'Solar Phone Charger', 'tags': {'eco-friendly', 'travel-friendly', 'tech'}}, {'name': 'Insulated Lunch Box', 'tags': {'portable', 'kitchen', 'durable'}}, {'name': 'Smart Light Bulbs', 'tags': {'energy-efficient', 'tech', 'smart-home'}}, {'name': 'Laptop Stand', 'tags': {'portable', 'tech', 'ergonomic'}}, {'name': 'Electric Bike', 'tags': {'eco-friendly', 'tech', 'fitness'}}, {'name': 'Digital Pen', 'tags': {'portable', 'tech', 'writing'}}, {'name': 'Silicone Food Storage Bags', 'tags': {'reusable', 'kitchen', 'eco-friendly'}}, {'name': 'UV Sanitizer Box', 'tags': {'tech', 'compact', 'health'}}, {'name': 'Virtual Reality Headset', 'tags': {'immersive', 'tech', 'entertainment'}}, {'name': 'Hydroponic Indoor Garden', 'tags': {'eco-friendly', 'kitchen', 'tech'}}, {'name': 'Wireless Charging Pad', 'tags': {'convenient', 'tech', 'modern'}}, {'name': 'Magnetic Whiteboard', 'tags': {'office', 'reusable', 'functional'}}, {'name': 'LED String Lights', 'tags': {'energy-efficient', 'decor', 'stylish'}}, {'name': 'Adjustable Dumbbells', 'tags': {'fitness', 'durable', 'compact'}}, {'name': 'Weighted Blanket', 'tags': {'comfortable', 'cozy', 'health'}}, {'name': 'Camping Stove', 'tags': {'portable', 'reliable', 'outdoors'}}, {'name': 'Touchless Trash Can', 'tags': {'convenient', 'kitchen', 'tech'}}, {'name': 'Electric Toothbrush', 'tags': {'tech', 'rechargeable', 'health'}}, {'name': 'Noise Machine', 'tags': {'portable', 'sleep', 'health'}}, {'name': 'Pet Water Fountain', 'tags': {'eco-friendly', 'pet', 'tech'}}, {'name': 'Motion Sensor Light', 'tags': {'smart-home', 'tech', 'safety'}}, {'name': 'Smart Door Lock', 'tags': {'smart-home', 'tech', 'security'}}, {'name': 'Cold Brew Coffee Maker', 'tags': {'kitchen', 'durable', 'compact'}}]

# Recommended Products (sorted by match count):
# Pet Water Fountain - Matches: 2
# Smartwatch - Matches: 1
# Bluetooth Speaker - Matches: 1
# Portable Charger - Matches: 1
# Noise-Cancelling Headphones - Matches: 1
# Air Purifier - Matches: 1
# Gaming Mouse - Matches: 1
# Fitness Tracker - Matches: 1
# Mini Projector - Matches: 1
# Electric Kettle - Matches: 1
# Smart Thermostat - Matches: 1
# Wool Blanket - Matches: 1
# Digital Notebook - Matches: 1
# Compact Air Fryer - Matches: 1
# Solar Phone Charger - Matches: 1
# Smart Light Bulbs - Matches: 1
# Laptop Stand - Matches: 1
# Electric Bike - Matches: 1
# Digital Pen - Matches: 1
# UV Sanitizer Box - Matches: 1
# Virtual Reality Headset - Matches: 1
# Hydroponic Indoor Garden - Matches: 1
# Wireless Charging Pad - Matches: 1
# Weighted Blanket - Matches: 1
# Touchless Trash Can - Matches: 1
# Electric Toothbrush - Matches: 1
# Motion Sensor Light - Matches: 1
# Smart Door Lock - Matches: 1
# Eco Water Bottle - Matches: 0
# Trail Backpack - Matches: 0
# Vegan Leather Wallet - Matches: 0
# Bamboo Toothbrush - Matches: 0
# LED Desk Lamp - Matches: 0
# Running Shoes - Matches: 0
# Compost Bin - Matches: 0
# Yoga Mat - Matches: 0
# Reusable Grocery Bags - Matches: 0
# Ergonomic Office Chair - Matches: 0
# Standing Desk - Matches: 0
# Cast Iron Skillet - Matches: 0
# Foldable Bike - Matches: 0
# Bamboo Cutlery Set - Matches: 0
# Insulated Lunch Box - Matches: 0
# Silicone Food Storage Bags - Matches: 0
# Magnetic Whiteboard - Matches: 0
# LED String Lights - Matches: 0
# Adjustable Dumbbells - Matches: 0
# Camping Stove - Matches: 0
# Noise Machine - Matches: 0
# Cold Brew Coffee Maker - Matches: 0


# DESIGN MEMO (write below in a comment):
# 1. What core operations did you use (e.g., intersections, loops)? Why?

# I used loops to collect the users input, convert product tags to sets, counting
# my matches, and reccomending products. The reason I used loops for this application is 
# because loops make the data easier to organize and call upon

# I used intersections to find the matches between the customer preferences and the product tags

#I used the sorting functions such as list.sort() and the lambada to sort through which products
#have the most matches. I used lambada because it is the easiest to use when sorting through 
# an item with a specific count. Using the function allows me to sort through how many matches
# with the product name attached. 

# I used sets, as taught in the notes, to eliminate any duplicates and make it easier to sift
# through data 

# 2. How might this code change if you had 1000+ products?

# If we were working with 1000+ products we would have to start worrying about effeciency of our code
# right now we are comparing each preference with every product tag which might take a lot 
# longer if we had 1000+ products

# with a larger list there is also a concern for device storage. In my code I copy the product 
# data in order to create a new list to turn into a set. With 1000+ products storagemay begin
# to be a issue.

# finally displayable matches becomes an issue as well. My current code returns all of the products
# sorted based on how many matches thay have. But if there is 1000+ products printing all of them
# even if it is based on matched is alot of data.
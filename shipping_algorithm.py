# Sal runs the biggest shipping company in the tri-county area, Sal’s Shippers. Sal wants to make sure that every single one of his customers has the best, and most affordable experience shipping their packages. In this project, you’ll build a program that will take the weight of a package and determine the cheapest way to ship that package using Sal’s Shippers.

# Sal’s Shippers has several different options for a customer to ship their package. They have ground shipping, which is a small flat charge plus a rate based on the weight of your package. Premium ground shipping, which is a much higher flat charge, but you aren’t charged for weight. They recently also implemented drone shipping, which has no flat charge, but the rate based on weight is triple the rate of ground shipping.

# Here are the prices:

# Premium Ground Shipping
# Flat charge: 125.00

# Ground Shipping:
# Weight                    Price per pound       Flat Charge
# 2 lb or less              1.50                  20.00
# over 2 lb but <= 6 lb     3.00                  20.00
# over 6 lb but <= 10 lb    4.00                  20.00
# over 10 lb                4.75                  20.00

# Drone Shipping:
# Weight                    Price per pound       Flat Charge
# 2 lb or less              4.50                  0.00
# over 2 lb but <= 6 lb     9.00                  0.00
# over 6 lb but <= 10 lb    12.00                 0.00
# over 10 lb                14.25                 0.00

# Write a program that asks the user for the weight of their package and then tells them which method of shipping is cheapest and how much it will cost to ship their package using Sal’s Shippers.

############################################################
############################################################

# Calcutating price of Std. Ground Shipping


def ground_shipping(weight):
    flat_charge = 20.00
    if weight > 10.00:
        price = flat_charge + 4.75 * weight
    elif weight > 6.00:
        price = flat_charge + 4.00 * weight
    elif weight > 2.00:
        price = flat_charge + 3.00 * weight
    else:
        price = flat_charge + 1.50 * weight
    return price


# Calcutating price of Drone Shipping


def drone_shipping(weight):
    flat_charge = 0.00
    if weight > 10.00:
        price = flat_charge + 4.50 * weight
    elif weight > 6.00:
        price = flat_charge + 9.00 * weight
    elif weight > 2.00:
        price = flat_charge + 12.00 * weight
    else:
        price = flat_charge + 14.25 * weight
    return price


# Calcutating price of Ground Shipping


def cheapest_shipping(weight):
    ground = ground_shipping(weight)
    # Uncomment to display final value of ground shipping
    # print(ground)
    drone = drone_shipping(weight)
    # Uncomment to display final value of drone shipping
    # print(drone)
    premium = 125.00
    # Uncomment to display value of premium shipping
    # print(premium)
#
#
    if ground < premium and drone < premium:
        if ground < drone:
            print('Best choice: standard shipping: $' + str(ground))
        elif drone < ground:
            print('Best choice: drone shipping: $' + str(drone))
        else:
            print(
                'Best choice: standard or drone: $' + str(ground))
    elif premium == ground:
        print('Best choice: premium or standard: $' + str(ground))
    elif premium == drone:
        print('Best choice: premium or drone: $' + str(ground))
    else:
        print('Best choice: premium shipping: $125.00')


# Run this function with the weight of your package

cheapest_shipping()

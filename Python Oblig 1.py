# Assignment number 1

# Making a simple separator line function, mostly for fun

def print_line():
    print("-" * 110)

# Defining the constants for my assignment

# Insurance costs in NOK per year

insurance_cost_electric = 5000  
insurance_cost_gas = 7500  

# NOK per year for both electric and gas cars

traffic_insurance_fee = 8.38 * 365 


# kWh per km 

electric_consumption_per_km = 0.2  

# NOK per kWh

electricity_price_per_kWh = 2.00  

gas_consumption_cost_per_km = 1.0  # Cost in NOK per km

toll_cost_electric_per_km = 0.1  # Toll cost in NOK per km
toll_cost_gas_per_km = 0.3  # Toll cost in NOK per km

# Assuming 12,000 km per year, as that is my normal usage

km_per_year = 12000

# Calculating annual cost for an electric car

electricCar_cost_per_year = (
    insurance_cost_electric +
    traffic_insurance_fee +
    (electric_consumption_per_km * electricity_price_per_kWh * km_per_year) +
    (toll_cost_electric_per_km * km_per_year)
)

# Calculating  annual cost for a gas car

gasCar_cost_per_year = (
    insurance_cost_gas +
    traffic_insurance_fee +
    (gas_consumption_cost_per_km * km_per_year) +
    (toll_cost_gas_per_km * km_per_year)
)

''' Calculating the difference between the two options, gas and
 electric and giving an absolute value as an answer
 '''

cost_difference = abs(gasCar_cost_per_year - electricCar_cost_per_year)

# Printing the results with 2 decimals
print_line()
print(f"Annual cost for electric car: {electricCar_cost_per_year:.2f} NOK")
print_line()
print(f"Annual cost for gas car: {gasCar_cost_per_year:.2f} NOK")
print_line()

# Here I compare the costs and print which is more the expensive car

if gasCar_cost_per_year > electricCar_cost_per_year:
    print(f"The gas car is more expensive by {cost_difference:.2f} NOK per year.")
elif electricCar_cost_per_year > gasCar_cost_per_year:
    print(f"The electric car is more expensive by {cost_difference:.2f} NOK per year.")
else:
    print("Both cars have the same annual cost.")

print_line()

# Recommendations for what car to purchase if cost is the only factor. 

if electricCar_cost_per_year < gasCar_cost_per_year:
    print("If cost is the most important factor then I would go with the electric car as it is the cheapest option.")
elif gasCar_cost_per_year < electricCar_cost_per_year:
    print("If cost is the most important factor then I would go with the gas car as it is the cheapest option of the two.")
else:
    print("Recommendation: Both cars cost the same, so choose based on other factors.")
       
print_line()
print_line()

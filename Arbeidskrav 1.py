# -*- coding: utf-8 -*-
"""
Created on Thu Oct 24 20:35:25 2024

@author: sult_
"""


# Creating a separator just for readability, and fun. 
def print_line():
    print("-" *120)

# The total kilometers driven in a year for each car based personal usage    
sum_km = 12000

# Electrical and gas vehicle costs eV = Electric Vehicle, gH = Gas Vehicle
insurance_eV = 5000

insurance_gV = 7500

Trafikkforsikringsavgift = 8.38

tf_avgift = Trafikkforsikringsavgift

# Trafikkforsikringsavgift per year = 8.38 all days of the year

yearly_tf_avgift = 8.38 * 365 

# Will just call both for "fuel" as fuel can mean several things and not just "gas"

fuel_usage_per_km_eV = 0.2

fuel_cost_per_km_gV = 1

sum_fuel_usage_eV = 0.2 * sum_km

eV_cost_per_km = 2

#Toll tax ( i mangel på bedre ord) for both vehicles

tolltax_eV_per_km = 0.1

tolltax_gV_per_km = 0.3

sum_tolltax_eV = tolltax_eV_per_km * sum_km

sum_tolltax_gV = tolltax_gV_per_km * sum_km



#Total fuel cost for the electric vehicle
sum_fuel_cost_eV = sum_fuel_usage_eV * eV_cost_per_km

#Total fuel cost for the gas vehicle
sum_fuel_cost_gV = fuel_cost_per_km_gV * sum_km 

sum_all_costs_eV_per_year = ((sum_fuel_cost_eV + tolltax_eV_per_km * sum_km) +
    (insurance_eV) + (yearly_tf_avgift)
    
    )

sum_all_costs_gV_per_year = ((sum_fuel_cost_gV + tolltax_gV_per_km * sum_km) +
    (insurance_gV) + (yearly_tf_avgift)
    
    )


#Creating subtotals along the way to test that everything is working. Printing results is a good way to test this, setting 2 decimals. 

print_line()


print(f"Fuel cost of the electric vehicle is a total of {sum_fuel_cost_eV:.2f},-" )

print_line()


print(f"Fuel cost of the gas vehicle is a total of {sum_fuel_cost_gV:.2f},-" )

print_line()


print(f"Insurance and toll costs for the electric vehicle is a total of, {(tolltax_eV_per_km * sum_km) + insurance_eV:.2f},-" )

print_line()


print(f"Insurance and toll costs for the gas vehicle is a total of, {(tolltax_gV_per_km * sum_km) + insurance_gV:.2f},-" )

print_line()

print(f"The total costs for the electrc vehicle for one year ={sum_all_costs_eV_per_year:.2f},-" )

print_line()


print(f"The total costs for the Gas vehcile for one year ={sum_all_costs_gV_per_year:.2f},-" )

#2 streker under svaret :-) 
print_line()
print_line()

# Compares the costs of the two vehicles for the costs
cost_difference = abs(sum_all_costs_gV_per_year - sum_all_costs_eV_per_year)

if sum_all_costs_gV_per_year > sum_all_costs_eV_per_year:
    print(f"The gas vehicle is more expensive by {cost_difference:.2f} NOK per year.")
elif sum_all_costs_eV_per_year > sum_all_costs_gV_per_year:
    print(f"The electric vehicle is more expensive by {cost_difference:.2f} NOK per year.")
else:
    print("Both vehicles have the same annual cost.")

print_line()

# Recommendation based on cost
if sum_all_costs_eV_per_year < sum_all_costs_gV_per_year:
    print("If cost is the most important factor, the electric vehicle is the cheapest option.")
elif sum_all_costs_gV_per_year < sum_all_costs_eV_per_year:
    print("If cost is the most important factor, the gas vehicle is the cheapest option.")
else:
    print("Both vehicles cost the same, so choose based on other factors.")

print_line()
print_line()



"""

Notes from oblig 1:

Lag et Python-program som beregner og presenterer (i konsollen) de årlige totalkostnadene for elbil og for bensinbil samt årlig kostnadsdifferanse basert på informasjonen gitt nedenfor. Du kan her for enkelhets skyld se bort fra kostnader som renter på billån og verditap (du har da egentlig antatt at slike kostnader er like for elbil og bensinbil).

Nedenfor er informasjon som programmet skal baseres på (som selvsagt kan diskuteres, men ikke ifm. denne oppgaven :-)

Du kan selv velge antall kjørte km/år ut fra din typiske bilbruk. Ev. (hvis du ikke har bil) kan du anta 10.000 km.
Forsikring: Elbil: 5000 kr/år. Bensinbil: 7500 kr/år.
Trafikkforsikringsavgift: 8,38 kr/dag for både elbil og bensinbil.
Drivstoffbruk: Elbil: 0,2 kWh/km. Strømpris (antar kun hjemmelading): 2.00 kr/kWh. Bensinbil: 1,0 kr/km.
Bomavgift: Elbil: 0,1 kr/km. Bensinbil: 0,3 kr/km.

"""
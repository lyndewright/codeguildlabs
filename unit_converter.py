#version 1

#mile conversions
km_in_mi = 1.60934
ft_in_mi = 5280
m_in_mi = 1609.34

#kilometer conversions
mi_in_km = .621371
ft_in_km = 3280.84
m_in_km = 1000

#feet conversions
mi_in_ft = .000189394
km_in_ft = .0003048
m_in_ft = .3048

#meter conversions
mi_in_m = .000621371
km_in_m = .09
ft_in_m = 3.28084


print("Welcome to the unit converter.")


distance = float(input("Enter a distance: "))
units = input("Enter units (mi/km/ft/m): ")
target_units = input("Enter target units (mi/km/ft/m): ")


while True:
    if units == 'mi' and target_units == 'km':
        mi_to_km = distance * km_in_mi
        print(str(mi_to_km) + " km")
    elif units == 'mi' and target_units == 'ft':
        mi_to_ft = distance * ft_in_mi
        print(str(mi_to_km) + " ft")
    elif units == 'mi' and target_units == 'm':
        mi_to_m = distance * m_in_mi
        print(str(mi_to_m) + " m")
    elif units == 'km' and target_units == 'mi':
        km_to_mi = distance * mi_in_km
        print(str(km_to_mi) + " mi")
    elif units == 'km' and target_units == 'ft':
        km_to_ft = distance * ft_in_km
        print(str(km_to_ft) + " ft")
    elif units == 'km' and target_units == 'm':
        km_to_m = distance * mi_in_km
        print(str(km_to_m) + " m")
    elif units == 'ft' and target_units == 'mi':
        ft_to_mi = distance * mi_in_ft
        print(str(ft_to_mi) + " mi")
    elif units == 'ft' and target_units == 'km':
        ft_to_km = distance * km_in_ft
        print(str(ft_to_km) + " km")
    elif units == 'ft' and target_units == 'm':
        ft_to_m = distance * mi_in_ft
        print(str(ft_to_km) + " m")
    elif units == 'm' and target_units == 'mi':
        m_to_mi = distance * mi_in_m
        print(str(m_to_mi) + " mi")
    elif units == 'm' and target_units == 'km':
        m_to_km = distance * km_in_m
        print(str(m_to_km) + " km")
    elif units == 'm' and target_units == 'ft':
        m_to_ft = distance * ft_in_m
        print(str(m_to_ft) + " ft")
    else:
        print("I'm sorry, I didn't understand.")

    quit()

def is_year_leap(year):
    if year < 1582:
	    print("No esta dentro del período del calendario Gregoriano")
    else:
    	if year % 4 != 0:
    		print("Año Común")
    		return False
    	elif year % 100 != 0:
    		print("Año Bisiesto")
    		return True
    	elif year % 400 != 0:
    		print("Año Común")
    		return False 
    	else:
    		print("Año Bisiesto")
    		return True 

def days_in_month(year, month):
    if month in [1, 3, 5, 7, 8, 10, 12]:
        days=31
        return days
    elif month in [4,6,9,11]:
        days=30
        return days
    elif(month==2):
        leap=is_year_leap(year)
        if leap:
            days=29
            return days
        else:
            days=28
            return days
    elif(month==8):
        days=31
        return days
    #
    # Escribe tu código nuevo aquí.
    #

test_years = [1900, 2000, 2016, 1987]
test_months = [2, 2, 1, 11]
test_results = [28, 29, 31, 30]
for i in range(len(test_years)):
    yr = test_years[i]
    mo = test_months[i]
    print(yr, mo, "->", end="")
    result = days_in_month(yr, mo)
    if result == test_results[i]:
        print("OK")
    else:
        print("Fallido")
        print(result)

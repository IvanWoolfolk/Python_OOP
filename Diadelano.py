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

def day_of_year(year, month, day):
        for i in range(1,month):
                day+=days_in_month(year, month)
        return day
    #
    # Escribe tu código nuevo aquí.
    #

print(day_of_year(2000, 12, 31))
print(day_of_year(2021, 2, 1))

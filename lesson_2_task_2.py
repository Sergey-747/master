def is_year_leap(year):
    if year % 4 == 0:
        return True
    else:
        return False

year = int(input("Введите год на проверку: "))
print("год:", year, is_year_leap(year) )

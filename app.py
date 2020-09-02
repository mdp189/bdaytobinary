def dec_to_bin(x):
    return int(bin(x)[2:])


birthday_month = int(input("What month is your birthday in? (MM) "))
birthday_day = int(input("What is the day of your birthday? (DD) "))
birthday_year = int(input("What year is your birthday in? (YY) "))
binary_dates = f"{dec_to_bin(birthday_month):04} {dec_to_bin(birthday_day):04} {dec_to_bin(birthday_year):04}"
print(f"your birthday in binary is {binary_dates}")
s1 = binary_dates.replace('0', 'W')
s2 = s1.replace('1', 'B')
s3 = s2.replace(' ', 'RR')
print(s3)

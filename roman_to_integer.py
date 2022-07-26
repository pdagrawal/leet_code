def roman_to_integer(roman):
    roman_numbers = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
    total = 0
    for i in range(len(roman)-1, -1, -1):
        num = roman_numbers[roman[i]]
        if 3*num < total:
            total -= num
        else:
            total += num
    return total


print(roman_to_integer('IV'))
print(roman_to_integer('IX'))
print(roman_to_integer('LVIII'))
print(roman_to_integer('MCMXCIV'))

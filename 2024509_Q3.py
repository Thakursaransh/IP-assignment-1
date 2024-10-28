def units_to_text(units):
    if units == 0:
        return "zero"
    elif units == 1:
        return "one"
    elif units == 2:
        return "two"
    elif units == 3:
        return "three"
    elif units == 4:
        return "four"
    elif units == 5:
        return "five"
    elif units == 6:
        return "six"
    elif units == 7:
        return "seven"
    elif units == 8:
        return "eight"
    elif units == 9:
        return "nine"

def tens_to_text(tens):
    if tens == 10:
        return "ten"
    elif tens == 20:
        return "twenty"
    elif tens == 30:
        return "thirty"
    elif tens == 40:
        return "forty"
    elif tens == 50:
        return "fifty"
    elif tens == 60:
        return "sixty"
    elif tens == 70:
        return "seventy"
    elif tens == 80:
        return "eighty"
    elif tens == 90:
        return "ninety"

def number_to_text(number):
    if 10 <= number <= 19:
        special_cases = {
            10: "ten", 11: "eleven", 12: "twelve", 13: "thirteen", 14: "fourteen",
            15: "fifteen", 16: "sixteen", 17: "seventeen", 18: "eighteen", 19: "nineteen"
        }
        return special_cases[number]    
    units = number % 10
    tens = number - units
    if number < 10:
        return units_to_text(number)
    else:
        if units == 0:
            return tens_to_text(tens)
        else:
            return tens_to_text(tens) + " " + units_to_text(units)
def _test():
    assert number_to_text(9) == "nine"
    assert number_to_text(29) == "twenty nine"    
num = int(input("Enter a number between 0 and 99: "))
print(number_to_text(num))
_test()

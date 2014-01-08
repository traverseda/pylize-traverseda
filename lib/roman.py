"""Convert from/to decimal to/from Roman numerals."""


def roman2dec(roman_string):
    import string

    s = string.lower(roman_string)
    exp = ""
    s = string.replace(s, 'iv', "+4")
    s = string.replace(s, 'ix', "+9")
    s = string.replace(s, 'xl', "+40")
    s = string.replace(s, 'xc', "+90")
    s = string.replace(s, 'cd', "+400")
    s = string.replace(s, 'cm', "+900")
    s = string.replace(s, 'i', "+1")
    s = string.replace(s, 'v', "+5")
    s = string.replace(s, 'x', "+10")
    s = string.replace(s, 'l', "+50")
    s = string.replace(s, 'c', "+100")
    s = string.replace(s, 'd', "+500")
    s = string.replace(s, 'm', "+1000")
    exec "num = " + s
    return num
    
 
def dec2roman(base10_integer):
    """Translated from a public domain C routine by Jim Walsh in the
    Snippets collection.
    """

    n, base10_integer = divmod(base10_integer, 1000)
    roman = "M"*n
    if base10_integer >= 900:
        roman = roman + "CM"
        base10_integer = base10_integer - 900
    while base10_integer >= 500:
        roman = roman + "D"
        base10_integer = base10_integer - 500
    if base10_integer >= 400:
        roman = roman + "CD"
        base10_integer = base10_integer - 400
    while base10_integer >= 100:
        roman = roman + "C"
        base10_integer = base10_integer - 100
    if base10_integer >= 90:
        roman = roman + "XC"
        base10_integer = base10_integer - 90
    while base10_integer >= 50:
        roman = roman + "L"
        base10_integer = base10_integer - 50
    if base10_integer >= 40:
        roman = roman + "XL"
        base10_integer = base10_integer - 40
    while base10_integer >= 10:
        roman = roman + "X"
        base10_integer = base10_integer - 10
    if base10_integer >= 9:
        roman = roman + "IX"
        base10_integer = base10_integer - 9
    while base10_integer >= 5:
        roman = roman + "V"
        base10_integer = base10_integer - 5
    if base10_integer >= 4:
        roman = roman + "IV"
        base10_integer = base10_integer - 4
    while base10_integer > 0:
        roman = roman + "I"
        base10_integer = base10_integer - 1
    return roman


if __name__ == "__main__":
    """We'll test the conversion routines by converting from a decimal
    integer n to a Roman numeral and then back again.  If the operations
    are not the identity transformation, it's an error.
    """

    largest_number = 5000
    for num in xrange(1,largest_number+1):
        s = dec2roman(num)
        number = roman2dec(s)
        if number != num:
            print "Routines failed for", num
            raise "Test failure"
    print "Test passed."

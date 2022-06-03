roman_num = {
    'M': 1000,
    'D': 500,
    'C': 100,
    'L': 50,
    'X': 10,
    'V': 5,
    'I': 1
}
def convertRoman_number(roman_number):
    temp_roman_num = list(roman_number)
    demical_num = []
    for v in temp_roman_num:
        demical_num.append(roman_num[v])
    for i in range(len(demical_num) - 1):
        if demical_num[i] < demical_num[i+1]:
            demical_num[i] = - demical_num[i]
    return sum(demical_num)
print(convertRoman_number("XLIII"))

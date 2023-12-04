def roman_to_int(roman):
    roman_numerals = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    result = 0

    for i in range(len(roman)):
        """ 
            ถ้า i น้อยกว่า length ของ และ dictionary roman_numerals[key n]
            น้อยกว่า dictionary roman_numerals[key n+1] 
        
        """
        condition = (
                
                i < len(roman) - 1 and
                roman_numerals[roman[i]] < roman_numerals[roman[i + 1]] 

                )        
        
        # 
        if condition:
            result -= roman_numerals[roman[i]]
        else:
            result += roman_numerals[roman[i]]

    return result

roman_num = roman_to_int(input())
print(roman_num)

class Solution:
    def myAtoi(self, s: str) -> int:
        # Initialize variables
        i = 0
        n = len(s)
        sign = 1
        result = 0
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31
        
        # Ignore leading whitespace
        while i < n and s[i] == ' ':
            i += 1
        
        # Check if the next character is '-' or '+'
        if i < n and (s[i] == '-' or s[i] == '+'):
            if s[i] == '-':
                sign = -1
            i += 1
        
        # Convt the digits into an integer
        while i < n and s[i].isdigit():
            digit = int(s[i])
            
            # Check for overflow/underflow before adding the digit
            if result > (INT_MAX - digit) // 10:
                return INT_MAX if sign == 1 else INT_MIN
            
            result = result * 10 + digit
            i += 1
        
        # Apply the sign and return the result
        return sign * result

"""
Given two integers representing the numerator and denominator of a fraction, return the fraction in string format.
If the fractional part is repeating, enclose the repeating part in parentheses.
Example 1:
Input: numerator = 1, denominator = 2
Output: "0.5"
Example 2:
Input: numerator = 2, denominator = 1
Output: "2"
Example 3:
Input: numerator = 2, denominator = 3
Output: "0.(6)"
"""

class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        num, den = numerator, denominator
        if not den:
            return 0
        if not num:
            return "0"
            
        res = []
        if (num < 0) ^ (den < 0):
            res.append("-")
        num, den = abs(num), abs(den)
        res.append(str(num//den))
        rmd = num % den

        if not rmd:
            return "".join(res)
        res.append(".")
        dic = {}
        while rmd:
            if rmd in dic:
                res.insert(dic[rmd], "(")
                res.append(")")
                break
            dic[rmd] = len(res)
            div,rmd = divmod(rmd*10, den)
            res.append(str(div))
        return "".join(res)

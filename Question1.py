def numberToWords(num: int) -> str:
    if num == 0:
        return "Zero"

    below_20 = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
    tens = ["", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
    thousands = ["", "Thousand", "Million", "Billion", "Trillion"]

    def helper(n):
        if n == 0:
            return ""
        elif n < 20:
            return below_20[n] + " "
        elif n < 100:
            return tens[n // 10] + " " + helper(n % 10)
        else:
            return below_20[n // 100] + " Hundred " + helper(n % 100)

    negative = num < 0
    num = abs(num)

    res = ""
    group = 0
    while num > 0:
        if num % 1000 != 0:
            res = helper(num % 1000) + thousands[group] + " " + res
        num //= 1000
        group += 1

    result = res.strip()
    result = " ".join(result.split())

    if negative:
        result = "Negative " + result

    return result

#Examlpes:
if __name__ == "__main__":
    print(numberToWords(123))
    print(numberToWords(12345))
    print(numberToWords(-45))
    print(numberToWords(0))
import sys

MAX_NUMBER = 100000

def convert_to_words(num):
    english = {
        0: "",
        1: "one",
        2: "two",
        3: "three",
        4: "four",
        5: "five",
        6: "six",
        7: "seven",
        8: "eight",
        9: "nine",
        10: "ten",
        11: "eleven",
        12: "twelve",
        13: "thirteen",
        14: "fourteen",
        15: "fifteen",
        16: "sixteen",
        17: "seventeen",
        18: "eighteen",
        19: "nineteen",
        20: "twenty",
        30: "thirty",
        40: "forty",
        50: "fifty",
        60: "sixty",
        70: "seventy",
        80: "eighty",
        90: "ninety"
    }
    mappings = english;
    if num == 0:
        return mappings[0]

    def convert_three_digits(n):
        if n >= 100:
            return mappings[n // 100] + " hundred" + (" and " + convert_three_digits(n % 100) if n % 100 > 0 else "")
        elif n >= 20 or n == 10:
            return mappings[n // 10 * 10] + ("-" + mappings[n % 10] if n % 10 > 0 else "")
        else:
            return mappings[n]

    def check_delimiter(num_part):
        return (", " if (num_part > 100) else " and " if num_part > 0 else "")

    group_nouns = ["", " thousand", " million"]
    result = ""
    index = 0;
    while num > 0:
        result = (check_delimiter(num % 1000) if (num // 1000 > 0) else "") + \
                 convert_three_digits(num % 1000) + group_nouns[index] + result
        index = index + 1
        num = num // 1000
    return result

def main():
    validate_input()

    number = int(sys.argv[1])
    result = convert_to_words(number)
    print(result)

def validate_input():
    if len(sys.argv) < 2 or not sys.argv[1].isdigit():
        print("Invalid or missing argument.")
        sys.exit(1)
    input_value = sys.argv[1]
    if int(input_value) > MAX_NUMBER or int(input_value) < 0:
        print("Invalid number provided. The value must be withing the range of 0 to 100000.")
        sys.exit(2)

if __name__ == "__main__":
    main()

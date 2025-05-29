dict = {
    "0" : "zero",
    "1" : "one",
    "2" : "two",
    "3" : "three",
    "4" : "four",
    "5" : "five",
    "6" : "six",
    "7" : "seven",
    "8" : "eight",
    "9" : "nine",
    "a" : "ten",
    "b" : "eleven",
    "c" : "twelve",
    "d" : "thirteen",
    "e" : "fourteen",
    "f" : "fifteen",
    }


def convert_num(num):
    return dict.get(num, "")

max_num = None
valid_num = []
with open('TextFile1.txt', 'r' ) as file:
    for line in file.readlines():
        for number in line.split():
             if len(number) <= 5:
                valid_num.append(number)

for possible_max in valid_num:
    if not max_num or int(possible_max, 16) > int(max_num, 16):
        max_num = possible_max

num_in_words = " ".join(convert_num(i) for i in max_num)
print(num_in_words)
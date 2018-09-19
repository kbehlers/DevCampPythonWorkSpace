hist_dict = {
    "g": 12,
    "f": 20,
    "t":8,
    "o":10
}

for key, value in hist_dict.items():
    print(key + " " + ("$"*int(value)))
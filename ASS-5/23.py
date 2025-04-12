def count_char_frequency(s):
    freq_dict = {}
    for char in s:
        if char in freq_dict:
            freq_dict[char] += 1
        else:
            freq_dict[char] = 1
    return freq_dict
input_string = str(input("Enter string: "))
result = count_char_frequency(input_string)
print(result)
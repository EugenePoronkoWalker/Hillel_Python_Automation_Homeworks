base_dict = {'contry':'Ukraine', 'continent': 'Europe', 'size': 123}
add_dict = {"a":1, "b":2, "c":2, "d":3, 'size': 12}

# task 6. Об'єднайте два словника base_dict та add_dict  в новий словник sum_dict
# Якщо ключі збігаються, то об'єднайте (str) або додайте їх значення (int)

sum_dict = {}
sum_dict.update(base_dict)

for key, value in add_dict.items():
    if key in sum_dict:
        value += sum_dict[key]
    sum_dict.update({key:value})
print("Dictionary with merged two dictionaries and sum of values of the matching key:", sum_dict)


###################################
for key, value in add_dict.items():
    if key in sum_dict:
        if (type(value)==int) and (type(sum_dict[key])==int):
            value += int(sum_dict[key])
        else:
            value = str(sum_dict[key]) + str(value)
    sum_dict.update({key:value})
print("Dictionary with merged two dictionaries and sum of values of the matching key:", sum_dict)

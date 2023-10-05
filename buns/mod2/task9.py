stroke = input("Введите строку: ")
vowel_list = "аеёиоуыэюяАЕЁИОУЫЭЮЯ"
consonant_list = "бвгджзйклмнпрстфхцчшщБВГДЖЗЙКЛМНПРСТФХЦЧШЩ"
vowel_count = 0
consonant_count = 0
for i in range(len(stroke)):
    if stroke[i] in vowel_list:
        vowel_count += 1
    elif stroke[i] in consonant_list:
        consonant_count += 1
    else:
        continue
print(vowel_count, consonant_count)

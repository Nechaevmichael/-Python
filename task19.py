# Задайте список. Напишите программу, которая определит, присутствует ли в заданном списке строк некое число.
# ['ssss', 'sngujn556', 56] -> Yes
# ['56', 'sgnbsb'] -> No

sp = ['ssss', 'sngujn556', 56]
result = False
for item in sp:
    try:
        item.isdigit()
    except:
        result = True
if result == True:
    print(f'{sp} -> Yes')
else:
    print(f'{sp} -> No')
# Напишите программу, удаляющую из текста все слова, содержащие "абв".
# *' 'абвгд гдежз жзе абв ыопыпт' -> ' гдежз жзе ыопыпт'

string = 'абвгд гдежз жзе абв ыопыпт'
string = string.split()

# result = []
# for i in range(len(string)):
#     if 'абв' not in string[i]:
#         result.append(string[i])
# print(result)

result = [i for i in string if "абв" not in i]
print(result)
'''Домашнє завдання:
5. Напишіть програму, яка переводить ціле число з римського запису до десяткового.
Наприклад: XXII -> 22
'''

# 1.1. Використовуючи словник, напишіть програму, яка виведе на екран назву дня тижня за номером.
# Наприклад, 1 - "Monday".
week = {1:"Monday", 2:"Tuesday", 3:"Wednesday", 4:"Thursday", 5:"Friday", 6:"Saturday", 7:"Sunday"}
dey_num = int(input("Enter week day number"))
print(week[dey_num] if 0 < dey_num < 8 else "Entered number out of range" )
# 2. Опишіть кота (домашня тварина) на основі словника.
cat = {"tail":1, "paw":["claw1","claw2","claw3","claw4"], "body":1, "color":"black",
       "head":{"ear":2, "eye":2, "nose":1, "mouth":1, "whisker":6}
       }
print(cat)
# 3. Напишіть програму, яка читає рядок тексту з клавіатури і виводить на екран статистику, скільки разів яка літера зустрічається в цьому рядку.
# Наприклад, для рядка «Hello world» ця статистика виглядає так: «H» - 1, «e» - 1, «l» - 3 і т.д.
text = "Hello world"
dict_ = {}
for i in text:
    dict_[i] = text.count(i)
print(dict_)
# 4.4. Ввести з клавіатури число, що означає кількість доларів і центів. Вивести цю кількість прописом.
# Наприклад:
# How much money do you have?
# 123,34
# You have: one hundred twenty three dollars thirty four cents
user_num = float(input("How much money do you have?"))
words = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten',
 11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen', 15: 'fifteen', 16: 'sixteen',
 17: 'seventeen', 18: 'eighteen', 19: 'nineteen', 20: 'twenty', 30: 'thirty', 40: 'forty', 50: 'fifty',
 60: 'sixty', 70: 'seventy', 80: 'eighty', 90: 'ninety', 100: 'hundred', 1000: 'thousand'}
result = ''
ones = user_num % 10
tens = user_num - ones
hundreds = user_num // 100
thousands = user_num // 1000
if 10 <= user_num < 20:
    result = words[user_num]
elif user_num < 100:
    result = words[tens] + ' ' + words[ones]
# elif user_num < 1000:
#     result = words[tens] + ' ' + words[ones]
# elif user_num < 1_000_000:
print(result)
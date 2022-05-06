# without list comprehensions
# final = []
# for number in list:
#     if number >= 10:
#         final.append(number)
#
# print(final)

list = [2,4,5,10,23,190]
final = [number for number in list if number >= 10]
print(final)
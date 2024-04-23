a, b = 50, 6
if a > b:
    print('a > b')
if a > b and a > 0:
    print('gud')
if (a > b) and (a > 0 or b < 1000):
    print('gud')
if 3 < b and b < 10:
    print('gud')
if '76'>'568':
    print('ok')
if '234'>'23':
    print('OK')
if [1,2] > [1,1]:
    print('Ok')
# a = 5
# if a == 5 and (a > 1 or a < 10):# сравнение разных типов данных не возможно
#     print( 'Ok')
# if '234'>23
# if [4,5] > 23
if '234' != 23:
    print('!')

yesterday_temp = int(input('Введите какая была вчера температура на улице?:'))
today_temp = int(input('Введите какая температура на улице сегодня?:' ))
if today_temp > yesterday_temp:
    print("Сегодня теплее, чем вчера.")
elif today_temp < yesterday_temp:
    print("Сегодня холоднее, чем вчера.")
else:
    print("Сегодня такая же температура, как вчера.")


# age = int (input('Сколько Вам лет? _'))# input запрос данных у пользователя с клавиатуры
# if age >= 18:
#     print('Ok')
# if age < 18:
#     print('No')
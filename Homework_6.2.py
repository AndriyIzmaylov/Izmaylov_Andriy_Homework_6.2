# Ваше завдання — написати програму, яка переводить число у формат часу у читальному вигляді.
#
# Користувач повинен ввести число більше або дорівнює 0 і менше ніж 8640000.
#
# Число, яке є кількістю секунд, необхідно перевести в дні, години, хвилини та секунди.
#
# Ну і додатковим завданням є турбота про виведення.
#
# Слово "день" підбирається на основі кількості днів, а години, хвилини, і секунди повинні заповнюватися
# нулями при одноцифрових значеннях.
#
# Підказка: одна хвилина - 60 сек. , В одній годині 60 * 60 сек, в одній добі 24 * 60 * 60 сек.
# Тобто використовуючи функцію divmod або методи поділу // і % вам необхідно знайти відповідну кількість днів,
# годин, хвилин, а те що залишиться - це секунди, які меньше 60 ;)
#
# Доповнити провідними нулями можна за допомогою методу zfill(2)
#
# Приклад:
# 0 -> 0 днів, 00:00:00
# 224930 -> 2 дні, 14:28:50
# 466289 -> 5 днів, 09:31:29
# 950400 -> 11 днів, 00:00:00
# 1209600 -> 14 днів, 00:00:00
# 1900800 - > 22 дні, 00:00:00
# 8639999 -> 99 днів, 23:59:59
# 22493 -> 0 днів, 06:14:53
# 7948799 -> 91 день, 23:59:59
def format_time(seconds):
    day_in_seconds = 24 * 60 * 60
    hour_in_seconds = 60 * 60
    minute_in_seconds = 60

    days, seconds = divmod(seconds, day_in_seconds)
    hours, seconds = divmod(seconds, hour_in_seconds)
    minutes, seconds = divmod(seconds, minute_in_seconds)

    if days % 10 == 1 and days % 100 != 11:
        plural_of_the_word = "день"
    elif 2 <= days % 10 <= 4 and (days % 100 < 10 or days % 100 >= 20):
        plural_of_the_word = "дні"
    else:
        plural_of_the_word = "днів"

    return f"{days} {plural_of_the_word}, {str(hours).zfill(2)}:{str(minutes).zfill(2)}:{str(seconds).zfill(2)}"


while True:
    try:
        input_seconds = int(input("Enter the number of seconds (from 0 to 8640000): "))
        if 0 <= input_seconds < 8640000:
            result = format_time(input_seconds)
            print(result)
            break
        else:
            print("Invalid number entered. Must be between 0 and 8640000.")
    except ValueError:
        print("Error: The entered number is not a number. Please enter a correct number.")

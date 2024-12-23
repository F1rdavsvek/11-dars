# 1
# async def remove_digits(password):
#     i = 0
#     result = ""
#     while i < len(password):
#         if not password[i].isdigit():
#             result += password[i]
#         i += 1
#     return result
#
# import asyncio
#
# result = asyncio.run(remove_digits("pass123word456"))
# print(result)

# ------------------------------------
# 2
# async def output_first_10_chars(text):
#     i = 0
#     result = ""
#     while i < len(text) and i < 10:
#         result += text[i]
#         i += 1
#     return result
#
# import asyncio
#
# result = asyncio.run(output_first_10_chars("ThisIsALongSentence"))
# print(result)

# ------------------------------------
# 3
# async def clean_digits_from_name(name):
#     i = 0
#     cleaned_name = ""
#     while i < len(name):
#         if not name[i].isdigit():
#             cleaned_name += name[i]
#         i += 1
#     return cleaned_name
#
# import asyncio
#
# result = asyncio.run(clean_digits_from_name("John123Doe456"))
# print(result)

# ----------------------------------------------
# 4
# async def to_lower_and_remove_spaces(text):
#     i = 0
#     result = ""
#     while i < len(text):
#         if text[i] != " ":
#             result += text[i].lower()
#         i += 1
#     return result
#
# import asyncio
#
# result = asyncio.run(to_lower_and_remove_spaces("Hello World! Welcome"))
# print(result)

# ---------------------------------------------
# 5
# async def extract_vowels(text):
#     vowels = "aeiouAEIOU"
#     i = 0
#     result = ""
#     while i < len(text):
#         if text[i] in vowels:
#             result += text[i]
#         i += 1
#     return result
#
# import asyncio
#
# result = asyncio.run(extract_vowels("Educational"))
# print(result)

# ---------------------------------
# 6
# async def replace_ab(sequence):
#     i = 0
#     result = ""
#     while i < len(sequence):
#         if i < len(sequence) - 1 and sequence[i] == "a" and sequence[i + 1] == "b":
#             result += "#"
#             i += 2
#         else:
#             result += sequence[i]
#             i += 1
#     return result
#
# import asyncio
#
# result = asyncio.run(replace_ab("cabdab"))
# print(result)

# --------------------------------
# 7
# async def is_palindrome(text):
#     cleaned_text = "".join(c.lower() for c in text if c.isalnum())
#     return cleaned_text == cleaned_text[::-1]
#
# import asyncio
#
# result = asyncio.run(is_palindrome("A man, a plan, a canal: Panama"))
# print(result)

# -------------------------------
# 8
# async def reverse_number(number):
#     reversed_num = int(str(abs(number))[::-1])
#     return reversed_num if number >= 0 else -reversed_num
#
# import asyncio
#
# result = asyncio.run(reverse_number(-12345))
# print(result)

# ----------------------------------
# 9
# async def sort_letters_in_word(word):
#     sorted_word = ''.join(sorted(word))
#     return sorted_word
#
# import asyncio
#
# result = asyncio.run(sort_letters_in_word("pycharm"))
# print(result)

# ---------------------------------
# 10
# async def find_max_in_list(numbers):
#     if not numbers:
#         return None
#     max_number = numbers[0]
#     for num in numbers:
#         if num > max_number:
#             max_number = num
#     return max_number
#
# import asyncio
#
# result = asyncio.run(find_max_in_list([3, 7, 2, 9, 5]))
# print(result)

# ------------------------------------
# 11
# async def calculate_factorial(n):
#     if n < 0:
#         return "Faktorial faqat musbat sonlar uchun aniqlangan."
#     factorial = 1
#     for i in range(1, n + 1):
#         factorial *= i
#     return factorial
#
# import asyncio
#
# result = asyncio.run(calculate_factorial(5))
# print(result)

# ------------------------------------------
# 12
# import aiohttp
# import asyncio
# import time
# from colorama import Fore, Style
#
# API_KEY = "e9b44ae0381135b11a5911d3cb3d44a9"
# BASE_URL = "http://api.openweathermap.org/data/2.5/weather"
#
# VALID_CITIES = ["Fargona", "Tashkent", "London", "New York", "Paris"]
#
# async def get_weather(city_name):
#     async with aiohttp.ClientSession() as session:
#         try:
#             params = {
#                 "q": city_name,
#                 "appid": API_KEY,
#                 "units": "metric",
#                 "lang": "uz"
#             }
#             async with session.get(BASE_URL, params=params) as response:
#                 if response.status == 200:
#                     data = await response.json()
#                     temp = data["main"]["temp"]
#                     weather = data["weather"][0]["description"]
#                     return f"{Fore.GREEN}Hozir {city_name} shahrida havo harorati: {temp}°C. Havo: {weather}.{Style.RESET_ALL}"
#                 elif response.status == 404:
#                     return f"{Fore.RED}Shahar nomi noto'g'ri kiritildi!!!{Style.RESET_ALL}"
#                 else:
#                     return f"{Fore.RED}Xatolik yuz berdi: {response.status}{Style.RESET_ALL}"
#         except Exception as e:
#             return f"{Fore.RED}Xatolik yuz berdi: {e}{Style.RESET_ALL}"
#
# async def main():
#     print(f"{Fore.CYAN}shahar nomini kiriting. {Fore.YELLOW}(to'xtash uchun 'stop' deb yozing){Style.RESET_ALL}")
#     start_time = time.time()
#
#     while True:
#         city_name = input(f"{Fore.BLUE}Shahar nomini kiriting: {Style.RESET_ALL}")
#         if city_name.lower() == "stop":
#             break
#         elif city_name in VALID_CITIES:
#             result = await get_weather(city_name)
#             print(result)
#         else:
#             print(f"{Fore.RED}Shahar nomi noto'g'ri kiritildi!!!{Style.RESET_ALL}")
#         print("-" * 50)
#
#     end_time = time.time()
#     elapsed_time = end_time - start_time
#     print(f"{Fore.MAGENTA}Dastur to'xtadi!!!{Style.RESET_ALL}")
#     print(f"{Fore.YELLOW}{elapsed_time:.3f} secund vaqt davomida ishladi!!!{Style.RESET_ALL}")
#
# if __name__ == "__main__":
#     asyncio.run(main())




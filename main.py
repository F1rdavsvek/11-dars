# import asyncio
#
# async def generate_numbers():
#     i = 0
#     while i < 10:
#         print(i, "----------")
#
#         i += 1
#         await asyncio.sleep(1)
#
# async def generate_number2():
#     print("Asinxiron ihladi")
#     i = 0
#     while i < 10:
#         print(i, "++")
#         i += 1
#         await asyncio.sleep(0.2)
#
# async def main():
#     await asyncio.gather(generate_numbers(), generate_number2())
#
# asyncio.run(main())

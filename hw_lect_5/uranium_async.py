import asyncio
import time


async def print_temp():
    await asyncio.sleep(2)
    print("Currenttemperatureis120C")


async def print_pressure():
    await asyncio.sleep(3)
    print("Currentpressureis100kPa")


async def print_uranium_level():
    await asyncio.sleep(1)
    print("UraniumlevelisOK")


async def main():
    start_time = float(time.time())
    print("Starting.....")
    temp = asyncio.create_task(print_temp())
    press = asyncio.create_task(print_pressure())
    ura = asyncio.create_task(print_uranium_level())
    await asyncio.gather(temp)
    await asyncio.gather(press)
    await asyncio.gather(ura)
    end_time = float(time.time())
    print(f"На опрос датчиков затрачено {end_time - start_time:.1f} сек.")

"""При решении задачи не понял почему в условии написано, что:
 "список из задач нужно выполнить с помощью asyncio.wait(tasks), в моем случае это создает ошибки,
 либо я что то не правильно понял"""

asyncio.run(main())

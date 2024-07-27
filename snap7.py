import snap7
from snap7.types import *
from snap7.util import *

# Создаем соединение с PLC
plc = snap7.client.Client()
plc.connect('192.168.0.1', 0, 1)

# Читаем данные из DB730, с 0 по 35 байт
db_number = 730
start_address = 0
size_in_bytes = 36

result = plc.db_read(db_number, start_address, size_in_bytes)

# Распаковываем данные
byte_0 = get_int(result, 0)
byte_2_3 = get_int(result, 2)
byte_4_5 = get_int(result, 4)
byte_6_7 = get_int(result, 6)
byte_8_9 = get_int(result, 8)
byte_10_11 = get_int(result, 10)
byte_12_13 = get_int(result, 12)
byte_14_15 = get_int(result, 14)
byte_16_17 = get_int(result, 16)
byte_18_19 = get_int(result, 18)
byte_20_21 = get_int(result, 20)
byte_22_23 = get_int(result, 22)
byte_24_25 = get_int(result, 24)
byte_26_27 = get_int(result, 26)
byte_28_29 = get_int(result, 28)
byte_30_31 = get_int(result, 30)
byte_32_33 = get_int(result, 32)
byte_34_35 = get_int(result, 34)

print(f"Byte 0: {byte_0}")
print(f"Byte 2-3: {byte_2_3}")
print(f"Byte 4-5: {byte_4_5}")
print(f"Byte 6-7: {byte_6_7}")
print(f"Byte 8-9: {byte_8_9}")
print(f"Byte 10-11: {byte_10_11}")
print(f"Byte 12-13: {byte_12_13}")
print(f"Byte 14-15: {byte_14_15}")
print(f"Byte 16-17: {byte_16_17}")
print(f"Byte 18-19: {byte_18_19}")
print(f"Byte 20-21: {byte_20_21}")
print(f"Byte 22-23: {byte_22_23}")
print(f"Byte 24-25: {byte_24_25}")
print(f"Byte 26-27: {byte_26_27}")
print(f"Byte 28-29: {byte_28_29}")
print(f"Byte 30-31: {byte_30_31}")
print(f"Byte 32-33: {byte_32_33}")
print(f"Byte 34-35: {byte_34_35}")

# Отключаемся от PLC
plc.disconnect()
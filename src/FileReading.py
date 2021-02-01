
def Hurapread(file, binary_result):

    for line in file:

        line = line.rstrip('\n')

        # print(line)

        # split by every 8th character
        split_eight = []
        for index in range(0, len(line), 8):
            split_eight.append(line[index: index + 8])

        # print(split_eight)
        binary_result.append(split_eight)

    # print(binary_result)


def convertHex(binary_result, hex_result, key):
    for line in binary_result:
        if line[0][0] != "0" and line[0][0] != "1":
            for elements in line:
                key.append(elements)
        else:
            hex_value = ""
            for byte in line:
                # print(byte)
                # continue
                split_four = []
                for index in range(0, len(byte), 4):
                    split_four.append(byte[index: index + 4])
                # print(split_four)
                for binary_string in split_four:
                    decimal = int(binary_string, 2)
                    # print(decimal)
                    if decimal == 0:
                        hexadecimal = 0
                    else:
                        hexadecimal = hex(decimal).lstrip("0x").rstrip("L")
                    # print(hexadecimal)
                    hex_value += str(hexadecimal).upper()

            # print(hex_value)
            hex_result.append(hex_value)

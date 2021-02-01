def encrypted(file, hex_result, encrypt_result):
    for line in hex_result:
        split_two = []
        for index in range(0, len(line), 2):
            split_two.append(line[index: index + 2])
        # print(split_two)
        line_result = ""
        # print("line_result = " + line_result)
        for keys in split_two:
            # print("keys == "+keys)
            for lines in file:
                splitted = lines.split("\t")
                # print("splitted[1] = "+splitted[1])
                if splitted[1] == keys:
                    line_result += splitted[0]
                    # print(line_result)
            file.seek(0, 0)

        encrypt_result.append(line_result)


def key_decryption(key):
    # print(key)
    string_key = ""

    for elements in key:
        for char in elements:
            if char != "0" and char != "1":
                continue
            else:
                string_key += char

    # print(string_key)

    def twos_comp(val, bits):
        """compute the 2's complement of int value val"""
        if (val & (1 << (bits - 1))) != 0:
            val = val - (1 << bits)
        return val

    return twos_comp(int(string_key, 2), len(string_key))


def decrypted(file, shift_amount, encryption_result, decryption_result):
    # print(shift_amount)
    # print(encryption_result)

    for elements in encryption_result:
        dec_line = ""
        for char in elements:
            char_loc = 0
            line_count = 1
            for lines in file:
                splitted = lines.split("\t")
                # print("splitted[0] = "+splitted[0])
                if splitted[0] == char:
                    char_loc = line_count
                    break
                line_count += 1
            file.seek(0, 0)
            original_loc = (char_loc - shift_amount) % 94

            line_count = 1
            for lines in file:
                splitted = lines.split("\t")
                # print("splitted[0] = "+splitted[0])
                if line_count == original_loc:
                    dec_line += splitted[0]
                line_count += 1
            file.seek(0, 0)
        decryption_result.append(dec_line)

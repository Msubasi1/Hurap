def decrypted_virus(file, shift_amount, encryption_result, decryption_result):
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
            original_loc = (char_loc + shift_amount) % 94

            line_count = 1
            for lines in file:
                splitted = lines.split("\t")
                # print("splitted[0] = "+splitted[0])
                if line_count == original_loc:
                    dec_line += splitted[0]
                line_count += 1
            file.seek(0, 0)
        decryption_result.append(dec_line)


def hexofdecrypted(file, dec_virus_result, hex_virus_result):

    for lines in dec_virus_result:
        hex_lines = ""
        for char in lines:
            for fptr in file:
                splitted = fptr.split("\t")
                if splitted[0] == char:
                    hex_lines += str(splitted[1])
                    break
            file.seek(0, 0)
        hex_virus_result.append(hex_lines)

def binofdecrypted(hex_virus_result, bin_virus_result):

    for line in hex_virus_result:
        line_result = ""
        split_two = []
        for index in range(0, len(line), 2):
            split_two.append(line[index: index + 2])

        for pairs in split_two:
            scale = 16  ## equals to hexadecimal
            num_of_bits = 8
            line_result += str(bin(int(pairs, scale))[2:].zfill(num_of_bits))

        bin_virus_result.append(line_result)
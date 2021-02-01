
def convertVirus(file, original, changed):

    for index in range(0, len(original)):
        temp = original[index]
        for elements in file:
            splitted = elements.split(":")
            if splitted[0] in original[index]:
                # changed.append(splitted[1])
                change = temp.replace(splitted[0].rstrip('\n'), splitted[1].rstrip('\n'))
                change = change.rstrip('\n')
                temp = change
                changed[index] = change
        file.seek(0, 0)

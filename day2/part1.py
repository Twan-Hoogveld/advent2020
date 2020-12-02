with open('inputFile') as f:
    valid = 0
    for line in f:
        parts = line.split(':')

        #Formatting
        parts[1] = parts[1][1:]
        mi = parts[0].split('-')
        ma, sym = mi[1].split(" ")
        mi = mi[0]
        password = parts[1]

        found = 0
        for letter in password:
            if letter == sym:
                found += 1
        if not found < int(mi) and not found > int(ma):
            valid += 1
print(valid)
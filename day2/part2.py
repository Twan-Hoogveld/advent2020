#Index 0 is a lie. It's 1 now.
#1 of 2 indexes must be correct, the other one not. XOR.

with open('inputFile') as f:
    valid = 0
    for line in f:
        parts = line.split(':')

        #Formatting
        parts[1] = parts[1][1:]
        low_index = parts[0].split('-')
        max_index, sym = low_index[1].split(" ")
        max_index = int(max_index)
        low_index = int(low_index[0])
        password = parts[1]

        for _ in password:

            if password[low_index - 1] == sym:
                if password[max_index - 1] != sym:
                    valid += 1
                    break

            if password[max_index - 1] == sym:
                if password[low_index - 1] != sym:
                    valid += 1
                    break
            break

print(valid)
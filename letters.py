def find_missing_letters(letters):

    for i in range(1, len(letters)):
       if ord(letters[i]) - ord(letters[i - 1]) != 1:
            return chr(ord(letters[i - 1]) + 1)

print(find_missing_letters(["A", "B", "C", "E", "F"]))
print(find_missing_letters(["а", "б", "в", "д", "е"]))


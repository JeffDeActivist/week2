a = [1, 2, 34, 66, 373, 4838, 3972, 3937, 937, 4834, 4839, 3838, 3724, 3526]
print(a.sort(reverse=False))
print(sorted(a, reverse=True))
# upper and lower()
b = "SmaLlLetter"
print(b.lower())  # returns string in small caps
print(b.upper())  # returns string in big caps
print(b.title())  # capitalizes first letter
print(b.count('a'))  # counts occurrences of a
print(b.count('l'))  # counts occurences of l...keep in mind that l is different from L
print(b.index('a'))  # returns index of a
print(b.capitalize())  # has capitalized first letter


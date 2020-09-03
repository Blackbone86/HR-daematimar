# Read exactly four lines of input
line1 = 'Jckn."Ecguct#'
line2 = 'Dg"tgcf{"hqt"cvvcem'
line3 = 'Fqp)v"ngv"vjg"gpgo{"ugg"{qw'
line4 = 'Ocmg"uwtg"Dtwvwu"uvc{u"swkgv'

# Define variables for the range of numbers within which we have 'printable' characters.
# As we shift the input characters, we must ensure that they stay within this range.
LOW = ord(" ")  # 32
HIGH = ord("~")  # 126



# Every transmission starts with the line "Hail Caesar!" so the first letter,
# once decrypted, must be H.
first_letter = line1[0]
# ...now find out what the key is
shift_number = ord(first_letter) - ord("H")


# We can use 'for' to iterate over the lines and decrypt them one by one
for line in (line1, line2, line3, line4):
    for character in line:
        print_char = chr(ord(character) -shift_number)
        print(print_char, end='')
    print()

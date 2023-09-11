def base_convert(ibase, obase, ival, precision = 64):
    '''
    Convert input value from input base to output base with fractional precision
    '''

    valid_digits = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    ival = ival.upper()

    # Split input value into input integer and fractional parts
    parts = ival.split('.') + ['']
    int_part, frac_part = parts[:2]
    if int_part == '':
        int_part = '0'

    # Get base 10 integer part value from input value
    '''
    int_val = 0
    for digit in int_part:
        int_val *= ibase
        int_val += digits.index(digit)
    '''

    # Use Python built-in 'int' function instead
    int_val = int(int_part, ibase)

    # Get base 10 fractional part from input value
    frac_val = 0
    for digit in frac_part[::-1]:
        frac_val += valid_digits.index(digit)
        frac_val /= ibase

    # Get output value from base 10 integer value
    int_oval = ''
    if int_val == 0:
        int_oval = '0'
    while int_val > 0:
        int_oval = valid_digits[int_val % obase] + int_oval
        int_val //= obase

    # Get output value from base 10 fractional value
    frac_oval = ''
    while frac_val > 0 and len(frac_oval) < precision:
        frac_oval += valid_digits[int(frac_val * obase)]
        frac_val = frac_val * obase % 1

    # Join output integer and fractional parts into output value
    oval = int_oval
    if frac_oval != '':
        oval += '.' + frac_oval

    # Return output value
    return oval

print(base_convert(10, 16, '48879.7458343505859375'))
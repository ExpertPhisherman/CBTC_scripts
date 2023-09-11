def cat_string(seq):
    for i in seq:
        print(i + "\t\U00002620")

cat_string(['hello', 'world', 'abcdefg'])
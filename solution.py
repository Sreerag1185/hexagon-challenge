def print_hex(row,columns):
    print(" ",end="")
    col = int((columns + 1)/2)
    print("     ".join(["___" for _ in range(col)]))
    first = True
    end1="\n"
    end2 = "\\\n"
    for r in range(row):
        if r == (row-1) and not first:
            end2 = "\n"
        if columns % 2 == 0:
            print("".join(["/   \\___" for _ in range(col)]),end=end1)
            print("".join(["\\___/   " for _ in range(col)]),end=end2)
        else:
            print("___".join(["/   \\" for _ in range(col)]))
            print("   ".join(["\\___/" for _ in range(col)]))
        if first:
            first = False
            end1 = "/\n"
    if row == 1:
        print("    ",end="")
        if columns % 2 == 0:
            print("   ".join(["\___/" for _ in range(col)]))
        else:
            print("   ".join(["\___/" for _ in range(col-1)]))

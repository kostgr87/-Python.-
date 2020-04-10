for i in range(31, 128):
    print("%4d-%s" % (i, chr(i)), end='')
    if i % 10 == 0:
        print()

print()


""" def file_read(fname):
    txt = open(fname)
    print(txt.read())
file_read("files/text.txt") """

def file_read_from_head(fname, nlines):
        from itertools import islice
        with open(fname) as f:
                for line in islice(f, nlines):
                        print(line)
file_read_from_head('files/text.txt',2)
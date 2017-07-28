import os


import csv
hs = {}
files = [f for f in os.listdir ('.') if os.path.isfile (f)]
for fname in files:
    # print (fname)
    filename = fname.split ('.')
    if filename[1] == 'csv':
        count = count + 1
        with open (fname, newline='') as f:
            reader = csv.reader (f)
            countOfRowNumber = 0
            for row in reader:
                countOfRowNumber += 1

                for each in row:
                    if each != '':
                        if each == 'Onions':
                            # print (each)
                            print (fname)
                print ('---------')

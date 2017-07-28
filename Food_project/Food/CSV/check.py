import csv
import os
import operator
# def showLocal():
#     files = [f for f in os.listdir ('.') if os.path.isfile (f)]
#     for f in files:
#         print (f)

def readAllFiles():
    count = 0
    files = [f for f in os.listdir ('.') if os.path.isfile (f)]
    for fname in files:
        # print (fname)
        filename = fname.split('.')
        if filename[1] == 'csv':
            count = count +1
            with open(fname, newline='') as f:
                reader = csv.reader(f)
                for row in reader:
                    length = len(row)
                    # print(length)
                    for each in row:
                        if each != '':
                            if each == 'Onions':
                                # print (each)
                                print(fname)
                    print('---------')

    print (count)
st = {}

def generateCountOfIng():
    count = 0
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
                    countOfRowNumber +=1

                    for each in row:
                        if countOfRowNumber ==2:
                            if each != '':
                                # print(each)
                                if each in st:
                                    value = st.get(each)
                                    # st.update(x,value+1)
                                    st[each] = value + 1
                                elif each not in st:
                                    st[each] = 1

    sorted_x = sorted (st.items (), key=operator.itemgetter (1), reverse=True)
    return sorted_x

countOfIngre =  generateCountOfIng()
dishes = {}
def generateCountOfDishesWithIngre():
    dishes = {}
    count = 0
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
                    countOfRowNumber +=1

                    for each in row:
                        if countOfRowNumber ==2:
                            if each != '':
                                # print(each)
                                if each in dishes:
                                    value = dishes.get(each)
                                    # st.update(x,value+1)
                                    dishes[each] = value + ',' + fname
                                elif each not in dishes:
                                    dishes[each] = fname

    for dish in dishes:
        print (dish + '====>' + dishes[dish])
    return dishes

countOfDishes = generateCountOfDishesWithIngre()

print(countOfDishes['Rice'])
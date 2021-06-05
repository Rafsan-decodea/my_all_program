import openpyxl
import subprocess

input_data = raw_input("input file name===>")
waireless = raw_input("[+] input Search 1===>")
lanphone = raw_input("[+] input search 2===>")

excel = openpyxl.load_workbook(input_data)
files = excel[excel.active.title]
sheet = files['A']

store1 =[]
store2 =[]
sotore3=[]


for x in xrange(len(sheet)):
    store1.append(sheet[x].value)

for y in store1:
    if "waireless" in y:
        store2.append(y)

for y in store1:
    if "landline" in y:
       sotore3.append(y)


sheet = files['D']






##data2=[]
##store = []
##store1 = []
##for x in xrange(len(sheet)):
##    data2.append( sheet[x].value)
##
##
##
##for x in data2:  # Search land Phone
##    if lanphone in x:
##        store.append(x)
##
##for y in data2:  # Search wairless
##    if waireless  in y:
##       store1.append(y)
##
##
##
##sheet2 = files['D']  # Colume Name
##for z in xrange(len(store)): # How Row Will be insert
##         sheet2[z].value =  store[z]
##
##
##sheet3 = files['G']
##for d in xrange(len(store1)):
##      sheet3[d].value = store1[d]

excel.save(input_data)





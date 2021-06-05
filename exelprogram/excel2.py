from openpyxl import *
from openpyxl.styles import Alignment


input_data = raw_input("input file name===>")
waireless = raw_input("[+] input Search 1===>")
lanphone = raw_input("[+] input search 2===>")

excel = load_workbook(input_data)
files = excel[excel.active.title] #Define Sheet name



store1 = []
store2 = []
store_wair =[]
store_lan =[]

sheet = files['A']

for x in xrange(len(sheet)):
      store1.append(sheet[x].value)

for x in store1:
     for y in  x.splitlines():
         store2.append(y)



for lenth in range(len(store2)):#this is process find Out Store1  data lan
         if waireless in store2[lenth]:
             store_wair.append(store2[lenth]) # if store 1st data is Wairless


for lenth in range(len(store2)):# this is process find Out Store2  data lan
         if lanphone in store2[lenth]: # if store 1st data is Lan
            store_lan.append(store2[lenth])


# sheet1 = files['D']


# for data_len in xrange(len(sheet1)):
#       sheet1[data_len].value = store_wair[data_len]

# sheet2 = files['F']
# for data_len in xrange(len(sheet2)):
#       sheet1[data_len].value = store_lan[data_len]

#sheet1 = excel.active

print("\n===========================")
for x in store_wair:
    print (x)
print("="*10)
for x in store_lan:
    print (x)






#excel.save("test.xlsx")





# import openpyxl
# import subprocess

# input_data = raw_input("input file name===>")
# waireless = raw_input("[+] input Search 1===>")
# lanphone = raw_input("[+] input search 2===>")

# excel = openpyxl.load_workbook(input_data)
# files = excel[excel.active.title]
# sheet = files['A']

# data2=[]
# store = []
# store1 = []
# for x in xrange(len(sheet)):
#     data2.append( sheet[x].value)



# for x in data2:  # Search land Phone
#     if lanphone in x:
#         store.append(x)

# for y in data2:  # Search wairless
#     if waireless  in y:
#        store1.append(y)



# sheet2 = files['D']  # Colume Name
# for z in xrange(len(store)): # How Row Will be insert
#          sheet2[z].value =  store[z]


# sheet3 = files['G']
# for d in xrange(len(store1)):
#       sheet3[d].value = store1[d]

# excel.save(input_data)






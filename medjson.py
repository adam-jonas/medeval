import json 

#Identify rows without an RxNorm code and print the corresponding order name to a file
File_Name = raw_input("File_Name: ")
RXNORM_CODE_Row = input("RXNORM_CODE Column: ")
DESCRIPTION_Row = input("DESCRIPTION Column: ")



dictionary_count = {}
none_descriptions = []
row_count = -1
count = 0

with open(File_Name) as json_data:
    reader = json.load(json_data)
    for row in reader:
        row_count += 1
        RXNORM_CODE = row[RXNORM_CODE_Row]
        DESCRIPTION = row[DESCRIPTION_Row]
        if RXNORM_CODE is "":
            none_descriptions.append(DESCRIPTION)
            count += 1
dictionary_count = {x:none_descriptions.count(x) for x in none_descriptions}
print dictionary_count
# print none_descriptions
print "Missing Description Row Total: ", count
print "Total Row Count: ", row_count

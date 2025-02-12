path = "excerpt.txt"

# with open(path, 'r') as f:
#     content = f.read()
# print(content)

with open(path,'r') as f :
    lst = [line.strip() for line in f if line.strip()]
print(lst)


# tabular data files can be two types as CSV(comma separted values) or TSV(tab separted values)
import csv 
path = "/path/to/cars.csv"
with open(path,'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    cars =[]
    for row in csv_reader :
        cars.append(dict(row))
# csv module's reader() method to turn the .csv file into a list of lists
with open(path,'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    cars =[]
    for row in csv_reader :
        cars.append(row)
#  the csv.DictReader() and csv.reader() methods have an optional delimiter parameter allowing you to specify
#  the character that separates fields in your tabular data file. This is defaults to comma which is perfect for csv files 
# by setting the parameter to delimiter = "\t", you can read .tsv files instead

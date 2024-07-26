
#Lists vs Tuple!!!! Video 44

#This is a list:
filenames = ["1.Raw Data.txt", "2. Reports.txt", "3.Presentations.txt"]

#This is a Tuple:
filenames = ("1.Raw Data.txt", "2. Reports.txt", "3.Presentations.txt")

#The difference is lists use [] and tuple us ()



filenames = ["1.Raw Data.txt", "2. Reports.txt", "3.Presentations.txt"]

for filename in filenames:
    filename = filename.replace(".", "-", 1)
    print(filename)







""" A simple example of parsing a csv file
   Look the documentation for more details on the csv library
   https://docs.python.org/3/library/csv.html
"""
import csv

# open the file to read it into the database
with open('USGS_WC_eartag_deployments_2009-2011.csv', newline='') as f:
    reader = csv.reader(f, delimiter=",")
    next(reader) # skip the header line
    for row in reader:
        print(row)

        """ we could do something with this data, 
        such as move it into a database, or process it by extracting items
        as here, being sure to convert them to the format required if they are not strings
        """
        bearID = int(row[0])
        pTT_ID = int(row[1])
        capture_lat = float(row[6])
        capture_long = float(row[7])
        sex = row[9]
        age_class = row[10]
        ear_applied = row[11]
    
    print("finished parsing")
f.close() # close the file 

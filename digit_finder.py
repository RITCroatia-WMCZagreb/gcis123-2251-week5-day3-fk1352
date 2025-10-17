import re
import csv

def find_digit(a_str,regex):
    for match in re.findall(regex,a_str):
        print(match)

def zip_check(filename):
    ##ZIP needs to start with 7,8 or 9, and in total has 5 digits
    zips_regex = "[7-9]\d{4}"  #regex for our ZIP
    with open(filename) as file:
       #Split we use as .split(",") and .split(" ")
       #in this case we will use CSV reader directly
       csv_reader = csv.reader(file)##wrapping csv reader around our file
       headers = next(csv_reader)##next is useing csv_reader to read one line
       for record in csv_reader:  ##continue reading the file
           #print(record)
           #print(record[1])
           if re.findall(zips_regex,record[1]):
               print(record[0],record[1])
               for match in re.findall(zips_regex,record[1]):
                   print("MATCH",match)




def main():
    zip_check("data/full_grades_010.csv")
    #testing REGEX
    #find_digit("01abc02def03gh6i","[0-9]+")
    #find_digit("abc_123_3#145","[a1#]")##extracing a,1,# characters

if __name__ == "__main__":
    main()
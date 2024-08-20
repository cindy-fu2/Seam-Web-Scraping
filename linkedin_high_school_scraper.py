import re
import csv
from bs4 import BeautifulSoup

dictList = []   # List of dicts. Each dict contains url and high school of each Linkedin profile
dictList_fields = ["Linkedin_URL", "High_School"]  # fields of the output csv

# This function takes in a row of the csv and appends high school information of the linkedin profile to the dictList.
def find_high_school(row):
    # Error handling of when a local HTML file given by the input CSV does not exist
    try:
        with open(row["Text_File"]) as fp:
            soup = BeautifulSoup(fp, 'html.parser')
    except FileNotFoundError:  # If we couldn't find the local HTML file, we say that this happened
        dictList.append(dict(Linkedin_URL = row["Linkedin_URL"], High_School = "Unable to find given HTML file"))
        return

    # Find the high school/high schools for this particular person
    education_section = soup.find(string="Education")
    if education_section == None:  # If there is no Education section
        high_school_string = "High school not found"
    else:
        in_education_section = education_section.find_parent().find_next_sibling()   # all schools are in a list, which is a sibling of the tag containing "Education"
        if in_education_section == None:  # If there is no sibling of the Education section
            high_school_string = "High school not found"
        else:
            high_schools = in_education_section.find_all("h3", string=re.compile("(H|h)igh (S|s)chool"))  # finds all high schools in the list

            # Generate the string containing the high school of the person (or high schools, if they transferred at some point)
            high_school_string = "";   # the string containing the person's high school
            is_first_school = True;
            for high_school in high_schools:
                # print(high_school.string)
                if is_first_school:
                    is_first_school = False
                else :
                    high_school_string += ", "   # append a comma between high schools if there is more than one high school
                    
                high_school_string += high_school.string

            # print(high_school_string)
            if len(high_schools) == 0:
                high_school_string = "High school not found"

    # Write the Linkedin URL and the corresponding high school into the dict
    dictList.append(dict(Linkedin_URL = row["Linkedin_URL"], High_School = high_school_string))

# Read from the input csv
with open('input_linkedin_profiles.csv', newline = '') as input_csv:
    reader = csv.DictReader(input_csv, fieldnames = ["Linkedin_URL", "Text_File"])
    for row in reader:
        find_high_school(row)

# Write to the output csv
with open('output_high_schools.csv', mode = 'w', newline = '') as output_csv:
    writer = csv.DictWriter(output_csv, fieldnames = dictList_fields, delimiter=',')
    writer.writeheader()
    writer.writerows(dictList)

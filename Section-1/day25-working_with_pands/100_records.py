import pandas

records = pandas.read_csv("100 Records.csv")

print(type(records))

# series
age_in_years = records["Age in Yrs."]
print(type(age_in_years))

# lookup how many are doctors
nm = records["Name Prefix"]


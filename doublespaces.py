
# removing the double gaps using replace:
string="this is a sentence , it dosent have any specific  meaning, except  testing out double spaces"
string=string.replace("  ","")
print(string)
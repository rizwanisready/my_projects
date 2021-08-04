authors = "Audre Lorde,Gabriela Mistral,Jean Toomer,An Qi,Walt Whitman,Shel Silverstein,Carmen Boullosa,Kamala Suraiyya,Langston Hughes,Adrienne Rich,Nikki Giovanni"
author_names = authors.split(",")
#print(author_names)
last_names_list = []
for names in author_names:
    last_names_list.append(names.split()[-1])
print(last_names_list)
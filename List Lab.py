from operator import contains


DC_list= ["superman", "batman", "flash", "greenlantern", "cyborg", "auqaman"]

MARVEL_list= ["ironman", "thor", "hulk", "antman", "captainamerica", "deadpool", "spiderman"]

man_list= []
NoMan_list=[]

for i in DC_list:
    if i[-3] == "m" and i[-2] == "a" and i[-1] == "n":
        man_list.append(i)
    else:
        NoMan_list.append(i)

for i in MARVEL_list:
    if i[-3] == "m" and i[-2] == "a" and i[-1] == "n":
        man_list.append(i)
    else:
        NoMan_list.append(i)

print("A list containing all super heroes ending with man", man_list)

print("All super heroes without man at the end", NoMan_list)
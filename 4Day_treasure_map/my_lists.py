usa_states = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts", "Maryland", "South Carolina", "New Hampshire", "Virginia", "New York", "North Carolina", "Rhode Island", "Vermont", "Kentucky", "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi", "Illinois", "Alabama", "Maine", "Missouri", "Arkansas", "Michigan", "Florida", "Texas", "Iowa", "Wisconsin", "California", "Minnesota", "Oregon", "Kansas", "West Virginia", "Nevada", "Nebraska", "Colorado", "North Dakota", "South Dakota", "Montana", "Washington", "Idaho", "Wyoming", "Utah", "Oklahoma", "New Mexico", "Arizona", "Alaska", "Hawaii"]

print(usa_states[20])
print(usa_states.index("California"))

state = usa_states[-5]
print(f"{state}, index {usa_states.index(state)}")

usa_states[1] = "Pencilvania"
print(usa_states[1])

usa_states.append("Angelalang") #to the end
print(f"{usa_states}\n-------------------------------------")

usa_states.extend(["Jack Bauer Land", "DisneyLand", "Horror Island"])
print(f"{usa_states}\n-------------------------------------")

usa_states.insert(2, "My Land")
print(f"{usa_states}\n-------------------------------------")

print(f"My Land index: {usa_states.index("My Land")}")
print(usa_states[2])



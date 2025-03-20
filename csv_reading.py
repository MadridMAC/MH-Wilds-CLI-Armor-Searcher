import csv

# Beautifies the CSV Armor row and makes it easier to read
def print_armor(armor):
    print(f"Armor Name: {armor[0]} // Armor Slot: {armor[1]}\nDeco Slots: {armor[2]} // Skills: {armor[3]}")
    print("===========x==========")

# Initially check through the entire CSV file to see if the provided skill name exists
def init_checker(csv_list, skill_name):
    contains_skill = False
    for item in csv_list:
        if skill_name in item[3]:
            contains_skill = True
    return contains_skill

# Searches for a single skill in the armor list
def single_armor_searcher(skill_name):
    with open('armordata.csv', newline='') as csvfile:
        listed_file = list(csv.reader(csvfile))
        if (not init_checker(listed_file, skill_name)):
            print("Skill not found - Ensure that you've typed a valid skill name (case sensitive)")
        for item in listed_file:
            if (skill_name in item[3]):
                print_armor(item)

# Searches for both skills on a single piece of armor in the list
def and_armor_searcher(skill_1, skill_2):
    with open('armordata.csv', newline='') as csvfile:
        listed_file = list(csv.reader(csvfile))
        if ((not init_checker(listed_file, skill_1)) or (not init_checker(listed_file, skill_2))):
            print("Skill not found - Ensure that you've typed a valid skill name (case sensitive)")
        for item in listed_file:
            if ((skill_1 in item[3]) and (skill_2 in item[3])):
                print_armor(item)

# Searches for either skill on a single piece of armor in the list
def or_armor_searcher(skill_1, skill_2):
    with open('armordata.csv', newline='') as csvfile:
        listed_file = list(csv.reader(csvfile))
        if ((not init_checker(listed_file, skill_1)) or (not init_checker(listed_file, skill_2))):
            print("Skill not found - Ensure that you've typed a valid skill name (case sensitive)")
        for item in listed_file:
            if ((skill_1 in item[3]) or (skill_2 in item[3])):
                print_armor(item)

def main():
    # Check if user wants AND, OR, or a SINGLE armor skill
    search_type = input("AND, OR, or SINGLE? ")
    if (search_type.upper() not in ["AND", "OR", "SINGLE"] ):
        print("Invalid input. Exiting...")
        return
    print("For each input, type EXIT to quit.")
    # While loop lets user search multiple times for the search type they chose
    while True:
        # Switch cases for SINGLE, AND, and OR searching
        match (search_type.upper()):
            case "SINGLE":
                skill_to_find = input("Enter armor skill to find: ")
                if (skill_to_find.upper() == "EXIT"):
                    return
                print("===========x==========")
                single_armor_searcher(skill_to_find)
            case "AND":
                skill_1 = input("Enter first skill to find: ")
                skill_2 = input("Enter second skill to find: ")
                if ((skill_1.upper() == "EXIT") or (skill_2.upper() == "EXIT")):
                    return
                print("===========x==========")
                and_armor_searcher(skill_1, skill_2)
            case "OR":
                skill_1 = input("Enter first skill to find: ")
                skill_2 = input("Enter second skill to find: ")
                if ((skill_1.upper() == "EXIT") or (skill_2.upper() == "EXIT")):
                    return
                print("===========x==========")
                or_armor_searcher(skill_1, skill_2)

main()
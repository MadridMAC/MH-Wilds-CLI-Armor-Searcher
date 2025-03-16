import csv

def print_armor(armor):
    print(f"Name: {armor[0]} // Armor Slot: {armor[1]}\nDeco Slots: {armor[2]} // Skills: {armor[3]}")
    print("===========x==========")

def init_checker(csv_list, skill_name):
    contains_skill = False
    for item in csv_list:
        if skill_name in item[3]:
            contains_skill = True
    return contains_skill

def main():
    skill_to_find = input("Enter armor skill to find: ")
    print("===========x==========")
    with open('armordata.csv', newline='') as csvfile:
        listed_file = list(csv.reader(csvfile))
        if (not init_checker(listed_file, skill_to_find)):
            print("Skill not found")
            return
        for item in listed_file:
            if (skill_to_find in item[3]):
                print_armor(item)

main()
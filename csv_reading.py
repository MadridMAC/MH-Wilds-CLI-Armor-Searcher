import csv

def print_armor(armor):
    print(f"Name: {armor[0]} // Armor Slot: {armor[1]}\nDeco Slots: {armor[2]} // Skills: {armor[3]}")
    print("===========x==========")

def main():
    skill_to_find = input("Enter armor skill to find: ")
    print("===========x==========")
    with open('armordata.csv', newline='') as csvfile:
        listed_file = list(csv.reader(csvfile))
        for item in listed_file:
            if (skill_to_find in item[3]):
                print_armor(item)

main()
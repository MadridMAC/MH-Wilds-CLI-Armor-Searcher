# MH Wilds CLI Armor Searcher
A simple Python project that reads a .csv file containing all armor sets from Monster Hunter Wilds, accepts a valid armor skill as input, and returns all known armor pieces containing that armor skill.<br>
I've limited the CSV file to only contain High Rank sets. Feel free to use it as a template and populate it with other sets.\
The CSV file also only uses Name, Armor Slot, Deco Slots, and Skills, so you should be able to adopt it for use with other games as well.
## How to Use
Before anything else, this script requires **Python 3.12.3**.<br><br>
First, specify whether you want to use SINGLE, OR, or AND skill searching:

- SINGLE will look for armor pieces containing the skill you input
- AND will look for armor pieces containing both of the two skills you input
- OR will look for armor pieces containing either of the two skills you input

Next, input the skill/s you want to search for as requested by the script.\
The program will then return the armor pieces fitting your criteria.<br>

To terminate the program, type in "exit" (case insensitive) for each requested input.

## Latest Changes
### To-Do
- Fill out armordata.csv with all current High Rank armor sets (pre-TU1)
### Version 2
- Added AND, OR, and SINGLE searching functionality
### Version 1.1
- Added some catches for invalid or incorrect input.
### Version 1.0
- Project release into GitHub.

"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""

numbers = set()
for call in calls:
    numbers.add(call[0])
    numbers.add(call[1])

for texts in texts:
    numbers.add(texts[0])
    numbers.add(texts[1])


print(f"There are {len(numbers)} different telephone numbers in the records.")

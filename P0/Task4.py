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
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

whitelist = []
for sendind, receiving, _ in texts:
    whitelist.append(sendind)
    whitelist.append(receiving)

callers = []
for caller, receiving, _, _ in calls:
    callers.append(caller)
    whitelist.append(receiving)

possibleTelemarketers = set(callers) - set(whitelist)

print("These numbers could be telemarketers: ")
for possibleTelemarketer in sorted(possibleTelemarketers):
    print(possibleTelemarketer)

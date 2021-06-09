"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
from os import lockf
from typing import DefaultDict
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

calls_dictionary = DefaultDict(int)
for caller, reciever, timestamp, duration in calls:
    calls_dictionary[caller] += int(duration)
    calls_dictionary[reciever] += int(duration)


def getSecondsFromCall(number):
    return calls_dictionary[number]


number = max(calls_dictionary, key=getSecondsFromCall)

print(
    f"{number} spent the longest time, {getSecondsFromCall(number)} seconds, on the phone during September 2016.")

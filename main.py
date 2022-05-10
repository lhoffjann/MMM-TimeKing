# This is a sample Python script.
from toggl.TogglPy import Toggl
#from dotenv import load_doten


def current_timer(time_entry: dict):
    if "stop" not in time_entry.keys():
        print(time_entry)

def last_entries(entries: list):
    if len(entries) < 5:
        for entry in entries:
            print(entry)
    elif len(entries) >= 5:
        for entry in entries[:5]:
            print(entry)

def sort_list_by_date(time_entries: list):
     for time_entry in time_entries:
        print(time_entry['start'], time_entry['stop'])

""""
[entry1, entry2, entry3...]
entry.start entry2.start 

"""
toggl = Toggl()
toggl.setAPIKey("")




response = toggl.request("https://api.track.toggl.com/api/v8/time_entries")
print(type(response))
for time_entry in response:
    current_timer(time_entry)

last_entries(response)



def calculate_total_time(time_periode):
    raise NotImplementedError



"""
Current Timer: description TIME
Total Time Today
Total Time Week
Last 5 Entries ....
"""
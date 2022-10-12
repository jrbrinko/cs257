'''
    convert.py
    For "Database Design" Assignment
    James Brink
    Oct 11 2022 
'''

import csv

# Creating athletes.csv
athletes = {}
with open('athlete_events.csv') as original_data_file,\
        open('athletes.csv', 'w') as athletes_file:
    reader = csv.reader(original_data_file)
    writer = csv.writer(athletes_file)
    heading_row = next(reader) # eat up and ignore the heading row of the data file
    for row in reader:
        athlete_id = row[0]
        athlete_name = row[1]
        if athlete_id not in athletes:
            athletes[athlete_id] = athlete_name
            writer.writerow([athlete_id, athlete_name])

# Creating the nocs.csv file.
nocs = {}
with open('noc_regions.csv') as original_data_file,\
        open('nocs.csv', 'w') as athletes_file:
    reader = csv.reader(original_data_file)
    writer = csv.writer(athletes_file)
    heading_row = next(reader) # eat up and ignore the heading row of the data file
    for row in reader: 
        noc_name = row[0]
        # Creates ID number for unique NOC (possibly unneeded)
        if noc_name not in nocs:
            noc_id = len(nocs) + 1
            nocs[noc_name] = noc_id
            writer.writerow([noc_id, noc_name])


# creating the events.csv file
events = {}
with open('athlete_events.csv') as original_data_file,\
        open('events.csv', 'w') as events_file:
    
    reader = csv.reader(original_data_file)
    writer = csv.writer(events_file)
    heading_row = next(reader) # eat up and ignore the heading row of the data file
    
    for row in reader:

        event_name = row[13]
        location_name = row[11]
        year = row[9]

        if event_name not in events:
            event_id = len(events) + 1
            events[event_name] = event_id
            writer.writerow([event_id, event_name, year])

# creating the events_results.csv file
with open('athlete_events.csv') as original_data_file,\
        open('event_results.csv', 'w') as event_results_file:
    reader = csv.reader(original_data_file)
    writer = csv.writer(event_results_file)
    heading_row = next(reader) # ignore first line

    for row in reader:
        athlete_id = row[0]

        noc_name = row[7]
        noc_id = nocs[noc_name]
        
        event_name = row[13]
        event_id = events[event_name] # this is guaranteed to work by section (2)
        medal = row[14]
        writer.writerow([event_id, athlete_id, noc_id, medal])
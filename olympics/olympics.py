'''
    olympics.py
    "OLYMPICS: A DB-DRIVEN COMMAND-LINE APPLICATION" Assignment
    James Brink
    Oct 11 2022 
'''

import sys
import psycopg2

# We're also going to import our postgres username, password,
# and database from a file named config.py, like so:
import config


def get_connection():
    ''' Returns a database connection object with which you can create cursors,
        issue SQL queries, etc. This function is extremely aggressive about
        failed connections--it just prints an error message and kills the whole
        program. Sometimes that's the right choice, but it depends on your
        error-handling needs. '''
    try:
        return psycopg2.connect(database=config.database,
                                user=config.user,
                                password=config.password)
    except Exception as e:
        print(e, file=sys.stderr)
        exit()

def usage_statement():
    #prints usage statement
    usage_txt = open('usage.txt', 'r')
    usage_contents = usage_txt.read()
    print(usage_contents)

def get_athletes_by_noc(search_text):
    '''
    Returns a list of athletes for the desired NOC (country)
    Input: search_text -- the NOC to search the query by
    Output: athletes -- list of athletes for the desired NOC
    '''

    athletes = []

    # The desired query command 
    try:
        query = '''SELECT DISTINCT athletes.name, nocs.name
        FROM athletes, nocs, event_results
        WHERE athletes.id = event_results.athlete_id
        AND nocs.id = event_results.noc_id
        AND nocs.name = %s;
        '''
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute(query, (search_text,))
        
        # Adds each data cell to to the list
        for row in cursor:
            noc = row[0]
            medal = row[1]
            athletes.append(f'{noc} | {medal}')

    except Exception as e:
        print(e, file=sys.stderr)

    connection.close()
    return athletes

def get_gold_medals():
    '''
    Returns a list of all NOCS that have recieved a gold medal in descending order
    Input: None
    Output: A list of each NOC and each gold medal they have won. 
    
    '''
    medals = []

    # SQL query
    try:
        query = '''
            SELECT nocs.name, COUNT(event_results.medal) as num_golds
            FROM nocs, event_results
            WHERE nocs.id = event_results.noc_id
            AND event_results.medal = 'Gold'
            GROUP BY nocs.name
            ORDER BY num_golds DESC; 
        '''
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute(query)

        # Adding to list from query
        for row in cursor:
            given_name = row[0]
            surname = row[1]
            medals.append(f'{given_name} | {surname}')

    except Exception as e:
        print(e, file=sys.stderr)

    return medals

def get_all_events(search_text):
    '''
    Returns list of all athletes from specified search text
    Input: search_text -- specified search text
    Output: events all events that have an athlete with the desired search text and the results.

    ***NOTE***
    There are some instances of athletes with middle names or nicknames in quotes. Try first name if your initial input does not yield the desirable results.
    '''
    events = []

    # SQL query
    try:
        query = '''
        SELECT events.name, athletes.name, event_results.medal
        FROM events, athletes, event_results
        WHERE athletes.id = event_results.athlete_id
        AND events.id = event_results.event_id
        AND athletes.name LIKE %s;
        '''
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute(query, (search_text,))
        
        # Formatting data into events list
        for row in cursor:
            event = row[0]
            athlete = row[1]
            result = row[2]
            events.append(f'{event} | {athlete} | {result}')

    except Exception as e:
        print(e, file=sys.stderr)

    connection.close()

    return events

def display_athlete(noc):
    # Displays list from argument
    print('========== Athletes in ' + noc + ' ==========')
    athletes = get_athletes_by_noc(noc)
    for athlete in athletes:
        print(athlete)

def display_golds():
    # Displays medal from argumetn
    print('====== NOCS and MEDALS ====')
    medals = get_gold_medals()
    for medal in medals:
        print(medal)


def display_events(search_athlete):
    # Displays list from argument
    print('========== EVENTS ==========')
    events = get_all_events(search_athlete)
    for event in events:
        print(event)

def main():
    
    # Checks the number of arguments.
    if 2 <= len(sys.argv) <= 3:

        # '--athlete' argument (athletes for each noc)
        if (sys.argv[1] in ['-a','--athlete']) \
        and len(sys.argv) == 3:
  
            display_athlete(sys.argv[2])
        
        # '--gold' argument (number of golds for each NOC)
        elif (sys.argv[1] in ['-g', '--gold']):
            display_golds()

        # '--event' argument (events with athletes with desired text)
        elif (sys.argv[1] in ['-e', '--event']) \
        and len(sys.argv) == 3:
            
            # '%' is for the SQL 'LIKE' query
            display_events(sys.argv[2] + '%')
        
        # '--help' argument 
        else :
            usage_statement()

    # In case of invalid number of arguments
    else:
        print("Invalid number of arguemnts.")
        usage_statement()


if __name__ == '__main__':
    main()

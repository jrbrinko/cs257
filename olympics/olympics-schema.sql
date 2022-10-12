CREATE TABLE athletes (
    id integer,
    name text
);

CREATE TABLE nocs (
    id integer,
    name text
);

CREATE TABLE events (
    id integer,
    name text,
    year integer
);

CREATE TABLE event_results (
    event_id integer,
    athlete_id integer,
    noc_id integer,
    medal text
);

\copy athletes from 'athletes.csv' DELIMITER ',' CSV NULL AS 'NULL'
\copy nocs from 'nocs.csv' DELIMITER ',' CSV NULL AS 'NULL'
\copy events from 'events.csv' DELIMITER ',' CSV NULL AS 'NULL'
\copy event_results from 'event_results.csv' DELIMITER ',' CSV NULL AS 'NULL'


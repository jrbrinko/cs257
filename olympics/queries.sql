SELECT nocs.name
FROM nocs
ORDER BY nocs.name;

SELECT DISTINCT athletes.name, nocs.name
FROM athletes, nocs, event_results
WHERE athletes.id = event_results.athlete_id
AND nocs.id = event_results.noc_id
AND nocs.name = 'JAM'

SELECT events.name, events.year, event_results.medal
FROM events, event_results, athletes
WHERE events.id = event_results.event_id
AND athletes.id = event_results.athlete_id
AND athletes.name LIKE '%Louganis'
ORDER BY events.year;

SELECT nocs.name, COUNT(event_results.medal) as num_golds
FROM nocs, event_results
WHERE nocs.id = event_results.noc_id
AND event_results.medal = 'Gold'
GROUP BY nocs.name
ORDER BY num_golds; 

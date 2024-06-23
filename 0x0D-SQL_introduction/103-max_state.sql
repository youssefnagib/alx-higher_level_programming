-- displays the Max temperature (Fahrenheit) by state ordered by state .
SELECT `state`, MAX(`value`) AS `max_temp` FROM `temperatures` GROUP BY `state` ORDER BY `state`;

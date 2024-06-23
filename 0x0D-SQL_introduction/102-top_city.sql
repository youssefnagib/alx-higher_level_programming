-- displays the average temperature (Fahrenheit) by city ordered by temperature (descending).
SELECT city, AVG(value) AS avg_temp FROM temperatures WHERE month IN (8, 9) GROUP BY city ORDER BY avg_temp DESC LIMIT 3;

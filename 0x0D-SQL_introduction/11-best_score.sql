--Top score 
--List records starting with the top score only for  > = 10
SELECT score, name FROM second_table 
WHERE score >= 10
ORDER BY score  DESC

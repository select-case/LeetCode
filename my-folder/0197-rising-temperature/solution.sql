# Write your MySQL query statement below
select W.id as Id from Weather W join Weather W1 where DATEDIFF(W.recordDate,W1.recordDate) = 1 and W.temperature > W1.temperature 

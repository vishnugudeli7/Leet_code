# Write your MySQL query statement below
select firstname,lastname,city,state FROM person p
 left join address a 
 on p.personid = a.personid;
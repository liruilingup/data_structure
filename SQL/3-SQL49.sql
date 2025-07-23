-- 

drop table if exists  `staff_tb` ; 
CREATE TABLE `staff_tb` (
`staff_id` int(11) NOT NULL,
`staff_name` varchar(16) NOT NULL,
`staff_gender` char(8) NOT NULL,
`post` varchar(11) NOT NULL,
`department` varchar(16) NOT NULL,
PRIMARY KEY (`staff_id`));
INSERT INTO staff_tb VALUES(1,'Angus','male','Financial','dep1'); 
INSERT INTO staff_tb VALUES(2,'Cathy','female','Director','dep1'); 
INSERT INTO staff_tb VALUES(3,'Aldis','female','Director','dep2'); 
INSERT INTO staff_tb VALUES(4,'Lawson','male','Engineer','dep1'); 
INSERT INTO staff_tb VALUES(5,'Carl','male','Engineer','dep2'); 
INSERT INTO staff_tb VALUES(6,'Ben','male','Engineer','dep1'); 
INSERT INTO staff_tb VALUES(7,'Rose','female','Financial','dep2'); 

drop table if exists  `attendent_tb` ;   
CREATE TABLE `attendent_tb` (
`info_id` int(11) NOT NULL,
`staff_id` int(11) NOT NULL,
`first_clockin` datetime NULL,
`last_clockin` datetime NULL,
PRIMARY KEY (`info_id`));
INSERT INTO attendent_tb VALUES(101,1,'2022-03-22 08:00:00','2022-03-22 17:00:00');
INSERT INTO attendent_tb VALUES(102,2,'2022-03-22 08:30:00','2022-03-22 18:00:00');
INSERT INTO attendent_tb VALUES(103,3,'2022-03-22 08:45:00','2022-03-22 17:00:00');
INSERT INTO attendent_tb VALUES(104,4,'2022-03-22 09:00:00','2022-03-22 18:30:00');
INSERT INTO attendent_tb VALUES(105,5,'2022-03-22 09:00:00','2022-03-22 18:10:00');
INSERT INTO attendent_tb VALUES(106,6,'2022-03-22 09:15:00','2022-03-22 19:30:00');
INSERT INTO attendent_tb VALUES(107,7,'2022-03-22 09:30:00','2022-03-22 18:29:00');

select s.post as post, avg(timestampdiff(second, first_clockin, last_clockin)/ (60*60)) as work_hours
from attendent_tb a
left join staff_tb s
on s.staff_id = a.staff_id 
group by s.post
order by work_hours DESC
;


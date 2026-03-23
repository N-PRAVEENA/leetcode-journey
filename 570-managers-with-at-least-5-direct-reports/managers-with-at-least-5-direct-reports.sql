select name from Employee e2 join (select managerId ,count(*) as dr from Employee group by managerId having count(*)>=5) e1 on e1.managerId=e2.Id

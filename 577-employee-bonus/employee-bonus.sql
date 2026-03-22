select 
a.name,b.bonus from Employee a left join Bonus b on a.empID=b.empId where bonus<1000 or bonus is null
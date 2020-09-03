#### mysql中使用rank函数
* rank()         有相同的排序，但是会跳过数字， 如1，1，1，4，4，6
* DENSE_RANK()   有相同的排序，但不跳过数字，如1,1,2,2,3,4
* row_number()   直接排序没有相同的:1，2，3，4

```sql
select emp_no,salary,dense_rank() over(order by salary desc) as rank
from salaries
where to_date='9999-01-01'

```


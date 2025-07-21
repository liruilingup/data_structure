https://www.nowcoder.com/exam/oj?page=1&tab=SQL%E7%AF%87&topicId=199
brew在本地安装的Mysql


MySQL 命令大全和基础知识学习
https://www.runoob.com/mysql/mysql-command-manual.html

正则表达式：
    LIKE ...% 来进行模糊匹配， MySQL 中使用 REGEXP 和 RLIKE来进行正则表达式匹配
事务使用：
    commit 提交，rollback 是回滚
 limit使用：
    select device_id from user_profile limit 0, 2; 表示从 0 开始，显示2条数据


刷题学习-SQL大厂笔试真题
1、 每个月Top3的周杰伦歌曲 （ROW_NUMBER() ）
学习22年的表达YEAR(fdate) = 2022、学习 between 18 and 25、学习月group by month(fdate)
-- 18-25岁用户
select user_id, age from user_info where age between 18 and 25;

-- 22 年的数据
select user_id,song_id, fdate from play_log where YEAR(fdate) = 2022;

-- group by 月
select month (fdate) as month, a.song_id, max(song_name) as song_name, count(1) as play_pv
from
play_log a
inner join user_info b on a.user_id = b.user_id
inner join song_info c on a.song_id = c.song_id
where year (fdate) = 2022
and age between 18 and 25
and singer_name = '周杰伦'
group by
month (fdate), a.song_id
;

--
select
    month,
    ranking,
    song_name,
    play_pv
from
    (
        select
            month,
            row_number() over (
                partition by
                    month
                order by
                    play_pv desc,
                    song_id
            ) as ranking,
            song_id,
            song_name,
            play_pv
        from
            (
                select
                    month (fdate) as month,
                    a.song_id,
                    max(song_name) as song_name,
                    count(1) as play_pv
                from
                    play_log a
                    inner join user_info b on a.user_id = b.user_id
                    inner join song_info c on a.song_id = c.song_id
                where
                    year (fdate) = 2022
                    and age between 18 and 25
                    and singer_name = '周杰伦'
                group by
                    month (fdate),
                    a.song_id
            ) a
    ) a
where
    ranking <= 3
order by
    month,
    ranking


ROW_NUMBER() 
是一个窗口函数，用于为结果集中的每一行分配一个唯一的序号。即使有相同的值，序号也是不同的
2、分析客户逾期情况 CONCAT
输出还款能力级别、逾期客户占比
按照百分数形式输出并四舍五入保留 1 位小数，最终结果按照占比降序排序
只有各个等级的数据统计，跟具体的客户没有关系，学会 concat函数和 round函数
-- ROUND(number, decimals)， 常用的数学函数； SELECT ROUND(123.456, 2);
-- number：需要进行四舍五入的数值。
-- decimals：（可选）指定保留的小数位数。如果省略，则默认为 0，即四舍五入到整数。

-- MySQL 中，CONCAT() 函数用于将多个字符串连接成一个字符串。
-- 可以连接两列，比如CONCAT(first_name, ' ', last_name)

-- 先 join查看数据
select *  
from loan_tb  as a 
join customer_tb as b 
on a.customer_id=b.customer_id;

-- 结果
SELECT
    pay_ability,
    CONCAT(round(count(overdue_days) / count(1) * 100, 1),'%') as overdue_ratio
FROM
    loan_tb l
    LEFT JOIN customer_tb c ON l.customer_id = c.customer_id
GROUP BY
    pay_ability
order by 2 desc 
3、获取指定客户每月的消费额 date_format
查询 Tom 这个客户在 2023 年、每月的消费金额（按月份正序显示）
学会使用date_format函数
-- DATE_FORMAT(date, format)
select
    date_format (t_time, '%Y-%m') as time,
    sum(t_amount) as total
from
    trade
    join customer on trade.t_cus = customer.c_id
where
    c_name = 'Tom'
    and t_type = 1
    and year (t_time) = 2023
group by
    1
order by
    1
4、查询连续入住多晚的客户信息 datediff
问题：请查询该酒店从6月12日开始、连续入住多晚的客户信息
注意：因为表里面有入住和离店信息，不需要group by了，只需要判断时间即可
-- datediff 函数
select datediff(checkout_time, checkin_time) from checkin_tb;
SELECT DATEDIFF('2025-02-20', '2025-01-01') AS days_difference;

-- sql 实现，注意不需要分组
select
    c.user_id as user_id,
    c.room_id as room_id,
    room_type,
    datediff (checkout_time, checkin_time) as days
from
    guestroom_tb g
    right join checkin_tb c on g.room_id = c.room_id
    and checkin_time like '2022-06-12%'
where
    datediff (checkout_time, checkin_time) > 1
order by
    days,
    room_id,
    user_id desc

5、统计所有课程参加培训人次 replace
题目：course 列是course1, course2, course3、course1, course2等等，统计 全部的course1
解决：就统计个数就可以
-- replace('col', ',' ,'')

-- 执行的SQL
select sum(length(course)-length(replace(course,',','')) + 1) as staff_nums
from cultivate_tb
7、查询培训指定课程的员工信息 LIKE
题目：只要培训的课程中包含course3课程就计入结果
解题：使用like模糊查询，就像编程的in类型
SELECT c.staff_id, staff_name
FROM staff_tb s
         JOIN cultivate_tb c ON s.staff_id = c.staff_id
WHERE course LIKE '%course3%'
ORDER BY staff_id;8、推荐内容准确的用户平均评分 distinct
如果同一用户推荐同一个内容标签的话，计算的时候只算一次。
解题：left的on条件里面可以跟着多个条件。可以使用 distinct user_id
select
    round(sum(score) / count(distinct user_id), 3) as avg_score
from
    user_action_tb
where
    user_id in (
        select
            user_id
        from
            user_action_tb as tb1
            join recommend_tb as tb2 on tb1.user_id = tb2.rec_user
            and tb1.hobby_l = tb2.rec_info_l
    )

9、每个商品的销售总额 （rank函数）
编写一个SQL查询，返回每个商品的销售总量，先按照商品类别升序排序，再按销售总量降序排列，同时包括商品名称和销售总量。此外，还需要在结果中包含每个商品在其所属类别内的排名，排名相同的商品可以按照 product_id 升序排序。
解题：需要窗口函数
-- RANK() 是一个窗口函数 用于为结果集中的每一行分配一个；函数会为具有相同值的行分配相同的排名，并

select
    name product_name,
    sum(quantity) total_sales,
    rank() over (
        partition by
            category
        order by
            sum(quantity) desc
    ) category_rank
from
    products a
    join orders b on a.product_id = b.product_id
group by
    product_name,
    category
10 、统计各岗位员工平均工作时长timestampdiff
-- TIMESTAMPDIFF() 是 MySQL 中用于计算两个日期或时间值之间差异的函数，支持多种时间单位，如秒、分钟、小时、天、月、年等。它比 DATEDIFF() 更灵活，可以精确到更细的时间单位
-unit：指定返回值的时间单位，可选值包括：SECOND\MINUTE\HOUR\DAY\WEEK\MONTH\QUARTER\YEAR
# 

select s.post as post, avg(timestampdiff(second, first_clockin, last_clockin)/ (60*60)) as work_hours
from attendent_tb a
left join staff_tb s
on s.staff_id = a.staff_id 
group by s.post
order by work_hours DESC

11、查询连续登陆的用户  DATE_SUB
请查询连续登陆不少于3天、的新注册用户
-- DATE_SUB 函数 ，减去年份
-- DATE_SUB(date, INTERVAL expr type)
-- date：需要进行减法操作的日期或时间值，可以是 DATE、DATETIME 或 TIMESTAMP 类型。
-- INTERVAL：关键字，表示后面跟随的是时间间隔。
-- expr：时间间隔的值，可以是一个整数或表达式。
-- type：时间间隔的单位，例如 DAY、MONTH、YEAR、HOUR

SELECT DATE_SUB('2025-02-20', INTERVAL 10 DAY) AS new_date; -- 减去10天

-- 使用窗口函数解决连续求解问题
SELECT  
    user_id
FROM
    (SELECT *,
     -- 若两行记录登录时间与序号相减是是相同值，则证明这两行时连续登录
        DATE_SUB(DATE(log_time), INTERVAL ranking DAY) AS dt
    FROM
        (SELECT 
            *,
         -- 首先根据用户分组，对用户登录时间进行排序
            ROW_NUMBER() OVER(PARTITION BY user_id ORDER BY log_time) AS ranking
        FROM login_tb
        JOIN register_tb USING(user_id)) AS t1) AS t2
GROUP BY user_id, dt
HAVING COUNT(dt)>=3
ORDER BY user_id;

-- 难
-- 从听歌流水中找到18-25岁用户在2022年每个月播放次数top 3的周杰伦的歌曲。

drop table if exists play_log;
create table `play_log` (
    `fdate` date,
    `user_id` int,
    `song_id` int
);
insert into play_log(fdate, user_id, song_id)
values 
('2022-01-08', 10000, 0),
('2022-01-16', 10000, 0),
('2022-01-20', 10000, 0),
('2022-01-25', 10000, 0),
('2022-01-02', 10000, 1),
('2022-01-12', 10000, 1),
('2022-01-13', 10000, 1),
('2022-01-14', 10000, 1),
('2022-01-10', 10000, 2),
('2022-01-11', 10000, 3),
('2022-01-16', 10000, 3),
('2022-01-11', 10000, 4),
('2022-01-27', 10000, 4),
('2022-02-05', 10000, 0),
('2022-02-19', 10000, 0),
('2022-02-07', 10000, 1),
('2022-02-27', 10000, 2),
('2022-02-25', 10000, 3),
('2022-02-03', 10000, 4),
('2022-02-16', 10000, 4);

drop table if exists song_info;
create table `song_info` (
    `song_id` int,
    `song_name` varchar(255),
    `singer_name` varchar(255)
);
insert into song_info(song_id, song_name, singer_name) 
values
(0, '明明就', '周杰伦'),
(1, '说好的幸福呢', '周杰伦'),
(2, '江南', '林俊杰'),
(3, '大笨钟', '周杰伦'),
(4, '黑键', '林俊杰');

drop table if exists user_info;
create table `user_info` (
    `user_id`   int,
    `age`       int
);
insert into user_info(user_id, age) 
values
(10000, 18);



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
;
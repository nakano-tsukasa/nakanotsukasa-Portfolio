MariaDB [user_db]> describe user_profiles;
+---------------+--------------+------+-----+---------+----------------+
| Field         | Type         | Null | Key | Default | Extra          |
+---------------+--------------+------+-----+---------+----------------+
| id            | int(11)      | NO   | PRI | NULL    | auto_increment |
| name          | varchar(255) | NO   |     | NULL    |                |
| email         | varchar(255) | NO   | UNI | NULL    |                |
| password_hash | varchar(255) | NO   |     | NULL    |                |
+---------------+--------------+------+-----+---------+----------------+
4 rows in set (0.001 sec)

MariaDB [user_db]> create table books(
    -> book_id int primary key auto_increment,
    -> user_id int not null,
    -> book_name varchar(255) not null,
    -> author varchar(255),
    -> published_date DATE,
    -> foreign key (user_id) references user_profiles(id)
    -> );

create table summaries(
summary_id int primary key auto_increment,
user_id int not null,
book_id int not null,
summary_text TEXT not null,
created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
FOREIGN KEY (user_id) REFERENCES user_profiles(id),
FOREIGN KEY (book_id) REFERENCES books(book_id)
);

2024/9/2に実行予定
CREATE TABLE derived_summaries(
    d_summary_id int PRIMARY KEY AUTO_INCREMENT,
    user_id int not null,
    book_id int not null,
    d_summary_text TEXT NOT NULL,
    d_created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    d_updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES user_profiles(id),
    FOREIGN KEY (book_id) REFERENCES books(book_id)
)

ALTER TABLE derived_summaries CHANGE COLUMN old_name new_name VARCHAR(255);

alter table derived_summaries modify d_summary_id int auto_increment;
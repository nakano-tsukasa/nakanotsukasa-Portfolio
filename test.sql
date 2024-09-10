-- Active: 1725963945883@@127.0.0.1@3306
CREATE Table book_groups (
    g_id INT auto_increment PRIMARY KEY,
    g_name VARCHAR(100) not null
);

INSERT into book_groups (g_name) VALUES ('others');

alter table books add column g_id int;

alter Table books
add constraint fk_book_group
Foreign Key (g_id) REFERENCES book_groups(g_id)
ON DELETE SET NULL
ON UPDATE CASCADE;

alter table books MODIFY column g_id int after book_name;

UPDATE books
SET g_id = 1
WHERE book_id = 1 AND user_id = 1;

ALTER Table books MODIFY column published_date text;

ALTER Table book_groups
add COLUMN user_id int not null;

alter Table book_groups
add constraint fk_user_id
Foreign Key (user_id) REFERENCES user_profiles(id)
on delete CASCADE
on update CASCADE;

ALTER Table user_profiles
ADD COLUMN is_verified BOOLEAN DEFAULT False;

UPDATE user_profiles
set is_verified = TRUE
where id = 1;
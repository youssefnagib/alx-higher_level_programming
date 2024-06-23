-- script that creates the database hbtn_0d_2
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
-- script that creates the user user_0d_2
CREATE USER IF NOT EXISTS user_0d_2@localhost IDENTIFIED BY 'user_0d_2_pwd';
-- user_0d_2 only have SELECT privilege in the database hbtn_0d_2
GRANT SELECT ON hbtn_0d_2.* TO user_0d_2@localhost ;
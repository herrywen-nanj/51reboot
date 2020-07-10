Create databases and tables.
```python
create database ops default character set utf8 collate utf8_unicode_ci;
```
```python
use ops;
create table yusers
(
UserID varchar(32) not null,
Name varchar(32) not null,
Phone varchar(11),
Company varchar(100),
Address varchar(1000),
Email varchar(100)
);
```

# Udacity Full Stack Web Developer Nanodegree

## Logs Analysis Project

#### Objective
Creating a reporting tool with Python using the `psycopg2` module on the mock `newsdata.sql` PostgreSQL database provided by Udacity. Then use this tool to query the database and produce a report that answers these questions:

1. What are the most popular three articles of all time?
2. Who are the most popular article authors of all time?
3. On which days did more than 1% of requests lead to errors?

#### Directions
1. Download [Vagrant](https://www.vagrantup.com/) and [VirtualBox](https://www.virtualbox.org/wiki/Download_Old_Builds_5_1) to install and manage your virtual machine.
Use the `vagrant up` command first, to bring the virtual machine online and then the `vagrant ssh` command to login.

2. Download the database provided by Udacity [here](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip). Unzip the file and place the newsdata.sql file inside the Vagrant folder.

3. Load the database using the following command: `psql -d news -f newsdata.sql`.

4. Connect to the database using the following command: `psql -d news`.

5. Create the following views:

##### Views for Question #2
```sql
CREATE VIEW article_authors AS
SELECT title, name
FROM articles, authors
WHERE articles.author = authors.id;
```
```sql
CREATE VIEW article_views AS
SELECT title, count(log.id) as views
FROM articles, log
WHERE log.path = CONCAT('/article/', articles.slug)
GROUP BY articles.title
ORDER BY views desc;
```

##### Views for Question #3
```sql
CREATE VIEW logs AS
SELECT to_char(time,'DD-MON-YYYY') as Date, count(*) as LogCount
FROM log
GROUP BY Date;
```
```sql
CREATE VIEW errorlogs AS
SELECT to_char(time,'DD-MON-YYYY') as Date, count(*) as ErrorCount
FROM log
WHERE STATUS = '404 NOT FOUND'
GROUP BY Date;
```

6. Now execute the Python file - `python logs_analysis.py`.

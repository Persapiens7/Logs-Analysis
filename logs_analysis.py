#!/usr/bin/env python3

import psycopg2

DBNAME = "news"

first_query = """
SELECT *
FROM article_views
LIMIT 3;
"""

second_query = """
SELECT name, sum(article_views.views) AS views
FROM article_authors, article_views
WHERE article_authors.title = article_views.title
GROUP BY name
ORDER BY views desc;
"""


third_query = """
SELECT errorlogs.date, round(100.0*errorcount/logcount,2) as percent
FROM logs, errorlogs
WHERE logs.date = errorlogs.date
AND errorcount > logcount/100;
"""


def connect(query):
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute(query)
    results = c.fetchall()
    db.close()
    return results


# Question 1: What are the most popular three articles of all time?
def most_popular_articles(query):
    results = connect(query)
    print('\n\nMost popular articles of all time:\n')
    for a in results:
        print(str(a[0]) + ': ' + str(a[1]) + ' views')


# Question 2: Who are the most popular article authors of all time?
def most_popular_authors(query):
    results = connect(query)
    print('\n\nMost popular authors of all time:\n')
    for a in results:
        print(str(a[0]) + ': ' + str(a[1]) + ' views')


# Question 3: On which days did more than 1% of requests lead to errors?
def high_error_percentage_days(query):
    results = connect(query)
    print('\n\nDay(s) when more than 1% of requests lead to error:\n')
    for a in results:
        print(str(a[0]) + ': ' + str(a[1]) + '% errors')


if __name__ == '__main__':
    # Print the results
    most_popular_articles(first_query)
    most_popular_authors(second_query)
    high_error_percentage_days(third_query)

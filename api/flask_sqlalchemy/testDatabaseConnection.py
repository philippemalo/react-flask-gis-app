import psycopg2
test = psycopg2.connect("dbname=db user=user host=localhost password=pass port=5432")
print(test)
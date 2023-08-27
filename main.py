QUERY = '''
select name, birthdate from animals where species = 'gorilla';
'''
QUERY = '''
select name from animals where not ( species = 'gorilla'  or  name ='Max');
'''
QUERY = '''
select name from animals where species='llama' and birthdate>='1995-01-01'and birthdate<='1998-12-31';
'''
#
# Uncomment one of these QUERY variables at a time and use "Test Run" to run it.
# You'll see the results below.  Then try your own queries as well!
#

QUERY = "select max(name) from animals;"

# QUERY = "select * from animals limit 10;"

# QUERY = "select * from animals where species = 'orangutan' order by birthdate;"

# QUERY = "select name from animals where species = 'orangutan' order by birthdate desc;"

# QUERY = "select name, birthdate from animals order by name limit 10 offset 20;"

# QUERY = "select species, min(birthdate) from animals group by species;"
QUERY="select * from animals where species ='llama'";

# QUERY = '''
# select name, count(*) as num from animals
# group by name
# order by num desc
# limit 5;
# '''
#
# Write a query that returns all the species in the zoo, and how many animals of
# each species there are, sorted with the most populous species at the top.
# 
# The result should have two columns:  species and number.
#
# The animals table has columns (name, species, birthdate) for each individual.
# 
QUERY = "select count(*) as num,species from animals group by species order by num desc "

# Insert a newborn baby opossum into the animals table and verify that it's
# been added. To do this, fill in the rest of SELECT_QUERY and INSERT_QUERY.
# 
# SELECT_QUERY should find the names and birthdates of all opossums.
# 
# INSERT_QUERY should add a new opossum to the table, whose birthdate is today.
# (Or you can choose any other date you like.)
#
# The animals table has columns (name, species, birthdate) for each individual.
#

SELECT_QUERY = '''
select name ,birthdate from animals where species='opossum'
'''

INSERT_QUERY = '''
insert into animals 
values('Ullu','opossum','1998-02-01');
'''
#
# Find the names of the individual animals that eat fish.
#
# The animals table has columns (name, species, birthdate) for each individual.
# The diet table has columns (species, food) for each food that a species eats.
#

QUERY = '''
select animals.name from animals join diet on animals.species=diet.species where food='fish'
'''

QUERY = '''
select food, count(*) as num 
from animals,diet
where animals.species=diet.species 
group by food
having num=1;
'''

QUERY = '''
select ordernames.name,count(*)as num 
from animals,taxonomy,ordernames
where animals.species=taxonomy.name
    and taxonomy.t_order=ordernames.t_order
group by ordernames.name
order by num desc
'''


import sqlite3

# Fetch some student records from the database.
db = sqlite3.connect("students")
c = db.cursor()
query = "select name, id from students order by name;"
c.execute(query)
rows = c.fetchall()

# First, what data structure did we get?
print "Row data:"
print rows

# And let's loop over it too:
print
print "Student names:"
for row in rows:
  print "  ", row[0]

db.close()
import sqlite3

db = sqlite3.connect("testdb")
c = db.cursor()
c.execute("insert into balloons values ('blue', 'water') ")
db.commit()
db.close()


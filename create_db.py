import sqlite3
conn = sqlite3.connect('pgmErrorGeneration.db')
conn.execute("PRAGMA foreign_keys = ON")
c = conn.cursor()


# Create table

c.execute("drop table if exists users")

c.execute("create table if not exists users(username varchar(100) primary key, password varchar(40) not null)")
c.execute("create table if not exists submissions(datetime varchar(100) primary key, username varchar(100) not null, language varchar(100), category varchar(100), program varchar(100), score int)")

#c.execute("INSERT INTO users VALUES('chitti','3d725109c7e7c0bfb9d709836735b56d943d263f')")
#c.execute("INSERT INTO users VALUES('rasya', '3d725109c7e7c0bfb9d709836735b56d943d263f')")
#c.execute("INSERT INTO users VALUES('jkprerana','3d725109c7e7c0bfb9d709836735b56d943d263f')")
#c.execute("INSERT INTO users VALUES('pragnya','3d725109c7e7c0bfb9d709836735b56d943d263f')")
#c.execute("INSERT INTO users VALUES('preet','3d725109c7e7c0bfb9d709836735b56d943d263f')")



conn.commit()
conn.close()


import sqlite3
import os
import requests


class Database():
	def __init__(self):
		if os.path.isfile("database.db"):
			self.con = sqlite3.connect('database.db')
			self.db_cursor = self.con.cursor()
		else:
			self.con = sqlite3.connect('database.db')
			self.db_cursor = self.con.cursor()
			self.init_db()

	def init_db(self):
		self.db_cursor.execute("CREATE TABLE locations(location_id integer PRIMARY KEY AUTOINCREMENT, name text NOT NULL, coordinates text NOT NULL)")
		self.db_cursor.execute("CREATE TABLE satellites(name text PRIMARY KEY, tle text NOT NULL)")
		self.con.commit()

	def insert_location(self, name, coordinates):
		entities = (name, coordinates)
		self.db_cursor.execute('INSERT INTO locations(name, coordinates) VALUES(?, ?)', entities)
		self.con.commit()

	def get_locations(self):
		self.db_cursor.execute('SELECT * FROM locations')
		rows = self.db_cursor.fetchall()
		return rows

	def delete_location(self, id):
		self.db_cursor.execute('DELETE FROM locations WHERE location_id = {}'.format(id))
		self.con.commit()

	def insert_tles(self, source):
		self.db_cursor.execute('DELETE FROM satellites')
		response = (requests.get(source)).text
		response = response.replace("\r", "")
		response = response.split("\n")
		count = len(response)
		for line in range(0, count - 2, 3):
			name = response[line]
			tle = name + "\n" + response[line + 1] + "\n" + response[line + 2]
			entities = (name, tle)
			self.db_cursor.execute('INSERT INTO satellites(name, tle) VALUES(?, ?)', entities)
		self.con.commit()

	def get_tles(self):
		self.db_cursor.execute('SELECT * FROM satellites')

		rows = self.db_cursor.fetchall()
		return dict(rows)


# def main():
# 	db = Database()
# 	# db.insert_location("Bucharest", "12, 32")
# 	# db.insert_location("London", "11, 32")
# 	rows = db.get_locations()
# 	print(rows)

# main()
from location_window import Ui_ChooseLocation
from PyQt5 import QtCore, QtGui, QtWidgets
from database import Database


class Location(QtWidgets.QMainWindow, Ui_ChooseLocation):
	def __init__(self, db, prev):
		QtWidgets.QMainWindow.__init__(self)
		self.setupUi(self)
		self.db = db
		self.prev = prev
		self.location_list = self.db.get_locations()
		self.fill_list()

		self.btnAddLocation.clicked.connect(self.add_location)
		self.btnDeleteLocation.clicked.connect(self.delete_element)

	def add_location(self):
		name = str(self.tbName.text())
		coordinates = str(self.tbCoordinates.text())
		if self.check_coordinates(coordinates):
			self.db.insert_location(name, coordinates)

			self.prev.fill_location_list()
			self.location_list = self.db.get_locations()
			self.lvLocations.clear()
			self.fill_list()

			self.tbName.setText("")
			self.tbCoordinates.setText("")

	def fill_list(self):
		ls = [x[1] for x in self.location_list]
		self.lvLocations.addItems(ls)

	def delete_element(self):
		#name = str(self.lvLocations.currentItem().text())
		index = self.lvLocations.currentRow()
		db_id = self.location_list[index][0]
		self.db.delete_location(db_id)

		self.prev.fill_location_list()
		self.location_list = self.db.get_locations()
		self.lvLocations.clear()
		self.fill_list()

	def check_coordinates(self, coo):

		try:
			coords = coo.split(",")
			coords = [x.strip() for x in coords]

			if coords[0][-1].upper() not in ["N", "S"]:
				return False
			if coords[1][-1].upper() not in ["E", "W"]:
				return False

			coords[0] = coords[0][:-1]
			coords[1] = coords[1][:-1]

			coords[0] = float(coords[0])
			coords[1] = float(coords[1])
		except Exception:
			return False

		return True

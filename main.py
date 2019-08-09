from main_window import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from database import Database
from location import Location
from satellite import Satellite
from prediction import Prediction


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
	def __init__(self):
		QtWidgets.QMainWindow.__init__(self)
		self.setupUi(self)
		self.database = Database()

		self.tles = self.database.get_tles()
		self.fill_satellite_list()

		self.fill_location_list()

		self.tbTle.setText("https://www.celestrak.com/NORAD/elements/noaa.txt")
		self.btnLoadTle.clicked.connect(self.load_tles)
		self.btnPredict.clicked.connect(self.predict)
		self.btnAddLocation.clicked.connect(self.open_location_chooser)

		self.location_chooser = Location(self.database, self)
		


	def load_tles(self):
		self.database.insert_tles(self.tbTle.text())
		self.tles = self.database.get_tles()
		self.fill_satellite_list()

	def fill_satellite_list(self):
		self.tbChooseSatellite.clear()
		tle_list = list(self.tles.keys())
		self.tbChooseSatellite.addItems(tle_list)

	def fill_location_list(self):
		locations = self.database.get_locations()
		location_names = [loc[1] for loc in locations]
		location_coord = [loc[2] for loc in locations]
		for i in range(len(location_names)):
			self.tbLocation.addItem(location_names[i], location_coord[i])

	def predict(self):
		sat = str(self.tbChooseSatellite.currentText())
		tle = self.tles[sat]
		with open("temp_tle.txt", "w") as f:
			f.write(tle+"\n")

		location = str(self.tbLocation.itemData(self.tbLocation.currentIndex()))
		satellite = Satellite(sat, tle, location)
		self.prediction = Prediction(satellite)
		self.prediction.show()

	def open_location_chooser(self):
		self.location_chooser.show()



if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = MainWindow()
    MainWindow.show()
    sys.exit(app.exec_())
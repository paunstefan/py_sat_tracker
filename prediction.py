from satellite_window import Ui_SatPage
from PyQt5 import QtCore, QtGui, QtWidgets
import matplotlib.pyplot as plt


class Prediction(QtWidgets.QMainWindow, Ui_SatPage):
	def __init__(self, satellite):
		QtWidgets.QMainWindow.__init__(self)
		self.setupUi(self)

		self.satellite = satellite
		self.write_info()

		self.lvPasses.addItems(self.satellite.pass_times)

		self.btnPlot.clicked.connect(self.plot)

	def write_info(self):
		self.nameLabel.setText(self.satellite.name)

		lines = self.satellite.tle
		lines = lines.split("\n")
		self.numberLabel.setText(lines[1].split(" ")[1])
		self.inclinationLabel.setText(lines[2].split(" ")[3])
		self.ascensionLabel.setText(lines[2].split(" ")[4])
		self.eccentricityLabel.setText(lines[2].split(" ")[5])
		self.argumentLabel.setText(lines[2].split(" ")[6])
		self.anomalyLabel.setText(lines[2].split(" ")[7])
		self.motionLabel.setText(lines[2].split(" ")[8][:15])

	def plot(self):
		index = self.lvPasses.currentRow()
		pass_indice = self.satellite.passes[index]
		print(pass_indice)
		self.satellite.plot_sky(pass_indice)

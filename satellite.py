from skyfield import api
from pytz import timezone
import numpy as np
import datetime
import matplotlib.pyplot as plt


class Satellite():
	def __init__(self, name, tle, location):
		self.name = name.strip()
		self.tle = tle
		self.timezone = timezone("Etc/UTC")
		current_time = datetime.datetime.utcnow()
		lat = location.split(",")[0].strip()
		lon = location.split(",")[1].strip()

		self.sats = api.load.tle('temp_tle.txt')
		self.sat = self.sats[self.name]

		minutes = range(60 * 24 * 2)
		ts = api.load.timescale()
		self.t = ts.utc(current_time.year, current_time.month, current_time.day, current_time.hour, minutes)
		place = api.Topos(latitude=lat, longitude=lon)
		orbit = (self.sat - place).at(self.t)
		self.alt, self.az, distance = orbit.altaz()

		above_horizon = self.alt.degrees > 0

		boundaries, = np.diff(above_horizon).nonzero()
		self.passes = boundaries.reshape(len(boundaries) // 2, 2)

		self.pass_times = []
		for p in range(len(self.passes)):
			i, j = self.passes[p]
			azimuth = self.az.degrees
			altitude = self.alt.degrees
			azimuth = int(max(azimuth[i:j]))
			altitude = int(max(altitude[i:j]))
			rise = str(self.t[i].astimezone(self.timezone))[:-6]
			sets = str(self.t[j].astimezone(self.timezone))[:-6] + "-> " + str(altitude) + "°"
			self.pass_times.append(rise + " - " + sets)

	def plot_sky(self, pass_indices):
		i, j = pass_indices

		ax = plt.subplot(111, projection='polar')
		ax.set_rlim([0, 90])
		ax.set_theta_zero_location('N')
		ax.set_theta_direction(-1)

		theta = self.az.radians
		r = 90 - self.alt.degrees

		ax.plot(theta[i:j], r[i:j], 'ro--')
		for k in range(i, j):
			text = self.t[k].astimezone(self.timezone).strftime('%H:%M')
			ax.text(theta[k], r[k], text, ha='right', va='bottom')

		plt.show()

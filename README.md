# py_sat_tracker

Simple PyQt program for tracking satellites.

# Installation

Run the following pip command to install the requirements:

```
pip install -r requirements.txt
```

After this, just run the software with:

```
python3 main.py
```

# Usage

![Main window](/uploads/83a678177ca9646d4869ad0155581b30/1.png)

In the main window, choose your location, TLE source and satellite of interest and click "Predict passes".

![Satellite page](/uploads/f4e09b2fcbb12f5b97cb4e1f206c7a30/2.png)

The satellite page shows information about the satellite and a list of future passes. Select a pass and you can see a polar plot for your location.

![Pass polar plot](/uploads/92d34cebaf5b4cd03054362d66b743ba/3.png)
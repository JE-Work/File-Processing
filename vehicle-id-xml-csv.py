#!/usr/bin/env python

# A Python script to convert data within an XML file into csv. No user interface
# was required.
# The script needed to be flexible enough the data extracted could be changed in 
# the code easily. (i.e. Part and BaseVehicleId in one run and then Part and Mfglabel
# in another run.
# This was to be used on a Windows platform.

import csv
import xml.etree.ElementTree as ET

#PATH = # Location of XML file

# LIST OF DATA WANTED
DATA = ['part', 'mfr_label', 'base_vehicle', 'part_type', ]
FILTER = ['part', 'mfr_label', 'base_vehicle', ] 

# PARSE XML 
xml = ET.parse('vehicle-data.xml')

# CREATE CSV FILE
with open('vehicle-data.csv', 'w', encoding='utf-8') as csv_file:
    csv_writer = csv.writer(csv_file)

    # ADD HEADER TO CSV FILE
    csv_writer.writerow([FILTER])

    # EXTRA DATA
    for app in xml.findall('App'):
        part = app.find('Part').text
        mfr_label = app.find('MfrLabel').text
        base_vehicle = list(app.find('BaseVehicle').attrib.values())[0]
        part_type = list(app.find('PartType').attrib.values())[0]

        #FILTER DATA TO ONLY WANTED ITEMS WRITE TO FILE
        FILTER_VAR = [v for k,v in locals().items() if k in FILTER]
        csv_writer.writerow([FILTER_VAR])

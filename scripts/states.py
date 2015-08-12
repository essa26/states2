#!/usr/bin/env python
import csv
import os
import sys

sys.path.append("..")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_states.settings")

from main.models import State, StateCapital

#print State.objects.all()

csv_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "states.csv")

csv_file = open(csv_file_path, 'r')

reader = csv.DictReader(csv_file)

#print reader

for row in reader:
	state_obj, created = State.objects.get_or_create(name=row['state'])
	#state_obj.name = row['state']
	state_obj.abbreviation = row['abbrev']
	state_obj.save()
	
	capital_obj, created = StateCapital.objects.get_or_create(name=row['capital'])
	capital_obj.latitude = row['latitude']
	capital_obj.longitude = row['longitude']
	capital_obj.population = row['population']
	capital_obj.state = state_obj 

	capital_obj.save()












	#print "State:%s Abbreviation:%s Capital:%s" % (row['state'], row['abbrev'], row['capital'])
	#print """
				#Welcome to {0},


				#Abbreviation:{2} Capital:{3}

				#""".format(row['state'], row['abbrev'], row['capital'])
import fiona
import csv

def main():
	'''
	filename_zone = "../data/Zone" 
	filename_format = ".gdb"
	for year in range(2009, 2015):
		for zone in range(1,13):
			for count in range(1,17):
				final = filename_zone + str(zone) + "_" + str(year) + "_" + str(count).zfill(2) + filename_format
				print(final)
	
	filename_zone = "../data/2009/01_January_2009/" 
	for zone in range(1,19):
			final = filename_zone + str(zone) + "_2009_01.gdb"
	'''
	gdb_data = fiona.open("../data/Zone1_2014_01.gdb")
	print(gdb_data.schema)
	print(len(gdb_data))

	ais_data = [['id','latitude','longitude','SOG','COG','Heading','ROT','Year','Month','Day','Hour','Min','Sec','Status','VoyageID','MMSI','ReceiverType','ReceiverID']]
	for row in gdb_data:
		val = row['properties']['BaseDateTime'].split('-')
		val.extend(val[2][3:].split(':'))
		val[2] = val[2][:2]
		y,m,d,h,mn,s = val
		ais_data.append([str(x) for x in [row['id'], row['geometry']['coordinates'][1], row['geometry']['coordinates'][0], row['properties']['SOG'], row['properties']['COG'], row['properties']['Heading'], row['properties']['ROT'], y,m,d,h,mn,s, row['properties']['Status'], row['properties']['VoyageID'], row['properties']['MMSI'], row['properties']['ReceiverType'], row['properties']['ReceiverID']]])
		
	print(len(ais_data))
	with open("../data/Zone1_2014_01.csv", "w") as f:
		writer = csv.writer(f)
		writer.writerows(ais_data)


#{'type': 'Feature', 'id': '64963', 'geometry': {'type': 'Point', 'coordinates': (-177.529652, 51.07158000000001)}, 'properties': OrderedDict([('SOG', 13.199999809265137), ('COG', 79.4000015258789), ('Heading', 75.0), ('ROT', 0.0), ('BaseDateTime', '2014-01-31T23:59:28'), ('Status', 0), ('VoyageID', 526), ('MMSI', 311700007), ('ReceiverType', 'r'), ('ReceiverID', '17MADA1')])}

if __name__=="__main__":
	main()
import fiona
gdb_data = fiona.open("../data/Zone1_2014_01.gdb")
print(gdb_data.schema)
for row in gdb_data:
	print row
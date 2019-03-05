# based on https://github.com/hfionte/csv_to_yaml

# Import the python library for parsing CSV files.
import csv
import glob

all_csvs = glob.glob('*.csv')

# open all CSVs
csvfile = open(all_csvs[0], 'r')

datareader = csv.reader(csvfile, delimiter=',', quotechar='"')

# Empty array for data headings, which we will fill with the first row from our CSV.
data_headings = []

# Loop through each row...
for row_index, row in enumerate(datareader):

	# If this is the first row, populate our data_headings variable.
	if row_index == 0:
		data_headings = row
		print(data_headings)

	# Otherwise, create a grav .meta.yaml file from the data in this row
	else:
		# Open a new file with filename based on the correct column from the CSV

		if row_index > 0:
			# print(row[1])
			# change this integer to change what column the file name is based on
			fname = row[1]

		filename = str(fname) + '.jpg.meta.yaml'
		new_yaml = open(filename, 'w')

		# Empty string that we will fill with yaml formatted text based on data extracted from our CSV.
		yaml_frontmatter = ""
		grav_tags = ""
		taxonomy_header = "taxonomy: " + "\n"

		for cell_index, cell in enumerate(row[:4]):

			cell_heading = data_headings[cell_index].lower().replace(" ", "_").replace("-", "")
			cell_text = cell_heading + ": " + cell.replace("\n", ", ") + "\n"

			yaml_frontmatter += cell_text

		for cell_index, cell in enumerate(row[+5:]):
			# print(cell)
			
			cell_heading = data_headings[cell_index].lower().replace(" ", "_").replace("-", "")
			taxonomy_text = "\t" + cell_heading + ": " + cell.replace("\n", ", ") + "\n"

			grav_tags += taxonomy_text

		new_yaml.write(yaml_frontmatter + taxonomy_header + grav_tags)
		new_yaml.close()

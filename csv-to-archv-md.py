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
			fname = row[3]

		filename = str(fname).replace(".jpg", "") + '.md'
		new_md = open(filename, 'w')
		meta_separator = str("---")

		# Empty string that we will fill with yaml formatted text based on data extracted from our CSV.
		md_frontmatter = ""
		md_tags = ""
		# taxonomy_header = "taxonomy: " + "\n"

		# for cell_index, cell in enumerate(row[:5]):
			# cell_index = row number
			# cell_heading = column header in csv
			

			# cell_heading = data_headings[cell_index].lower().replace(" ", "_").replace("-", "")
			# cell_text = cell_heading + ": " + "\"" + cell.replace("\n", ", ") + "\"" + "\n" 

			# md_frontmatter += cell_text

			# print(cell_text)

		for cell_index, cell in enumerate(datareader):

			if row_index == 6:
			# print(cell)
			
				cell_heading = data_headings[cell_index].lower().replace(" ", "_").replace("-", "")
				taxonomy_text = cell_heading + ": " + "[" + cell.replace("\n", ", ") + "]" + "\n"

				# md_frontmatter += taxonomy_text
				md_tags += taxonomy_text

		new_md.write(meta_separator + "\n" + md_tags + meta_separator +"\n")
		new_md.close()

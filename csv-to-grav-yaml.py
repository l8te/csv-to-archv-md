# modifed from https://github.com/hfionte/csv_to_yaml

# Takes a file CSV file called "data.csv" and outputs each row as a numbered YAML file.
# Data in the first row of the CSV is assumed to be the column heading.

# Import the python library for parsing CSV files.
import csv
# import glob

# get any CSV file - have gotten this to print the CSV name, but cannot open it
# for name in glob.glob('*.csv'):
	# print(name)

# Open our data file in read-mode.
csvfile = open('data.csv', 'r')

# Save a CSV Reader object.
datareader = csv.reader(csvfile, delimiter=',', quotechar='"')

# Empty array for data headings, which we will fill with the first row from our CSV.
data_headings = []

# Loop through each row...
for row_index, row in enumerate(datareader):

	# If this is the first row, populate our data_headings variable.
	if row_index == 0:
		data_headings = row

		# Otherwise, create a grav .meta.yaml file from the data in this row
	else:
		# Open a new file with filename based on the correct column from the CSV

		if row_index > 0:
			# print(row[1])
			# change this integer to change what column the file name is based on
			fname = row[1]

		filename = str(fname) + '.jpg.meta.yaml'
		new_yaml = open(filename, 'w')
		# frontmatter_delimiter = str("---")

		# Empty string that we will fill with yaml formatted text based on data extracted from our CSV.
		yaml_frontmatter = ""
		# yaml_body = ""
		# yaml_img = ""

		# Loop through each cell, EXCEPT those in "description", in this row...
		for cell_index, cell in enumerate(row):

			# Compile a line of yaml text from our headings list and the text of the current cell, followed by a linebreak.
			# Heading text is converted to lowercase. Spaces are converted to underscores and hyphens are removed.
			# In the cell text, line endings are replaced with commas.
			cell_heading = data_headings[cell_index].lower().replace(" ", "_").replace("-", "")
			cell_text = cell_heading + ": " + cell.replace("\n", ", ") + "\n"

			# Add this line of text to the current yaml string.
			yaml_frontmatter += cell_text

		# for cell_index, cell in (row['image']):
			# to do: add link to image above yaml+body - ![Tux, the Linux mascot](/assets/images/tux.png)

			# yaml_img = "![" + cell + "](" + cell + ")" + "\n"
			# print(yaml_img)

		# for cell_index, cell in enumerate(row[+4:]):

		# 	yaml_text = "\n" + cell
			

		# 	yaml_body += yaml_text


		# Write our yaml string to the new text file and close it.
		# new_yaml.write(frontmatter_delimiter + "\n" + yaml_frontmatter + frontmatter_delimiter +"\n" + yaml_body)
		new_yaml.write(yaml_frontmatter)
		new_yaml.close()

# We're done! Close the CSV file.
csvfile.close()
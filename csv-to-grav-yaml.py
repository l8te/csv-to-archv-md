# modifed from https://github.com/hfionte/csv_to_yaml

# Takes a CSV file and outputs each row as a YAML file.
# Data in the first row of the CSV is assumed to be the column heading.

# Import the python library for parsing CSV files.
import csv

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
			# change this integer to change what column the file name is based on
			fname = row[1]
			
		# change file extension here as needed
		filename = str(fname) + '.jpg.meta.yaml'
		new_yaml = open(filename, 'w')

		# Empty string that we will fill with yaml formatted text based on data extracted from our CSV.
		yaml_frontmatter = ""

		# Loop through each cell in this row...
		for cell_index, cell in enumerate(row):

			# Compile a line of yaml text from our headings list and the text of the current cell, followed by a linebreak.
			# Heading text is converted to lowercase. Spaces are converted to underscores and hyphens are removed.
			# In the cell text, line endings are replaced with commas.
			cell_heading = data_headings[cell_index].lower().replace(" ", "_").replace("-", "")
			cell_text = cell_heading + ": " + cell.replace("\n", ", ") + "\n"

			# Add this line of text to the current yaml string.
			yaml_frontmatter += cell_text

		# Write our yaml string to the new text file and close it.
		# new_yaml.write(frontmatter_delimiter + "\n" + yaml_frontmatter + frontmatter_delimiter +"\n" + yaml_body)
		new_yaml.write(yaml_frontmatter)
		new_yaml.close()

# We're done! Close the CSV file.
csvfile.close()

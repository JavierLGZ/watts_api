import pandas
import json

# Read excel document
excel_data_df = pandas.read_excel('fixture.xlsx', sheet_name='sheet1')

# Convert excel to string 
# (define orientation of document in this case from up to down)
thisisjson = excel_data_df.to_json(orient='records')

# Print out the result
print('Excel Sheet to JSON:\n', thisisjson)

# Make the string into a list to be able to input in to a JSON-file
thisisjson_dict = json.loads(thisisjson)

# Define file to write to and 'w' for write option -> json.dump() 
# defining the list to write from and file to write to
with open('data.json', 'w') as json_file:
    json.dump(thisisjson_dict, json_file)
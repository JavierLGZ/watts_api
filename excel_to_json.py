import json
from datetime import datetime, timedelta

import pandas


def main():
    excel_data_df = pandas.read_excel("fixture_excel.xlsx", sheet_name="Query result")
    excel_to_json_string = excel_data_df.to_json(orient="records")
    json_data = json.loads(excel_to_json_string)
    load_data = []

    for data in json_data:
        data["meter_date"] = datetime.fromtimestamp(data["meter_date"] // 1000)
        data["meter_date"] += timedelta(hours=5)
        data["meter_date"] = data["meter_date"].isoformat()
        data_structure = {"model": "watts_api.wattconsume", "fields": data}
        load_data.append(data_structure)

    with open("fixture.json", "w") as json_file:
        json.dump(load_data, json_file)


if __name__ == "__main__":
    main()

from datetime import datetime

formatted_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

data_cai_a = {"Monday":["MFC","CP","C", "FIH", "TC", "[LAB] CP"],
              "Tuesday": ["DM", "MFC", "MAOM","MAOM", "YOGA", "[LAB] TC" ,],
              "Wednesday":["CP", "MFC", "ECS", "C", "TC", "[LAB] ECS"],
              "Thursday":["C", "DM", "ECS", "MAOM", "COUNS.", "[LAB] DM"],
              "Friday":["FIH", "C", "[LAB] C", "[LAB] C", "LIBRARY", "[LAB] MFC"] }
# for key, value in data_cai_a.items():
#     print(data_cai_a[key][5], "weights: ", "8" )

print(formatted_date)
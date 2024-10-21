from datetime import datetime, timedelta

current_day = datetime.now().strftime("%A")

data_cai_a = {
    "Monday": ["MFC", "CP", "C", "FIH", "TC", "[LAB] CP"],
    "Tuesday": ["DM", "MFC", "MAOM", "MAOM", "YOGA", "[LAB] TC"],
    "Wednesday": ["CP", "MFC", "ECS", "C", "TC", "[LAB] ECS"],
    "Thursday": ["C", "DM", "ECS", "MAOM", "COUNS.", "[LAB] DM"],
    "Friday": ["FIH", "C", "[LAB] C", "[LAB] C", "LIBRARY", "[LAB] MFC"],
}

today = datetime.now()
next_day_date = today + timedelta(days=1)
next_day = next_day_date.strftime("%A")

print("Current Day:", current_day)
print("Next Day:", next_day)

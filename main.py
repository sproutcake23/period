from datetime import datetime, timedelta

current_day = datetime.now().strftime("%A")

data_cai_a = {
    "Monday": ["MFC", "CP", "C", "FIH", "TC", "CP", "CP", "CP"],
    "Tuesday": ["DM", "MFC", "MAOM", "MAOM", "YOGA", "TC", "TC", "TC"],
    "Wednesday": ["CP", "MFC", "ECS", "C", "TC", "ECS", "ECS", "ECS"],
    "Thursday": ["C", "DM", "ECS", "MAOM", "COUNS.", "DM", "DM", "DM"],
    "Friday": ["FIH", "C", "C", "C", "LIBRARY", "MFC", "MFC", "MFC"],
}

today = datetime.now()
next_day_date = today + timedelta(days=1)
next_day = next_day_date.strftime("%A")

print("Current Day:", current_day)
print("Next Day:", next_day)

notDone = True # loop
final_list = [] # final list

while notDone:
    sub_input = input("Enter the subjects you need to work on :")

    ## error -- cannot split
    todo_sub=[x.strip() for x in sub_input.split(",")]
    
    next_day_tb = data_cai_a.get(next_day,[])
    
    if sub_input.lower() == "q":
        final_list = todo_sub
        print(sub_input.split(",")) ## DB
        print(todo_sub) ## DB

        notDone = False

for x in todo_sub:
        print(f"Prioritise these subjects {x}")    
    

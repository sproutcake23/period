from datetime import datetime, timedelta

current_day = datetime.now().strftime("%A")

data_cai_a = {
    "Monday": ["MFC", "CP", "C", "FIH", "TC", "CP", "CP", "CP"],
    "Tuesday": ["DM", "MFC", "MAOM", "MAOM", "YOGA", "TC", "TC", "TC"],
    "Wednesday": ["CP", "MFC", "ECS", "C", "TC", "ECS", "ECS", "ECS"],
    "Thursday": ["C", "DM", "ECS", "MAOM", "COUNS.", "DM", "DM", "DM"],
    "Friday": ["FIH", "C", "C", "C", "LIBRARY", "MFC", "MFC", "MFC"],
}

prio =[]
not_prio=[]

today = datetime.now()
next_day_date = today + timedelta(days=1)
next_day = next_day_date.strftime("%A")

print("Current Day:", current_day)
print("Next Day:", next_day)

notDone = True 
print('''Enter the subjects you need to work on 
and press q to go to the next step :''')
while notDone:
    sub_input = input("")

    if sub_input.lower() == "q":
        notDone =False
        continue

    todo_sub=[x.strip() for x in sub_input.split(",")]
    
    next_day_tb = data_cai_a.get(next_day,[])

    for x in todo_sub:
        if x in next_day_tb:
            prio.append(x)
        else:
            not_prio.append(x)
     

print(f"Prioritise these subjects {prio}")           
print(f"Do these subjects later{not_prio}")

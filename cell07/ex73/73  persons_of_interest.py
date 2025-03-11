from datetime import datetime

def famous_births(historical_figures):
   
    sorted_figures = sorted(historical_figures.items(), key=lambda x: datetime.strptime(x[1]['date_of_birth'], '%d-%m-%Y'))
    for figure in sorted_figures:
        name = figure[1]['name']
        date_of_birth = figure[1]['date_of_birth']
        print(f"Name: {name}, Date of Birth: {date_of_birth}")

historical_figures = {
    1: {"name": "Cristiano Ronaldo", "date_of_birth": "5-2-1985"},
    2: {"name": "Kaka", "date_of_birth": "22-04-1982"},
    3: {"name": "Wayne Rooney", "date_of_birth": "10-9-2003"},
    4: {"name": "Mitree Kumsu", "date_of_birth": "22-07-2007"}
}

famous_births(historical_figures)

gamers = {}
def add_gamer(gamer, gamers_list):
    if gamer.get("name") and gamer.get("availability"):
        gamers_list.update(gamer)
    else:
        print("Gamer missing critical information")

kimberly = {"name": "Kimberly", "availability": ["Mondays", "Tuesdays", "Fridays"]}
add_gamer(kimberly, gamers)
#print((gamers))

add_gamer({'name':'Thomas Nelson','availability': ["Tuesday", "Thursday", "Saturday"]}, gamers)
add_gamer({'name':'Joyce Sellers','availability': ["Monday", "Wednesday", "Friday", "Saturday"]}, gamers)
add_gamer({'name':'Michelle Reyes','availability': ["Wednesday", "Thursday", "Sunday"]}, gamers)
add_gamer({'name':'Stephen Adams','availability': ["Thursday", "Saturday"]}, gamers)
add_gamer({'name': 'Joanne Lynn', 'availability': ["Monday", "Thursday"]}, gamers)
add_gamer({'name':'Latasha Bryan','availability': ["Monday", "Sunday"]}, gamers)
add_gamer({'name':'Crystal Brewer','availability': ["Thursday", "Friday", "Saturday"]}, gamers)
add_gamer({'name':'James Barnes Jr.','availability': ["Tuesday", "Wednesday", "Thursday", "Sunday"]}, gamers)
add_gamer({'name':'Michel Trujillo','availability': ["Monday", "Tuesday", "Wednesday"]}, gamers)

# for key, value in gamers.items():
#     print(key, ' : ', value)

def build_daily_frequency_table():
    return {
            "Monday":    0,
            "Tuesday":   0,
            "Wednesday": 0,
            "Thursday":  0,
            "Friday":    0,
            "Saturday":  0,
            "Sunday":    0,
    }
count_availability = build_daily_frequency_table()

def calculate_availability(gamers_list, available_frequency):
    for gamer in gamers_list:
        for day in gamers["availability"]:
            available_frequency[day] += 1

calculate_availability(gamers, count_availability)
print(count_availability)


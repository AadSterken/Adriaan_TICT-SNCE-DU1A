stations = ['Schagen', 'Heerhugowaard', 'Alkmaar', 'Castricum', 'Zaandam',
            'Amsterdam Sloterdijk', 'Amsterdam Centraal', 'Amsterdam Amstel',
            'Utrecht Centraal', '\’s-Hertogenbosch', 'Eindhoven', 'Weert', 'Roermond', 'Sittard', 'Maastrich']


def inlezen_beginstation(station):
    invoer = input("Vul hier het begin station in:")

    for station in stations:
        if invoer == station:
            print("Begin station: " + station)
            return station
        else:
            if invoer not in stations:
                print("Deze trein komt niet in " + invoer)
                invoer = input("Vul hier het begin station in:")
                return station


beginstation = inlezen_beginstation(stations)


def inlezen_eindstation(stations):
    invoer1 = input("Vul hier het eind station in:")
    for station1 in stations:
        if invoer1 == station1:
            print("Eind station: " + invoer1)
        else:
            if invoer1 not in stations:
                print("Deze trein komt niet in " + invoer1)
                invoer1 = input("Vul hier het eind station in:")

inlezen_eindstation(stations)

# eindstation = inlezen_eindstation(stations)
# inlezen_beginstation(stations)
# omroepen_reis(stations, beginstation, eindstation)
# def omroepen_reis(stations, beginstation, eindstation):
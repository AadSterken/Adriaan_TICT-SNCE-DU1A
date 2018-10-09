bruin = ['Boxtel', 'Best', 'Beukenlaan', 'Eindhoven', 'Helmond \t Hout', 'Helmond', 'Helmond Brouwhuis', 'Deurne']
groen = ['Boxtel', 'Best', 'Beukenlaan', 'Eindhoven', 'Geldrop', 'Heeze', 'Weert']

print(set(bruin).intersection(groen))

print(set(bruin). difference(groen))
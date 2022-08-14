from prettytable import PrettyTable

#cara 1
# table = PrettyTable(["Pokemon Name", "Type"])
# table.add_row(['Pikachu', 'water'])

#cara 2
table = PrettyTable()

table.add_column('Pokemon name', ['Pikachu', 'Charamander'])
table.add_column('Type', ['Water', 'Earth'])

table.align = 'l'


print(table)
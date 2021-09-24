from prettytable import PrettyTable 

table = PrettyTable(["name","test"])

table.add_row(["hello","world"])

print(table)
from prettytable import PrettyTable

table = PrettyTable()
pokemon_name_col = table.add_column("Pokemon",["Pikachu", "Charmander", "Squirtle", "Bellossom"])
pokemon_type_col = table.add_column("Pokemon", ["Electric", "Fire", "Water","Grass"])

table.align = "c"
print(table)
"""
Table looks like this
+------------+----------+
|  Pokemon   | Pokemon  |
+------------+----------+
|  Pikachu   | Electric |
| Charmander |   Fire   |
|  Squirtle  |  Water   |
+------------+----------+
"""


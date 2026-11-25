Llegir un conjunt de dades d'alumnes ficticis i crear un CSV net.
Treballarem quatre problemes habituals:
  1. Valors absents (missing values).
  2. Espais innecessaris abans o després dels valors.
  3. Valors numèrics fora dels rangs permesos.
  4. Registres duplicats, comparant-los amb TUPLES.
  
Escriure conjunt de dades net en arxiu de sortida


--------------------

sales_data = [
    {'Product ID': 'abc123',  'Units Sold': 10,     'Revenue USD': 1250.0, 'Date': '2023-01-01'},
    {'Product ID': 'abc123',  'Units Sold': 10,     'Revenue USD': 1250.0, 'Date': '2023-01-01'},
    {'Product ID': 'abc123 ', 'Units Sold': 10,     'Revenue USD': 1250.0, 'Date': '2023-01-01'},
    {'Product ID': 'XYZ789',  'Units Sold': -5,     'Revenue USD': -300.0, 'Date': '2023-02-15'},
    {'Product ID': None,      'Units Sold': 8,      'Revenue USD': 800.0,  'Date': '2023-03-10'},
    {'Product ID': 'test123', 'Units Sold': 1000,   'Revenue USD': 50000.0,'Date': '2023-03-15'},
    {'Product ID': 'test123', 'Units Sold': 1000,   'Revenue USD': 50000.0,'Date': '2023-03-15'},
    {'Product ID': 'DEF456',  'Units Sold': None,   'Revenue USD': 150.0,  'Date': '2023-03-20'}
]

#Registros originales
"""print("Registros originales\n")
for i, record in enumerate(sales_data):
    print(f"{i+1}. {record}")"""

#eliminamos None
sales_cleaned = [
    record for record in sales_data if record['Product ID'] is not None and record['Units Sold'] is not None
]

#Registros después None
"""print("Registros después eliminar None\n")
for i, record in enumerate(sales_cleaned):
    print(f"{i+1}. {record}")"""

#Eliminamos espacions en blanco en product id
for record in sales_cleaned:
    record['Product ID'] = record['Product ID'].strip().lower()

#Registros eliminar blancos y minúscula
"""print("Registros después eliminar blancos y minuscola\n")
for i, record in enumerate(sales_cleaned):
    print(f"{i+1}. {record}")"""

#eliminamos negativos
sales_cleaned = [
    record for record in sales_cleaned if record['Units Sold'] >= 0 and record['Revenue USD'] >= 0
]

#eliminar negativos
print("Registros después eliminar negativos\n")
for i, record in enumerate(sales_cleaned):
    print(f"{i+1}. {record}")

#eliminamos duplicados

seen = set()
for record in sales_cleaned:
    record_tuple = tuple(record.items())
    #print(record_tuple)
    seen.add(record_tuple)
    
print(seen)

sales_cleaned = [dict(t) for t in seen]

print("Registros después eliminar duplicados\n")
for i, record in enumerate(sales_cleaned):
    print(f"{i+1}. {record}")
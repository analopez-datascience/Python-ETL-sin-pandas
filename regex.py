import re
transactions = [{'transaction_id': 1, 'description': 'Sale of PROD-481a for $299'},
    {'transaction_id': 2, 'description': 'Item PROD-92841 sold'},
    {'transaction_id': 3, 'description': 'Returned Item (PROD-552)'},
    {'transaction_id': 4, 'description': 'Misc sale, no product code'}]

def extract_product_id(description):
    match = re.search(r'(PROD-\w+)', description)
    if match:
        return match.group(1)
    else:
        return None

    for transaction in transactions:    
        product_id = extract_product_id(transaction['description'])
        print(f"Transaction ID: {transaction['transaction_id']}, Product ID: {product_id}")



# %%
import re
text = "Python es facil. Me gusta programar en Python"
re.search(r"Python",text)

# %%
re.search(r"python",text)

# %%
re.search(r"[pP]ython",text)

# %%
text = "Python es facil. Me gusta programar en python"
re.findall(r"[pP]ython",text)

# %%
text = "Tinc 25 anys i visc al carre número 18"
re.findall(r"\d",text)

# %%
len(re.findall(r"\w",text))

# %%
text = "Hola Python 2026! Programació ABC xyz 123"
re.findall(r"[2-7]", text)

# %%
text = "Codis 12 345 6789 12345 7 987654 123"
re.findall(r'\d+', text)

# %%
re.findall(r'\b\d{2,4}\b', text)

# %%
#^inicio, $ final,
paraules = ["Python", "Python3", "Aprendre Python", "Java", "123Python", "Programacio"]

[p for p in paraules if re.search(r"^Python", p)]

# %%
[p for p in paraules if re.search(r"Python$", p)]

# %%
[p for p in paraules if re.search(r"\d$", p)]

# %%
for telefon in ["612345678", "1234"]:
    if re.fullmatch(r"[0-9]{9}", telefon):
        print(telefon, " Format correcte")
    else:
        print(telefon, " Format incorrecte")


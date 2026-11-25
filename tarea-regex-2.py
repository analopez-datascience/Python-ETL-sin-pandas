import re

#['15/10/2026', '1/10/2026']
#['marc@gmail.com', 'marc@com']

dates = ['15/10/2026', '1/10/2026']
for date in dates:
    if re.search(r"\d{1,2}/\d{1,2}/\d{4}", date):
        print(f"{date} és una data vàlida")
    else:
        print(f"{date} no és una data vàlida")

dates = ['15/10/2026', '1/10/2026']
for date in dates:
    re.fullmatch(r"[0-9]{2}/[0-9]{2}/[0-9]{4}", dates)
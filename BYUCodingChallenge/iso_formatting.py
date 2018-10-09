from datetime import datetime

formatted_date = datetime.strptime("20180122", "%Y%m%d").date().isoformat()
print(formatted_date)


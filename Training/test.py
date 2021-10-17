from datetime import date, timedelta

days = []
for i in range(181):
    days.append((date.today() - timedelta(days=i)).isoformat())

print(days)
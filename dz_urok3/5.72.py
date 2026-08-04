current_km = 10
percent = 10
finish_day = 10
i = 1
total_km_7_days = 10

while i <= finish_day:
    current_km = current_km + (current_km*percent/100)
    print(f"текущий день = {i} текущий пробег = {current_km:.2f}")
    i += 1

    if i <= 7:
        total_km_7_days += current_km

print(f"за первые семь дней он пробежал {total_km_7_days:.2f}")
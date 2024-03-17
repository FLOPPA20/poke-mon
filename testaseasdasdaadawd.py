from datetime import datetime, timedelta

# Создание объекта даты и времени
now = datetime.now()

# Вывод текущей даты и времени
print("Текущая дата и время:", now)
# Создание объекта даты и времени
start_date = datetime.now()

# Добавление интервала времени к дате
future_date = start_date + timedelta(days=7)

# Вывод будущей даты
print("Дата через 7 дней:", future_date)
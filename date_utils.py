import datetime

def count_days_till_deadline():
    while True:
        year_month_day = input('Введите дату дедлайна: ')

        if len(year_month_day) == 10 and year_month_day[0:4].isdigit and year_month_day[4] == '-' and year_month_day[5:7].isdigit() and year_month_day[7] == '-' and year_month_day[8:].isdigit() and 1 <= int(year_month_day[5:7]) <= 12 and 1 <= int(year_month_day[8:]) <= 31:
            date_obj = datetime.date.fromisoformat(year_month_day)
        else:
            print('Неправильный формат даты')
            continue

        today_date = datetime.date.today()

        if date_obj < today_date:
            print('Введите дату позже сегодняшней')
            continue
        else:
            deadline_count = (date_obj - today_date).days

            if deadline_count < 7:
                print('До дедлайна меньше недели!\n')

            return print(f'{deadline_count} дней до дедлайна')
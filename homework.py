import datetime as dt


class Calculator:
    def __init__(self, limit):
        self.limit = limit
        self.records = []

    def add_record(self, record):
        self.records.append(record)

    def get_today_stats(self):
        today = dt.date.today()
        day_sum = sum([
            record.amount for record in self.records
            if record.date == today 
        ])
        return day_sum
        
    def get_week_stats(self):
        start_date = dt.date.today() - dt.timedelta(days=7)
        week_sum = sum([
            record.amount for record in self.records
            if dt.date.today() >= record.date > start_date
        ])
        return week_sum

    def difference(self):
        return self.limit - self.get_today_stats()


class Record:
    def __init__(self, amount, comment, date=None):
        self.amount = amount
        self.comment = comment
        self.date = date
        if date is None:
            self.date = dt.date.today()
        else:
            self.date = dt.datetime.strptime(date, '%d.%m.%Y').date()


class CashCalculator(Calculator):
    USD_RATE = float(60)
    EURO_RATE = float(70)
    currency_dict = {
        'usd': (USD_RATE, 'USD'),
        'eur': (EURO_RATE, 'Euro'),
        'rub': (1, 'руб')
        }
    zero = 'Денег нет, держись'
    dept = 'Денег нет, держись: твой долг -'
    positive = 'На сегодня осталось'

    def get_today_cash_remained(self, currency):
        difference = self.difference()
        if difference == 0:
            return self.zero
        balance = difference / self.currency_dict[currency][0]
        result = abs(round(balance, 2))
        currency_name = self.currency_dict[currency][1]
        if difference > 0:
            return f"{self.positive} {result} {currency_name}"
        if difference < 0:
            return f"{self.dept} {result} {currency_name}"


class CaloriesCalculator(Calculator):
    def get_calories_remained(self): 
        remained = self.difference()
        if remained <= 0:
            return "Хватит есть!"
        if remained > 0:
            return ("Сегодня можно съесть что-нибудь ещё, " 
            f"но с общей калорийностью не более {remained} кКал")
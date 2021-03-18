class CashCalculator(Calculator):
    EUR_RATE: float = 85
    USD_RATE: float = 72

    def __init__(self, limit: float,  EUR_RATE, USD_RATE):
        super().__init__(limit)
        self.currency = currency
        self.EUR_RATE = EUR_RATE
        self.USD_RATE = USD_RATE
            
    def get_today_cash_remained(self, currency: str):
                
        if currency == 'rub':        
            self.limit=self.limit-self.get_today_status()
            if self.limit > 0:
                print(f'На сегодня осталось {self.limit} руб.')
            elif self.limit == 0:             
                print(f'Денег нет, держись {self.limit}  руб.')
            else:             
                print(f'Денег нет, держись: твой долг - {self.limit*(-1)} руб.') 
        
                            
        if currency == 'eur':        
            self.limit=round((self.limit-self.get_today_status())/self.EUR_RATE, 2)
            if self.limit > 0:
                print (f'На сегодня осталось {self.limit} eur.')
            elif self.limit == 0:
                print(f'Денег нет, держись {self.limit} eur.')
            else:
                print(f'Денег нет, держись: твой долг - {self.limit*(-1)} eur.')
                   
        if currency == 'usd':        
            self.limit=round((self.limit-self.get_today_status())/self.USD_RATE, 2)
            if self.limit > 0:
                print(f'На сегодня осталось {self.limit} usd')
            elif self.limit == 0:
                print(f'Денег нет, держись {self.limit} usd.')
            else:
                print(f'Денег нет, держись: твой долг - {self.limit*(-1)} usd.')
            
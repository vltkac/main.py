class CreditCardPayment:
    def __init__(self, currency: str):
        self.currency = currency.strip().upper()

    def pay(self, amount: (int, float)):
        try:
            if float(amount) < 0:
                raise ValueError
        except ValueError:
            print('Invalid format. Please use only digits and \'.\'')
            return None

        print(f'Card payment was confirmed: {amount} {self.currency}')
        return None


class PayPalPayment:
    def __init__(self, currency: str):
        self.currency = currency.strip().upper()

    def pay(self, amount: (int, float)):
        try:
            if float(amount) < 0:
                raise ValueError
        except ValueError:
            print('Invalid format. Please use only digits and \'.\'')
            return None

        print(f'PayPal payment was confirmed: {amount} {self.currency}')
        return None


class CryptoPayment:
    def __init__(self, currency: str):
        self.currency = currency.strip().upper()

    def pay(self, amount: (int, float)):
        try:
            if float(amount) < 0:
                raise ValueError
        except ValueError:
            print('Invalid format. Please use only digits and \'.\'')
            return None

        print(f'Crypto payment was confirmed: {amount} {self.currency}')
        return None


payment_methods_print = ['CreditCardPayment', 'PayPalPayment', 'CryptoPayment']

payment_methods = {'creditcardpayment': CreditCardPayment,
                    'paypalpayment': PayPalPayment,
                    'cryptopayment': CryptoPayment
                   }

payments = []


def create_payment():
    print(f'Available payment methods: {', '.join(payment_methods_print)}')

    try:
        wallet_type = input('Please specify a wallet type: ').strip().lower()
        operation_currency = input('Please specify a currency: ').strip()

        new_payment = payment_methods[wallet_type](operation_currency)
        payments.append(new_payment)
        return new_payment
    except KeyError:
        print('Payment method unknown')
        return None


create_payment()
create_payment()
create_payment()

for i, payment in enumerate(payments):
    operation_amount = input(f'[Transaction {i + 1}] Please type a sum in {payment.currency}: ').strip()

    payment.pay(operation_amount)
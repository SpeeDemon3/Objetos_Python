class Customer:

    id = 1

    def __init__(self,  name, account_balance):
        self.id = Customer.id
        Customer.id += 1
        self.name = name
        self.account_balance = account_balance

    def check_account_balance(self):
        print(f"{self.name}'s balance is {self.account_balance}")


customer = Customer('Antonio', 20000)
customer_2 = Customer('Chula', 200002)




print(customer.id)
print(customer_2.id)
print(customer_2.check_account_balance())

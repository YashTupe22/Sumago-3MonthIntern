class Bank:
    def account(self,acc_no ,bal):
        print(f"Welcome Detail of {acc_no} and Balance is {bal}")

class Update_bal(Bank):
    def up_bal(self,upbal):
        print(f"New Balance is")

class view(Update_bal):
    def view(self):
        print("Thank you for using us")

a = view()
a.account(1,500)
a.up_bal(500)
a.view()
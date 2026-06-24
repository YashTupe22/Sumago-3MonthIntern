from abc import ABC,abstractmethod

class Subscription(ABC):
    def __init__(self,User_Name,Monthly_Fee):
        self.User_Name = User_Name
        self.__Monthly_Fee = Monthly_Fee

    @abstractmethod
    def show_features(self):
        pass

    def show_plan_details(self):
        print(f"Plan Details\n1.User Name: {self.User_Name}\n2.Monthly Fee: {self.__Monthly_Fee}")

class BasicPlan(Subscription):
    def __init__(self, User_Name, Monthly_Fee):
        super().__init__(User_Name, Monthly_Fee)

    def show_features(self):
        print("Message!!\nBasic Plan Features")
        print("1. SD Quality")
        print("2. Single Device Access")
        return super().show_plan_details()

class StandardPlan(Subscription):
    def __init__(self, User_Name, Monthly_Fee):
        super().__init__(User_Name, Monthly_Fee)

    def show_features(self):
        print("Message!!\nStandard Plan Features")
        print("1. HD Quality")
        print("2. Two Device Access")
        print("3. Download Available")
        return super().show_plan_details()

class PremiumPlan(Subscription):
    def __init__(self, User_Name, Monthly_Fee):
        super().__init__(User_Name, Monthly_Fee)

    def show_features(self):
        print("Message!!\nPremium Plan Features")
        print("1. Ultra HD Quality")
        print("2. Four Device Access")
        print("3. Download Available")
        print("4. Ad Free Streaming")
        return super().show_plan_details()

User_Name = input("Enter User Name: ")
Monthly_Fee = int(input("Enter Monthly Fee: "))

Plan = int(input("Select Plan\n1.Basic Plan\n2.Standard Plan\n3.Premium Plan\n"))

if Plan == 1:
    M = BasicPlan(User_Name,Monthly_Fee)
    M.show_features()
elif Plan == 2:
    M = StandardPlan(User_Name,Monthly_Fee)
    M.show_features()
elif Plan == 3:
    M = PremiumPlan(User_Name,Monthly_Fee)
    M.show_features()
else:
    print("Wrong Information!!")
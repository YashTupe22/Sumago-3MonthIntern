# Child Classes
# •	BasicPlan 
# •	StandardPlan 
# •	PremiumPlan 
# Requirements
# •	Use super() constructor. 
# •	Different features for each plan. 
# •	Fee should be private. 
from abc import ABC, abstractmethod

class Subscription(ABC):
    def __init__(self, user_name, monthly_fee):
        self.user_name = user_name
        self.__monthly_fee = monthly_fee

    @abstractmethod
    def show_features(self):
        pass

    def show_plan_details(self):
        print(f"User Name: {self.user_name}")
        print(f"Monthly Fee: {self.__monthly_fee}")

# Child Classes
# •	BasicPlan 
# •	StandardPlan 
# •	PremiumPlan 
class Basic
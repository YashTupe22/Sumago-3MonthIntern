from abc import ABC,abstractmethod

class Patient(ABC):
    def __init__(self,patient_id,patient_name,Treatment_cost):
        self.patient_id = patient_id
        self.patient_name = patient_name
        self.__Treatment_cost = Treatment_cost
    @abstractmethod
    def generate_bill(self):
        pass

    def patient_details(self):
        print(f"Patient Details\n1.Patient Id: {self.patient_id}\n2.Patient Name: {self.patient_name}")

class GeneralPatient(Patient):
    def __init__(self, patient_id, patient_name, Treatment_cost):
        super().__init__(patient_id, patient_name, Treatment_cost)
    
    def generate_bill(self):
        bb = 5000
        super().patient_details()
        print(f"3.Total bill: {self._Patient__Treatment_cost+bb}")

class ICUPatient(Patient):
    def __init__(self, patient_id, patient_name, Treatment_cost):
        super().__init__(patient_id, patient_name, Treatment_cost)
    
    def generate_bill(self):
        bb = 15000
        super().patient_details()
        print(f"3.Total bill: {self._Patient__Treatment_cost+bb}")

class EmergencyPatient(Patient):
    def __init__(self, patient_id, patient_name, Treatment_cost):
        super().__init__(patient_id, patient_name, Treatment_cost)
    
    def generate_bill(self):
        bb = 25000
        super().patient_details()
        print(f"3.Total bill: {self._Patient__Treatment_cost+bb}")
Patient_id = int(input("Enter your Patient ID: "))
Patient_Name = input("Enter your name: ")
Treatment_cost = int(input("Enter your Treatment cost: "))
type = int(input("What is patient type\n1.General Patient\n2.ICU Patient\n3.Emergency Patient"))
if type == 1:
    M = GeneralPatient(Patient_id,Patient_Name,Treatment_cost)
    M.generate_bill()
elif type == 2:
    D = ICUPatient(Patient_id,Patient_Name,Treatment_cost)
    D.generate_bill()
elif type == 3:
    I = EmergencyPatient(Patient_id,Patient_Name,Treatment_cost)
    I.generate_bill()
else:
    print("Wrong Information!!")
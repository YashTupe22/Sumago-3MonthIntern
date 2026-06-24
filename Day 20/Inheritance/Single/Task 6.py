class Patient:
    def fetch(self,patient_name,age):
        self.name = patient_name
        self.age = age

class InPatient(Patient):
    def inpatient(self,room_no):
        self.room_no = room_no
        print(f"\tDetails\n1.Name: {self.name}\n2.Age: {self.age}\n3.Room no: {room_no}")

name = input("Enter patient name: ")
age = int(input("Enter age: "))
room_no = int(input("Enter room no: "))
i=InPatient()
i.fetch(name,age)
i.inpatient(room_no)
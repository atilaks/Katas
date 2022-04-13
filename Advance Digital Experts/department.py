import random


class Department:

    def __init__(self):
        self._department = ["departmentA", "departmentB"]
        self.available_department = False

    def set_department_availability(self):
        if self.available_department:
            self.available_department = False
        else:
            self.available_department = True

    def set_department(self):
        if self.available_department:
            assignment = self.get_random_departments()
        else:
            assignment = "not assigned"
        return assignment

    def get_random_departments(self):
        return self._department[random.randint(0, len(self._department))]

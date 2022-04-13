class Department:

    def __init__(self):
        self._department = ["departmentA", "departmentB"]
        self.available_department = True

    def set_department(self, new_department):
        self._department.append(new_department)

    def get_department(self):
        return self._department

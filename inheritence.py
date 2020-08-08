class employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
        print("Employee\'s name is {} and his salary is{}".format(name,salary))

class company(employee):
    def staff(staff,name,salary):
        employee.__init__(self,name,salary)

class profession(employee):
    def developer(staff,name,salary):
        employee.__init__(self,name,salary)

e=employee('shri',2000)
em=company('prabhu',1111)
pr=profession('gaur',1000)



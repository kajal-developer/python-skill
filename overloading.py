class employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    def __str__(self):
        return("Employee\'s name is: {} and his salary is{}".format(self.name,self.salary))


class company(employee):
    def __init__(self,name,salary,age):
        employee.__init__(self,name,salary)
        self.age=age
    def __str__(self):
        return(employee.__str__(self)+'and his age is:{}'.format(self.age))


class profession(employee):
    def __init__(self,name,salary,budget):
        employee.__init__(self,name,salary)
        self.budget=budget
    def __str__(self):
        return(employee.__str__(self)+'and his budget is:{}'.format(self.budget))

co=company('priya',2000,28)
pro=profession('shreya',3000,20000)
print(co)
print(pro)



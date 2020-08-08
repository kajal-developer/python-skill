class employee:
    def staff(self,name,salary):
        self.name=name
        self.salary=salary
        print("Employee\'s name is {} and his salary is{}".format(name,salary))


em=employee()
(em.staff('paul',10000))
#as we have given self.name nd self.salary values so now we can rum below command
print(em.salary)

#construtor method
class college:
    def __init__(self,branch,year):
        self.branch=branch
        self.year=year
        print("branch is {} and {} year".format(branch,year))

clg=college('cse','third')


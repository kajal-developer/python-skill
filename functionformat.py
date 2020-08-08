n='kajal'
a=19
g=85.5


print('student\'s name is {} and age is {} and grade is {}'.format(n,a,g))

print('student\'s name is {2} and age is {1} and grade is {0}'.format(g,a,n))
print('student\'s name is {:10} and age is {:5} and grade is {:15}'.format(n,a,g))
for i in range(1,11):
    print("{:5}{:10}{:10}".format(i,i*i,i*i*i))
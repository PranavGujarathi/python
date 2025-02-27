class College:
    collegename="SCOE"    # static variable ( 1 memory)
    def __init__(self):
        self.studentname="Pranav"   # instance variable (3 seperate memory )
    

principal=College()  # objet creation 
teacher = College()
accountant = College()


print('principal: ',principal.collegename,"....",principal.studentname)
print('teacher: ',teacher.collegename,"....",teacher.studentname)
print('accountant: ',accountant.collegename,"....",accountant.studentname)

College.collegenmae="BNN"
principal.studentname="Pranav"

print('principal: ',principal.collegename,"|",principal.studentname)
print('teacher: ',teacher.collegename,"|",teacher.studentname)
print('accountant: ',accountant.collegename,"|",accountant.studentname)


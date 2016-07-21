from models import *

for i in range(0,9):
    City.create(name='City' + str(i))
    Applicant.create(name='Proba_Baba_' + str(i), application_code=0, home=1)

for x in Applicant.select():
    print(x.name)

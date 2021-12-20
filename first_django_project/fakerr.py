import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','first_django_project.settings')

import django
django.setup()

from myApp.models import My_User
from faker import Faker

fake=Faker()

def f_loop(n=10):
    for i in range(n):

        fname = fake.first_name()
        lname = fake.last_name()
        f_email = fake.email()

        user=My_User.objects.get_or_create(First_Name = fname,Last_Name = lname,Email=f_email)[0]

if __name__=='__main__':
    print("faking script!")
    f_loop(20)
    print("faking complete!")
from django.contrib.auth.models import User
from django.db import models





# Create your models here.



class Department(models.Model):

    name = models.CharField(max_length=100)
    acronym = models.CharField(max_length=10)
    code = models.CharField(max_length=100)
    estd = models.DateTimeField()
    location = models.CharField(max_length=100)



class hodregister (models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()

    department = models.CharField(max_length=100)
    mobile = models.IntegerField()
    designation = models.CharField(max_length=500)

    user  = models.ForeignKey(
        User,on_delete=models.CASCADE,blank=True,null=True)




class Personal_Details(models.Model):
    firstname = models.CharField(max_length=100)
    middlename = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    dateofbirth = models.DateField()
    emailid = models.EmailField()
    mobile = models.IntegerField()
    alternatemobile = models.IntegerField()
    aadharnumber = models.IntegerField()
    pancardnumber = models.IntegerField()
    bloodgroup  = models.CharField(max_length=60)
    street = models.CharField(max_length=200)
    pincode = models.IntegerField()
    city = models.CharField(max_length=200)
    district = models.CharField(max_length=200)
    state =  models.CharField(max_length=200)
    dateofjoining = models.DateField(max_length=200)
    departmentname =  models.CharField(max_length=200)
    designation = models.CharField(max_length=200)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)




class Bachelorss_Degree (models.Model):
    degreename = models.CharField(max_length=400)
    collegename = models.CharField(max_length=400)
    University = models.CharField(max_length=400)
    yearofpassing = models.CharField(max_length=500)
    result = models.CharField(max_length=600)
    percentage = models.CharField(max_length=100)
    emailid = models.EmailField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

class Masterss_degree (models.Model):
    degreename = models.CharField(max_length=400)
    collegename = models.CharField(max_length=400)
    University = models.CharField(max_length=400)
    yearofpassing = models.CharField(max_length=500)
    result = models.CharField(max_length=600)
    percentage = models.CharField(max_length=100)
    emailid = models.EmailField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)


class Phds_Degree (models.Model):
    degreename = models.CharField(max_length=400)
    collegename = models.CharField(max_length=400)
    University = models.CharField(max_length=400)
    specification  = models.CharField(max_length=500)
    yearofpassing = models.CharField(max_length=500)
    result = models.CharField(max_length=600)
    percentage = models.CharField(max_length=100)
    emailid = models.EmailField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)


class Experiences_Details (models.Model):
    institutename = models.CharField(max_length=600)
    joiningdate = models.DateField()
    designation = models.CharField(max_length=600)
    hikename = models.CharField(max_length=600)
    scale = models.CharField(max_length=600)
    enddate = models.DateField()
    address = models.CharField(max_length=600)
    state = models.CharField(max_length=600)
    emailid = models.EmailField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)


class Publications_Details (models.Model):
    titleofpublication = models.CharField(max_length=600)
    authorname = models.CharField(max_length=600)
    year = models.DateField()
    titleofpaper = models.CharField(max_length=600)
    volume = models.CharField(max_length=600)
    pagenumbers = models.CharField(max_length=600)
    impact = models.CharField(max_length=600)
    reviewer = models.CharField(max_length=600)
    journalname = models.CharField(max_length=600)
    emailid = models.EmailField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

class Patentss_Details(models.Model):
    title = models.CharField(max_length=600)
    name = models.CharField(max_length=600)
    holder = models.CharField(max_length=600)
    datesubmitprovisional = models.DateField()
    datesubmitcomplete = models.DateField()
    datepublication = models.DateField()
    remarks = models.CharField(max_length=800)
    emailid = models.EmailField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)


class Grantss_Fetched(models.Model):
    projectname = models.CharField(max_length=600)
    grantissuedby = models.CharField(max_length=600)
    grantedamount = models.IntegerField()
    grantdate = models.DateField()
    coauthors = models.CharField(max_length=900)
    address = models.CharField(max_length=200)
    description = models.CharField(max_length=900)
    emailid = models.EmailField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

class Grantss_Applied(models.Model):
    date = models.DateField()
    projectname = models.CharField(max_length=600)
    agency = models.CharField(max_length=600)
    grantamount = models.IntegerField()
    address = models.CharField(max_length=200)
    description = models.CharField(max_length=900)
    emailid = models.EmailField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

class Awardss_Details(models.Model):
    awardname = models.CharField(max_length=600)
    awardinstitution = models.CharField(max_length=600)
    date = models.DateField()
    description = models.CharField(max_length=900)
    emailid = models.EmailField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)


class Workshops_Details(models.Model):
    presentationlevel = models.CharField(max_length=300)
    type = models.CharField(max_length=400)
    sourceoffunding = models.CharField(max_length=400)
    paper = models.CharField(max_length=400)
    name= models.CharField(max_length=400)
    description = models.CharField(max_length=900)
    country = models.CharField(max_length=900)
    state = models.CharField(max_length=400)
    startdate = models.DateField()
    date = models.DateField()
    hostorganization = models.CharField(max_length=900)
    eventname = models.CharField(max_length=900)
    area = models.CharField(max_length=900)
    resourceperson = models.CharField(max_length=600)
    place = models.CharField(max_length=900)
    numberofparticipants = models.IntegerField()
    briefdescription = models.CharField(max_length=990)
    amountfaculty = models.IntegerField()
    modeofpayment = models.CharField(max_length=600)
    amountuniversity = models.CharField(max_length=900)
    emailid = models.EmailField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

class Banks_Details(models.Model):
     bankname = models.CharField(max_length=900)
     accountnumber = models.IntegerField()
     branchname = models.CharField(max_length=900)
     ifsccode = models.CharField(max_length=900)
     city = models.CharField(max_length=900)
     state = models.CharField(max_length=900)
     emailid = models.EmailField()
     user = models.ForeignKey(User, on_delete=models.CASCADE)
     created = models.DateTimeField(auto_now_add=True)
     updated = models.DateTimeField(auto_now_add=True)


class Courses_Details(models.Model):
    name = models.CharField(max_length=400)
    code = models.CharField(max_length=500)
    credit = models.IntegerField()
    created = models.DateField()
    department = models.CharField(max_length=600)
    semester = models.IntegerField()
    coursedescription = models.CharField(max_length=600)


class facultydetails(models.Model):
    name = models.CharField(max_length=500)
    email = models.EmailField()
    department = models.CharField(max_length=700)
    mobile = models.IntegerField()
    joining = models.DateField()
    facultycourse = models.CharField(max_length=500)
    designation = models.CharField(max_length=700)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, blank=True, null=True)

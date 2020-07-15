# Create your views here.
import json

from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from mysite.common_utils import CommonUtils
from staff.forms import personaldetailsForm, bachelordetailsForm, \
    masterdetailsForm, phddetailsForm, experiencedetailsForm, publicationdetailsForm, workshopdetailsForm, \
    patentsdetailsForm, grantsfetchedForm, grantsappliedForm, awardsdetailsForm, bankdetailsForm, coursedetailsForm, \
    facultydetailsForm, registerForm44
from staff.forms import DepartmentForm
from django.http.response import HttpResponseRedirect
from staff.models import Department, hodregister, Personal_Details, facultydetails, Bachelorss_Degree, \
    Experiences_Details, \
    Publications_Details, Masterss_degree, Phds_Degree, Workshops_Details, Patentss_Details, Grantss_Fetched, \
    Grantss_Applied, Awardss_Details, Banks_Details, Courses_Details
from django.contrib import messages


# Create your views here.


#
def viwer(request):
    return HttpResponseRedirect('/staff/dashboard')


# to view the login page for Admin
def log(request):
    return render(request, 'login4.html')


# view to come back Admin dashboard
def backk(request):
    return render(request, 'dashboard.html')


# view to modfiy password in faculty
def change_password(request):
    if request.method == 'POST':
        old_password = request.POST['password']
        new_password = request.POST['new_password']
        User.objects.filter(
            password__iexact=old_password).update(
            password=new_password)
        return render(request,'changepassword.html')
    else:
        return render(request,
                      'changepassword.html')

# to view login page for HOD
def log2(request):
    return render(request, 'login5.html')


# to view login page for Faculty
def log3(request):
    return render(request, 'login6.html')


def log4(request):
    return render(request, 'login5.html')


# TO view details of Faculties in HOD dashboard
def view_Faculty(request):
    if request.method == 'GET':
        queryset = facultydetails.objects.filter(designation='professor').only("name", "department", "email", "mobile",
                                                                        "facultycourse", "designation")

        return render(request, 'viewFaculty.html',
                      {'staff': queryset})


# view for courses in HOd dashboard
def view_course(request):
    if request.method == 'GET':
        queryset = Courses_Details.objects.filter(department='MCA').only("name", "code", "credit", "created",
                                                                        "department", "semester")
        return render(request, 'viewcourse.html',
                      {'staff': queryset})



# view faculty report in HOD dashboard
def view_Report(request):
    return render(request, 'viewReport.html')


def homes(request):
    return render(request, 'homepage.html')


# To view a home page
def hp(request):
    return render(request, 'homepage.html')


def faculty_home(request):
    return render(render, 'facultydashboard.html')


# To view HOD dashboard
def hod_dashboard(request):
    return render(request, 'dashboard2.html')


# ---------------------------------------------------------------------------------------------------

# login view(login code) for Admin dashboard
def seen(request):
    if request.method == 'GET':
        return render(request, 'login4.html')
    else:
        validate_user = authenticate(
            username=request.POST['username'],
            password=request.POST['password'])
        if validate_user:
            login(request, validate_user)
            return render(request, 'dashboard.html')
        else:
            messages.success(request, 'Invalid password!!')
            return render(request, 'login4.html')


# --------------------------------------------------------------------------------------------

# login view (login code) for Faculty dashboard
def seener(request):
    if request.method == 'GET':
        return render(request, 'login6.html')
    else:
        validate_user = authenticate(
            username=request.POST['username'],
            password=request.POST['password'])
        if validate_user:
            login(request, validate_user)
            return render(request, 'facultydashboard.html')
        else:
            messages.success(request, 'Invalid password!!')
            return render(request, 'login6.html')


# login view(login code) for HOD Dashboard
def seens(request):
    if request.method == 'GET':
        return render(request, 'login5.html')
    else:
        validate_user = authenticate(
            username=request.POST['username'],
            password=request.POST['password'])
        if validate_user:
            login(request, validate_user)
            return render(request, 'dashboard2.html')
        else:
            messages.success(request, 'Invalid password!!')
            return render(request, 'login5.html')


# view to insert department in Admin dashboard
def insert_department(request):
    if request.method == 'POST':
        department_form = DepartmentForm(request.POST)
        if department_form.is_valid():
            post_department = department_form.save(commit=False)
            post_department.save()
            messages.success(request, 'Department Added SUCCESSFULLY!!')
            return HttpResponseRedirect('/staff/adddept')
    if request.method == 'GET':
        return render(request, 'adddept.html')


# view to add HODS in Admin dashboard
def insert_hod(request):
    if request.method == 'POST':
        department_form = registerForm44(request.POST)
        if department_form.is_valid():
            new_user = User.objects.create_user(
                username=request.POST['email'],
                password=request.POST['password'])

            post_department = department_form.save(commit=False)
            post_department.user = new_user

            post_department.save()
            messages.success(request, 'HOD Added SUCCESSFULLY!!')
            return HttpResponseRedirect('/staff/addhod')
    if request.method == 'GET':
        return render(request, 'addhod.html')


# TO view all departments in Admin dashboard
def depttview(request):
    if request.method == 'GET':
        department = list(Department.objects.all())
        return render(request, 'view.html',
                      {'staff': department})


# TO view all HOD dept:MCA in Admin dashboard
def view_hod(request):
    if request.method == 'GET':
        queryset = hodregister.objects.filter(designation='HOD', department='MCA').only("name", "department","email","mobile")
        return render(request, 'viewhod.html',
                      {'staff': queryset})


# TO delete the department iin Admin dashboard
def dept_delete(request):
    if request.method == 'POST':
        acronym = request.POST['acronym']
        Department.objects.filter(
            acronym__iexact=acronym
        ).delete()
        return HttpResponseRedirect('/staff/deptdelete')
    else:
        return render(request,
                      'deptdelete.html')


# view to insert personl details of faculty in faclty dashboard

def insert_personal(request):
    message = ''
    priority = ''
    title = ''
    if request.method == 'POST':
        personaldetails_form = personaldetailsForm(request.POST)
        print(personaldetails_form.errors)
        if personaldetails_form.is_valid():
            if request.POST['edit_personaldetails']:
                if Personal_Details.objects.filter(
                        mobile=request.POST['mobile']).count() > 1:
                    message = 'Data Exists!!'
                    priority = 'error'
                    title = 'Data already exists'
                    personaldetails_records = CommonUtils().fetch_department(str(request.user))
                    return render(request, 'personal.html',
                                  {'personaldetails_records': personaldetails_records,
                                   'message': message, 'title': title,
                                   'priority': priority})
                personaldetails_content = {
                    'firstname': request.POST['firstname'],
                    'middlename': request.POST['middlename'],
                    'lastname': request.POST['lastname'],
                    'dateofbirth': request.POST['dateofbirth'],
                    'emailid': request.POST['emailid'],
                    'mobile': request.POST['mobile'],
                    'alternatemobile': request.POST['alternatemobile'],
                    'aadharnumber': request.POST['aadharnumber'],
                    'pancardnumber': request.POST['pancardnumber'],
                    'bloodgroup': request.POST['bloodgroup'],
                    'street': request.POST['street'],
                    'pincode': request.POST['pincode'],
                    'city': request.POST['city'],
                    'district': request.POST['district'],
                    'state': request.POST['state'],
                    'dateofjoining': request.POST['dateofjoining'],
                    'departmentname': request.POST['departmentname'],
                    'designation': request.POST['designation'],
                }
                Personal_Details.objects.filter(
                    id=request.POST['edit_personaldetails']).update(
                    **personaldetails_content)
                message = 'Data Updated !!'
                priority = 'success'
                title = 'Data updated'
            else:
                if Personal_Details.objects.filter(
                        mobile=request.POST['mobile']).count() > 1:
                    message = 'Data Exists!!'
                    priority = 'error'
                    title = 'Data already exists'
                    personaldetails_records = CommonUtils().fetch_department(str(request.user))
                    return render(request, 'personal.html',
                                  {'personaldetails_records': personaldetails_records,
                                   'message': message, 'title': title,
                                   'priority': priority})
                post_personaldetails = personaldetails_form.save(commit=False)
                post_personaldetails.user = request.user
                post_personaldetails.save()
                message = 'Data saved !!'
                priority = 'success'
                title = 'Data saved'
            personaldetails_records = CommonUtils().fetch_department(str(request.user))
            return render(request, 'personal.html',
                          {'personaldetails_records': personaldetails_records,
                           'message': message, 'title': title,
                           'priority': priority})
    if request.method == 'GET':
        personaldetails_records = CommonUtils().fetch_department(str(request.user))
        return render(request, 'personal.html',
                      {'personaldetails_records': personaldetails_records,
                       'message': message, 'title': title,
                       'priority': priority})


# view to inseert bachelor degree details of faculty in faculty dashboard
def add_bachelor(request):
    message = ''
    priority = ''
    title = ''
    if request.method == 'POST':
        bachelordetails_form = bachelordetailsForm(request.POST)
        print(bachelordetails_form.errors)
        if bachelordetails_form.is_valid():
            if request.POST['edit_bachelordetails']:
                if Bachelorss_Degree.objects.filter(
                        degreename=request.POST['degreename']).count() > 1:
                    message = 'Data Exists!!'
                    priority = 'error'
                    title = 'Data already exists'
                    bachelordetails_records = CommonUtils().fetch_bachelor(str(request.user))
                    return render(request, 'bachelor.html',
                                  {'bachelordetails_records': bachelordetails_records,
                                   'message': message, 'title': title,
                                   'priority': priority})
                bachelordetails_content = {
                    'degreename': request.POST['degreename'],
                    'collegename': request.POST['collegename'],
                    'University': request.POST['University'],
                    'yearofpassing': request.POST['yearofpassing'],
                    'result': request.POST['result'],
                    'percentage': request.POST['percentage'],

                }
                Bachelorss_Degree.objects.filter(
                    id=request.POST['edit_bachelordetails']).update(
                    **bachelordetails_content)
                message = 'Data Updated !!'
                priority = 'success'
                title = 'Data updated'
            else:
                if Bachelorss_Degree.objects.filter(
                        degreename=request.POST['degreename']).count() > 1:
                    message = 'Data Exists!!'
                    priority = 'error'
                    title = 'Data already exists'
                    bachelordetails_records = CommonUtils().fetch_bachelor(str(request.user))
                    return render(request, 'bachelor.html',
                                  {'bachelordetails_records': bachelordetails_records,
                                   'message': message, 'title': title,
                                   'priority': priority})
                post_bachelordetails = bachelordetails_form.save(commit=False)
                post_bachelordetails.user = request.user
                post_bachelordetails.save()
                message = 'Data saved !!'
                priority = 'success'
                title = 'Data saved'
            bachelordetails_records = CommonUtils().fetch_bachelor(str(request.user))
            return render(request, 'bachelor.html',
                          {'bachelordetails_records': bachelordetails_records,
                           'message': message, 'title': title,
                           'priority': priority})
    if request.method == 'GET':
        bachelordetails_records = CommonUtils().fetch_bachelor(str(request.user))
        return render(request, 'bachelor.html',
                      {'bachelordetails_records': bachelordetails_records,
                       'message': message, 'title': title,
                       'priority': priority})


def view_personal(request):
    return render(request, 'facultyview.html')


# view to inseert master degree details of faculty in faculty dashboard
def add_master(request):
    message = ''
    priority = ''
    title = ''
    if request.method == 'POST':
        masterdetails_form = masterdetailsForm(request.POST)
        print(masterdetails_form.errors)
        if masterdetails_form.is_valid():
            if request.POST['edit_masterdetails']:
                if Masterss_degree.objects.filter(
                        degreename=request.POST['degreename']).count() > 1:
                    message = 'Data Exists!!'
                    priority = 'error'
                    title = 'Data already exists'
                    masterdetails_records = CommonUtils().fetch_master(str(request.user))
                    return render(request, 'master.html',
                                  {'masterdetails_records': masterdetails_records,
                                   'message': message, 'title': title,
                                   'priority': priority})
                personaldetails_content = {
                    'degreename': request.POST['degreename'],
                    'collegename': request.POST['collegename'],
                    'University': request.POST['University'],
                    'yearofpassing': request.POST['yearofpassing'],
                    'result': request.POST['result'],
                    'percentage': request.POST['percentage'],
                    'emailid': request.POST['emailid'],

                }
                Masterss_degree.objects.filter(
                    id=request.POST['edit_masterdetails']).update(
                    **personaldetails_content)
                message = 'Data Updated !!'
                priority = 'success'
                title = 'Data updated'
            else:
                if Masterss_degree.objects.filter(
                        degreename=request.POST['degreename']).count() > 1:
                    message = 'Data Exists!!'
                    priority = 'error'
                    title = 'Data already exists'
                    masterdetails_records = CommonUtils().fetch_master(str(request.user))
                    return render(request, 'master.html',
                                  {'masterdetails_records': masterdetails_records,
                                   'message': message, 'title': title,
                                   'priority': priority})
                post_personaldetails = masterdetails_form.save(commit=False)
                post_personaldetails.user = request.user
                post_personaldetails.save()
                message = 'Data saved !!'
                priority = 'success'
                title = 'Data saved'
            masterdetails_records = CommonUtils().fetch_master(str(request.user))
            return render(request, 'master.html',
                          {'masterdetails_records': masterdetails_records,
                           'message': message, 'title': title,
                           'priority': priority})
    if request.method == 'GET':
        masterdetails_records = CommonUtils().fetch_master(str(request.user))
        return render(request, 'master.html',
                      {'masterdetails_records': masterdetails_records,
                       'message': message, 'title': title,
                       'priority': priority})


# view to inseert phd degree details of faculty in faculty dashboard
def add_phd(request):
    message = ''
    priority = ''
    title = ''
    if request.method == 'POST':
        phddetails_form = phddetailsForm(request.POST)
        print(phddetails_form.errors)
        if phddetails_form.is_valid():
            if request.POST['edit_phddetails']:
                if Phds_Degree.objects.filter(
                        degreename=request.POST['degreename']).count() > 1:
                    message = 'Data Exists!!'
                    priority = 'error'
                    title = 'Data already exists'
                    phddetails_records = CommonUtils().fetch_phd(str(request.user))
                    return render(request, 'phd.html',
                                  {'phddetails_records': phddetails_records,
                                   'message': message, 'title': title,
                                   'priority': priority})
                personaldetails_content = {
                    'degreename': request.POST['degreename'],
                    'collegename': request.POST['collegename'],
                    'University': request.POST['University'],
                    'specification': request.POST['specification'],
                    'yearofpassing': request.POST['yearofpassing'],
                    'result': request.POST['result'],
                    'percentage': request.POST['percentage'],
                    'emailid': request.POST['emailid'],

                }
                Phds_Degree.objects.filter(
                    id=request.POST['edit_phddetails']).update(
                    **personaldetails_content)
                message = 'Data Updated !!'
                priority = 'success'
                title = 'Data updated'
            else:
                if Phds_Degree.objects.filter(
                        degreename=request.POST['degreename']).count() > 1:
                    message = 'Data Exists!!'
                    priority = 'error'
                    title = 'Data already exists'
                    phddetails_records = CommonUtils().fetch_phd(str(request.user))
                    return render(request, 'phd.html',
                                  {'phddetails_records': phddetails_records,
                                   'message': message, 'title': title,
                                   'priority': priority})
                post_personaldetails = phddetails_form.save(commit=False)
                post_personaldetails.user = request.user
                post_personaldetails.save()
                message = 'Data saved !!'
                priority = 'success'
                title = 'Data saved'
            phddetails_records = CommonUtils().fetch_phd(str(request.user))
            return render(request, 'phd.html',
                          {'phddetails_records': phddetails_records,
                           'message': message, 'title': title,
                           'priority': priority})
    if request.method == 'GET':
        phddetails_records = CommonUtils().fetch_phd(str(request.user))
        return render(request, 'phd.html',
                      {'phddetails_records': phddetails_records,
                       'message': message, 'title': title,
                       'priority': priority})


# view to inseert experience details of faculty in faculty dashboard
def add_experience(request):
    message = ''
    priority = ''
    title = ''
    if request.method == 'POST':
        experiencedetails_form = experiencedetailsForm(request.POST)
        print(experiencedetails_form.errors)
        if experiencedetails_form.is_valid():
            if request.POST['edit_experiencedetails']:
                if Experiences_Details.objects.filter(
                        institutename=request.POST['institutename']).count() > 1:
                    message = 'Data Exists!!'
                    priority = 'error'
                    title = 'Data already exists'
                    experiencedetails_records = CommonUtils().fetch_experience(str(request.user))
                    return render(request, 'teachingExp.html',
                                  {'experiencedetails_records': experiencedetails_records,
                                   'message': message, 'title': title,
                                   'priority': priority})
                personaldetails_content = {
                    'institutename': request.POST['institutename'],
                    'joiningdate': request.POST['joiningdate'],
                    'designation': request.POST['designation'],
                    'hikename': request.POST['hikename'],
                    'scale': request.POST['scale'],
                    'enddate': request.POST['enddate'],
                    'address': request.POST['address'],
                    'state': request.POST['state'],
                    'emailid': request.POST['emailid'],

                }
                Experiences_Details.objects.filter(
                    id=request.POST['edit_experiencedetails']).update(
                    **personaldetails_content)
                message = 'Data Updated !!'
                priority = 'success'
                title = 'Data updated'
            else:
                if Experiences_Details.objects.filter(
                        institutename=request.POST['institutename']).count() > 1:
                    message = 'Data Exists!!'
                    priority = 'error'
                    title = 'Data already exists'
                    experiencedetails_records = CommonUtils().fetch_experience(str(request.user))
                    return render(request, 'teachingExp.html',
                                  {'experiencedetails_records': experiencedetails_records,
                                   'message': message, 'title': title,
                                   'priority': priority})
                post_personaldetails = experiencedetails_form.save(commit=False)
                post_personaldetails.user = request.user
                post_personaldetails.save()
                message = 'Data saved !!'
                priority = 'success'
                title = 'Data saved'
            experiencedetails_records = CommonUtils().fetch_experience(str(request.user))
            return render(request, 'teachingExp.html',
                          {'experiencedetails_records': experiencedetails_records,
                           'message': message, 'title': title,
                           'priority': priority})
    if request.method == 'GET':
        experiencedetails_records = CommonUtils().fetch_experience(str(request.user))
        return render(request, 'teachingExp.html',
                      {'experiencedetails_records': experiencedetails_records,
                       'message': message, 'title': title,
                       'priority': priority})


# view to inseert publication details of faculty in faculty dashboard
def add_publication(request):
    message = ''
    priority = ''
    title = ''
    if request.method == 'POST':
        publicationdetails_form = publicationdetailsForm(request.POST)
        print(publicationdetails_form.errors)
        if publicationdetails_form.is_valid():
            if request.POST['edit_publicationdetails']:
                if Publications_Details.objects.filter(
                        titleofpublication=request.POST['titleofpublication']).count() > 1:
                    message = 'Data Exists!!'
                    priority = 'error'
                    title = 'Data already exists'
                    publicationdetails_records = CommonUtils().fetch_publication(str(request.user))
                    return render(request, 'publications.html',
                                  {'publicationdetails_records': publicationdetails_records,
                                   'message': message, 'title': title,
                                   'priority': priority})
                personaldetails_content = {
                    'titleofpublication': request.POST['titleofpublication'],
                    'authorname': request.POST['authorname'],
                    'year': request.POST['year'],
                    'titleofpaper': request.POST['titleofpaper'],
                    'volume': request.POST['volume'],
                    'pagenumbers': request.POST['pagenumbers'],
                    'impact': request.POST['impact'],
                    'reviewer': request.POST['reviewer'],
                    'journalname': request.POST['journalname'],
                    'emailid': request.POST['emailid'],

                }
                Publications_Details.objects.filter(
                    id=request.POST['edit_publicationdetails']).update(
                    **personaldetails_content)
                message = 'Data Updated !!'
                priority = 'success'
                title = 'Data updated'
            else:
                if Publications_Details.objects.filter(
                        titleofpublication=request.POST['titleofpublication']).count() > 1:
                    message = 'Data Exists!!'
                    priority = 'error'
                    title = 'Data already exists'
                    publicationdetails_records = CommonUtils().fetch_publication(str(request.user))
                    return render(request, 'publications.html',
                                  {'publicationdetails_records': publicationdetails_records,
                                   'message': message, 'title': title,
                                   'priority': priority})
                post_personaldetails = publicationdetails_form.save(commit=False)
                post_personaldetails.user = request.user
                post_personaldetails.save()
                message = 'Data saved !!'
                priority = 'success'
                title = 'Data saved'
            publicationdetails_records = CommonUtils().fetch_publication(str(request.user))
            return render(request, 'publications.html',
                          {'publicationdetails_records': publicationdetails_records,
                           'message': message, 'title': title,
                           'priority': priority})
    if request.method == 'GET':
        publicationdetails_records = CommonUtils().fetch_publication(str(request.user))
        return render(request, 'publications.html',
                      {'publicationdetails_records': publicationdetails_records,
                       'message': message, 'title': title,
                       'priority': priority})


# To view the facuulty dashboard
def add_home(request):
    if request.method == 'GET':
        return render(request, 'facultydashboard.html')


# view to inseert workshop details of faculty in faculty dashboard
def add_workshop(request):
    message = ''
    priority = ''
    title = ''
    if request.method == 'POST':
        workshopdetails_form = workshopdetailsForm(request.POST)
        print(workshopdetails_form.errors)
        if workshopdetails_form.is_valid():
            if request.POST['edit_workshopdetails']:
                if Workshops_Details.objects.filter(
                        presentationlevel=request.POST['presentationlevel']).count() > 1:
                    message = 'Data Exists!!'
                    priority = 'error'
                    title = 'Data already exists'
                    workshopdetails_records = CommonUtils().fetch_workshop(str(request.user))
                    return render(request, 'workshops.html',
                                  {'workshopdetails_records': workshopdetails_records,
                                   'message': message, 'title': title,
                                   'priority': priority})
                personaldetails_content = {
                    'presentationlevel': request.POST['presentationlevel'],
                    'type': request.POST['type'],
                    'sourceoffunding': request.POST['sourceoffunding'],
                    'paper': request.POST['paper'],
                    'name': request.POST['name'],
                    'description': request.POST['description'],
                    'country': request.POST['country'],
                    'state': request.POST['state'],
                    'startdate': request.POST['startdate'],
                    'date': request.POST['date'],
                    'hostorganization': request.POST['hostorganization'],
                    'eventname': request.POST['eventname'],
                    'area': request.POST['area'],
                    'resourceperson': request.POST['resourceperson'],
                    'place': request.POST['place'],
                    'numberofparticipants': request.POST['numberofparticipants'],
                    'briefdescription': request.POST['briefdescription'],
                    'amountfaculty': request.POST['amountfaculty'],
                    'modeofpayment': request.POST['modeofpayment'],
                    'amountuniversity': request.POST['amountuniversity'],
                    'emailid': request.POST['emailid'],




                }
                Workshops_Details.objects.filter(
                    id=request.POST['edit_workshopdetails']).update(
                    **personaldetails_content)
                message = 'Data Updated !!'
                priority = 'success'
                title = 'Data updated'
            else:
                if Workshops_Details.objects.filter(
                        presentationlevel=request.POST['presentationlevel']).count() > 1:
                    message = 'Data Exists!!'
                    priority = 'error'
                    title = 'Data already exists'
                    workshopdetails_records = CommonUtils().fetch_workshop(str(request.user))
                    return render(request, 'workshops.html',
                                  {'workshopdetails_records': workshopdetails_records,
                                   'message': message, 'title': title,
                                   'priority': priority})
                post_personaldetails = workshopdetails_form.save(commit=False)
                post_personaldetails.user = request.user
                post_personaldetails.save()
                message = 'Data saved !!'
                priority = 'success'
                title = 'Data saved'
            workshopdetails_records = CommonUtils().fetch_workshop(str(request.user))
            return render(request, 'workshops.html',
                          {'workshopdetails_records': workshopdetails_records,
                           'message': message, 'title': title,
                           'priority': priority})
    if request.method == 'GET':
        workshopdetails_records = CommonUtils().fetch_workshop(str(request.user))
        return render(request, 'workshops.html',
                      {'workshopdetails_records': workshopdetails_records,
                       'message': message, 'title': title,
                       'priority': priority})


# view to inseert patents details of faculty in faculty dashboard
def add_patents(request):
    message = ''
    priority = ''
    title = ''
    if request.method == 'POST':
        patentdetails_form = patentsdetailsForm(request.POST)
        print(patentdetails_form.errors)
        if patentdetails_form.is_valid():
            if request.POST['edit_patentdetails']:
                if Patentss_Details.objects.filter(
                        title=request.POST['title']).count() > 1:
                    message = 'Data Exists!!'
                    priority = 'error'
                    title = 'Data already exists'
                    patentdetails_records = CommonUtils().fetch_patent(str(request.user))
                    return render(request, 'patents.html',
                                  {'patentdetails_records': patentdetails_records,
                                   'message': message, 'title': title,
                                   'priority': priority})
                personaldetails_content = {
                    'title': request.POST['title'],
                    'name': request.POST['name'],
                    'holder': request.POST['holder'],
                    'datesubmitprovisional': request.POST['datesubmitprovisional'],
                    'datesubmitcomplete': request.POST['datesubmitcomplete'],
                    'datepublication': request.POST['datepublication'],
                    'remarks': request.POST['remarks'],
                    'emailid': request.POST['emailid'],

                }
                Patentss_Details.objects.filter(
                    id=request.POST['edit_patentdetails']).update(
                    **personaldetails_content)
                message = 'Data Updated !!'
                priority = 'success'
                title = 'Data updated'
            else:
                if Patentss_Details.objects.filter(
                        title=request.POST['title']).count() > 1:
                    message = 'Data Exists!!'
                    priority = 'error'
                    title = 'Data already exists'
                    patentdetails_records = CommonUtils().fetch_patent(str(request.user))
                    return render(request, 'patents.html',
                                  {'patentdetails_records': patentdetails_records,
                                   'message': message, 'title': title,
                                   'priority': priority})
                post_personaldetails = patentdetails_form.save(commit=False)
                post_personaldetails.user = request.user
                post_personaldetails.save()
                message = 'Data saved !!'
                priority = 'success'
                title = 'Data saved'
            patentdetails_records = CommonUtils().fetch_patent(str(request.user))
            return render(request, 'patents.html',
                          {'patentdetails_records': patentdetails_records,
                           'message': message, 'title': title,
                           'priority': priority})
    if request.method == 'GET':
        patentdetails_records = CommonUtils().fetch_patent(str(request.user))
        return render(request, 'patents.html',
                      {'patentdetails_records': patentdetails_records,
                       'message': message, 'title': title,
                       'priority': priority})


# view to inseert grantsfetched details of faculty in faculty dashboard
def add_grantsfetched(request):
    message = ''
    priority = ''
    title = ''
    if request.method == 'POST':
        grantsfetcheddetails_form = grantsfetchedForm(request.POST)
        print(grantsfetcheddetails_form.errors)
        if grantsfetcheddetails_form.is_valid():
            if request.POST['edit_grantsfetcheddetails']:
                if Grantss_Fetched.objects.filter(
                        projectname=request.POST['projectname']).count() > 1:
                    message = 'Data Exists!!'
                    priority = 'error'
                    title = 'Data already exists'
                    grantsfetcheddetails_records = CommonUtils().fetch_grantsfetched(str(request.user))
                    return render(request, 'grantsfetched.html',
                                  {'grantsfetcheddetails_records': grantsfetcheddetails_records,
                                   'message': message, 'title': title,
                                   'priority': priority})
                personaldetails_content = {
                    'projectname': request.POST['projectname'],
                    'grantissuedby': request.POST['grantissuedby'],
                    'grantedamount': request.POST['grantedamount'],
                    'grantdate': request.POST['grantdate'],
                    'coauthors': request.POST['coauthors'],
                    'address': request.POST['address'],
                    'description': request.POST['description'],
                    'emailid': request.POST['emailid'],

                }
                Grantss_Fetched.objects.filter(
                    id=request.POST['edit_grantsfetcheddetails']).update(
                    **personaldetails_content)
                message = 'Data Updated !!'
                priority = 'success'
                title = 'Data updated'
            else:
                if Grantss_Fetched.objects.filter(
                        projectname=request.POST['projectname']).count() > 1:
                    message = 'Data Exists!!'
                    priority = 'error'
                    title = 'Data already exists'
                    grantsfetcheddetails_records = CommonUtils().fetch_grantsfetched(str(request.user))
                    return render(request, 'grantsfetched.html',
                                  {'grantsfetcheddetails_records': grantsfetcheddetails_records,
                                   'message': message, 'title': title,
                                   'priority': priority})
                post_personaldetails = grantsfetcheddetails_form.save(commit=False)
                post_personaldetails.user = request.user
                post_personaldetails.save()
                message = 'Data saved !!'
                priority = 'success'
                title = 'Data saved'
            grantsfetcheddetails_records = CommonUtils().fetch_grantsfetched(str(request.user))
            return render(request, 'grantsfetched.html',
                          {'grantsfetcheddetails_records': grantsfetcheddetails_records,
                           'message': message, 'title': title,
                           'priority': priority})
    if request.method == 'GET':
        grantsfetcheddetails_records = CommonUtils().fetch_grantsfetched(str(request.user))
        return render(request, 'grantsfetched.html',
                      {'grantsfetcheddetails_records': grantsfetcheddetails_records,
                       'message': message, 'title': title,
                       'priority': priority})


# view to inseert grants Applied details of faculty in faculty dashboard
def add_grantsapplied(request):
    message = ''
    priority = ''
    title = ''
    if request.method == 'POST':
        grantsapplieddetails_form = grantsappliedForm(request.POST)
        print(grantsapplieddetails_form.errors)
        if grantsapplieddetails_form.is_valid():
            if request.POST['edit_grantsapplieddetails']:
                if Grantss_Applied.objects.filter(
                        projectname=request.POST['projectname']).count() > 1:
                    message = 'Data Exists!!'
                    priority = 'error'
                    title = 'Data already exists'
                    grantsapplieddetails_records = CommonUtils().fetch_grantssapplied(str(request.user))
                    return render(request, 'grantsapplied.html',
                                  {'grantsapplieddetails_records': grantsapplieddetails_records,
                                   'message': message, 'title': title,
                                   'priority': priority})
                personaldetails_content = {
                    'date': request.POST['date'],
                    'projectname': request.POST['projectname'],
                    'agency': request.POST['agency'],
                    'grantamount': request.POST['grantamount'],
                    'address': request.POST['address'],
                    'description': request.POST['description'],
                    'emailid': request.POST['emailid'],

                }
                Grantss_Applied.objects.filter(
                    id=request.POST['edit_grantsapplieddetails']).update(
                    **personaldetails_content)
                message = 'Data Updated !!'
                priority = 'success'
                title = 'Data updated'
            else:
                if Grantss_Applied.objects.filter(
                        projectname=request.POST['projectname']).count() > 1:
                    message = 'Data Exists!!'
                    priority = 'error'
                    title = 'Data already exists'
                    grantsapplieddetails_records = CommonUtils().fetch_grantssapplied(str(request.user))
                    return render(request, 'grantsapplied.html',
                                  {'grantsapplieddetails_records': grantsapplieddetails_records,
                                   'message': message, 'title': title,
                                   'priority': priority})
                post_personaldetails = grantsapplieddetails_form.save(commit=False)
                post_personaldetails.user = request.user
                post_personaldetails.save()
                message = 'Data saved !!'
                priority = 'success'
                title = 'Data saved'
            grantsapplieddetails_records = CommonUtils().fetch_grantssapplied(str(request.user))
            return render(request, 'grantsapplied.html',
                          {'grantsapplieddetails_records': grantsapplieddetails_records,
                           'message': message, 'title': title,
                           'priority': priority})
    if request.method == 'GET':
        grantsapplieddetails_records = CommonUtils().fetch_grantssapplied(str(request.user))
        return render(request, 'grantsapplied.html',
                      {'grantsapplieddetails_records': grantsapplieddetails_records,
                       'message': message, 'title': title,
                       'priority': priority})


# view to inseert Awards details of faculty in faculty dashboard
def add_awards(request):
    message = ''
    priority = ''
    title = ''
    if request.method == 'POST':
        awardsdetails_form = awardsdetailsForm(request.POST)
        print(awardsdetails_form.errors)
        if awardsdetails_form.is_valid():
            if request.POST['edit_awardsdetails']:
                if Awardss_Details.objects.filter(
                        awardname=request.POST['awardname']).count() > 1:
                    message = 'Data Exists!!'
                    priority = 'error'
                    title = 'Data already exists'
                    awardsdetails_records = CommonUtils().fetch_awards(str(request.user))
                    return render(request, 'awards.html',
                                  {'awardsdetails_records': awardsdetails_records,
                                   'message': message, 'title': title,
                                   'priority': priority})
                personaldetails_content = {
                    'awardname': request.POST['awardname'],
                    'awardinstitution': request.POST['awardinstitution'],
                    'date': request.POST['date'],
                    'description': request.POST['description'],
                    'emailid': request.POST['emailid'],

                }
                Awardss_Details.objects.filter(
                    id=request.POST['edit_awardsdetails']).update(
                    **personaldetails_content)
                message = 'Data Updated !!'
                priority = 'success'
                title = 'Data updated'
            else:
                if Awardss_Details.objects.filter(
                        awardname=request.POST['awardname']).count() > 1:
                    message = 'Data Exists!!'
                    priority = 'error'
                    title = 'Data already exists'
                    awardsdetails_records = CommonUtils().fetch_awards(str(request.user))
                    return render(request, 'awards.html',
                                  {'awardsdetails_records': awardsdetails_records,
                                   'message': message, 'title': title,
                                   'priority': priority})
                post_personaldetails = awardsdetails_form.save(commit=False)
                post_personaldetails.user = request.user
                post_personaldetails.save()
                message = 'Data saved !!'
                priority = 'success'
                title = 'Data saved'
            awardsdetails_records = CommonUtils().fetch_awards(str(request.user))
            return render(request, 'awards.html',
                          {'awardsdetails_records': awardsdetails_records,
                           'message': message, 'title': title,
                           'priority': priority})
    if request.method == 'GET':
        awardsdetails_records = CommonUtils().fetch_awards(str(request.user))
        return render(request, 'awards.html',
                      {'awardsdetails_records': awardsdetails_records,
                       'message': message, 'title': title,
                       'priority': priority})


# view to inseert Bank details of faculty in faculty dashboard
def add_bank(request):
    message = ''
    priority = ''
    title = ''
    if request.method == 'POST':
        bankdetails_form = bankdetailsForm(request.POST)
        print(bankdetails_form.errors)
        if bankdetails_form.is_valid():
            if request.POST['edit_bankdetails']:
                if Banks_Details.objects.filter(
                        accountnumber=request.POST['accountnumber']).count() > 1:
                    message = 'Data Exists!!'
                    priority = 'error'
                    title = 'Data already exists'
                    bankdetails_records = CommonUtils().fetch_bank(str(request.user))
                    return render(request, 'addbank.html',
                                  {'bankdetails_records': bankdetails_records,
                                   'message': message, 'title': title,
                                   'priority': priority})
                personaldetails_content = {
                    'bankname': request.POST['bankname'],
                    'accountnumber': request.POST['accountnumber'],
                    'branchname': request.POST['branchname'],
                    'ifsccode': request.POST['ifsccode'],
                    'city': request.POST['city'],
                    'state': request.POST['state'],
                    'emailid': request.POST['emailid'],

                }
                Banks_Details.objects.filter(
                    id=request.POST['edit_bankdetails']).update(
                    **personaldetails_content)
                message = 'Data Updated !!'
                priority = 'success'
                title = 'Data updated'
            else:
                if Banks_Details.objects.filter(
                        accountnumber=request.POST['accountnumber']).count() > 1:
                    message = 'Data Exists!!'
                    priority = 'error'
                    title = 'Data already exists'
                    bankdetails_records = CommonUtils().fetch_bank(str(request.user))
                    return render(request, 'addbank.html',
                                  {'bankdetails_records': bankdetails_records,
                                   'message': message, 'title': title,
                                   'priority': priority})
                post_personaldetails = bankdetails_form.save(commit=False)
                post_personaldetails.user = request.user
                post_personaldetails.save()
                message = 'Data saved !!'
                priority = 'success'
                title = 'Data saved'
            bankdetails_records = CommonUtils().fetch_bank(str(request.user))
            return render(request, 'addbank.html',
                          {'bankdetails_records': bankdetails_records,
                           'message': message, 'title': title,
                           'priority': priority})
    if request.method == 'GET':
        bankdetails_records = CommonUtils().fetch_bank(str(request.user))
        return render(request, 'addbank.html',
                      {'bankdetails_records': bankdetails_records,
                       'message': message, 'title': title,
                       'priority': priority})


# view to inseert course details  in HOD dashboard
def add_Course(request):
    if request.method == 'POST':
        department_form = coursedetailsForm(request.POST)
        if department_form.is_valid():
            post_department = department_form.save(commit=False)
            post_department.save()
            messages.success(request, 'Course Added SUCCESSFULLY!!')
            return render(request, 'addCourse.html')
    if request.method == 'GET':
        return render(request, 'addCourse.html')


# view to add the faculties  in HOD dashboard
def add_Faculty(request):
    if request.method == 'GET':
        department = list(Department.objects.all())
        return render(request, 'addFaculty.html',
                      {'departments': department})

    if request.method == 'POST':
        student_form = facultydetailsForm(request.POST)
        if student_form.is_valid():
            new_user = User.objects.create_user(
                username=request.POST['email'],
                password=request.POST['password'])

            post_department = student_form.save(commit=False)
            post_department.user = new_user

            post_department.save()
            messages.success(request, 'Faculty Added SUCCESSFULLY!!')
            return HttpResponseRedirect('/staff/addFaculty')




































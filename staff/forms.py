from django import forms
from staff.models import  Personal_Details, Bachelorss_Degree, Masterss_degree, Phds_Degree, Experiences_Details, \
    Publications_Details, Workshops_Details, Patentss_Details, Grantss_Fetched, Grantss_Applied, Awardss_Details, Banks_Details, \
    Courses_Details, facultydetails, hodregister

from staff.models import Department

class DepartmentForm(forms.ModelForm):

    class Meta:
        model = Department
        fields = ('name', 'acronym','code','estd','location')


class registerForm44(forms.ModelForm):

    class Meta:
        model = hodregister
        fields = ('name','email','department','mobile','designation')







class personaldetailsForm(forms.ModelForm):
    class Meta:
        model = Personal_Details
        fields = ('firstname','middlename','lastname','dateofbirth','emailid','mobile','alternatemobile','aadharnumber','pancardnumber','bloodgroup','street','pincode','city','district','state','dateofjoining','departmentname','designation')

class bachelordetailsForm(forms.ModelForm):
    class Meta:
        model =  Bachelorss_Degree
        fields = ('degreename','collegename','University','yearofpassing','result','percentage','emailid')

class masterdetailsForm(forms.ModelForm):
    class Meta:
        model =  Masterss_degree
        fields = ('degreename','collegename','University','yearofpassing','result','percentage','emailid')

class phddetailsForm(forms.ModelForm):
    class Meta:
        model = Phds_Degree
        fields = ('degreename','collegename','specification','University','yearofpassing','result','percentage','emailid')


class experiencedetailsForm(forms.ModelForm):
    class Meta:
        model = Experiences_Details
        fields = ('institutename','joiningdate','designation','hikename','scale','enddate','address','state','emailid')

class publicationdetailsForm(forms.ModelForm):
    class Meta:
        model = Publications_Details
        fields = ('titleofpublication','authorname','year','titleofpaper','volume','pagenumbers','impact','reviewer','journalname','emailid')


class workshopdetailsForm(forms.ModelForm):
    class Meta:
        model = Workshops_Details
        fields = ('presentationlevel','type','sourceoffunding','paper','name','description','country','state','startdate','date','hostorganization','eventname','area','resourceperson','place','numberofparticipants','briefdescription','amountfaculty','modeofpayment','amountuniversity','emailid')


class patentsdetailsForm(forms.ModelForm):
    class Meta:
        model = Patentss_Details
        fields = ('title','name','holder','datesubmitprovisional','datesubmitcomplete','datepublication','remarks','emailid')


class grantsfetchedForm(forms.ModelForm):
    class Meta:
        model = Grantss_Fetched
        fields = ('projectname','grantissuedby','grantedamount','grantdate','coauthors','address','description','emailid')


class grantsappliedForm(forms.ModelForm):
    class Meta:
        model = Grantss_Applied
        fields = ('date', 'projectname', 'agency', 'grantamount', 'address', 'description','emailid')


class awardsdetailsForm(forms.ModelForm):
    class Meta:
        model = Awardss_Details
        fields = ('awardname','awardinstitution','date','description','emailid')

class bankdetailsForm(forms.ModelForm):
    class Meta:
        model = Banks_Details
        fields = ('bankname','accountnumber','branchname','ifsccode','city','state','emailid')


class coursedetailsForm(forms.ModelForm):
    class Meta:
        model = Courses_Details
        fields = ('name','code','credit','created','department','semester','coursedescription')


class facultydetailsForm(forms.ModelForm):
    class Meta:
        model = facultydetails
        fields =('name','email','department','mobile','joining','facultycourse','designation')
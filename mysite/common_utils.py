from staff.models import Personal_Details, Bachelorss_Degree, Experiences_Details, Publications_Details, \
    Masterss_degree, \
    Phds_Degree, Patentss_Details, Grantss_Fetched, Grantss_Applied, Awardss_Details, Workshops_Details, Banks_Details, \
    Courses_Details, facultydetails, Department, hodregister, Courses_Details


class CommonUtils:

    def fetch_department(self, pd='all'):
        if pd.lower() == 'all':
            department_records = Personal_Details.objects.all()
        else:
            department_records = Personal_Details.objects.filter(emailid=pd)
        department_list = []
        for elements, item in enumerate(department_records):
            department_dict = {}
            department_dict["id"] = item.id
            department_dict["firstname"] = item.firstname
            department_dict["middlename"] = item.middlename
            department_dict["lastname"] = item.lastname
            department_dict["dateofbirth"] = str(item.dateofbirth)
            department_dict["emailid"] = item.emailid
            department_dict["mobile"] = item.mobile
            department_dict["alternatemobile"] = item.alternatemobile
            department_dict["aadharnumber"] = item.aadharnumber
            department_dict["pancardnumber"] = item.pancardnumber
            department_dict["bloodgroup"] = item.bloodgroup
            department_dict["street"] = item.street
            department_dict["pincode"] = item.pincode
            department_dict["city"] = item.city
            department_dict["district"] = item.district
            department_dict["state"] = item.state
            department_dict["dateofjoining"] = str(item.dateofjoining)
            department_dict["departmentname"] = item.departmentname
            department_dict["designation"] = item.designation

            department_list.append(department_dict)
        return department_list



    def fetch_bachelor(self, pd='all'):
        if pd.lower() == 'all':
            bachelor_records = Bachelorss_Degree.objects.all()
        else:
            bachelor_records = Bachelorss_Degree.objects.filter(emailid=pd)
        bachelor_list = []
        for elements, item in enumerate(bachelor_records):
            bacelor_dict = {}
            bacelor_dict["id"] = item.id
            bacelor_dict["degreename"] = item.degreename
            bacelor_dict["collegename"] = item.collegename
            bacelor_dict["University"] = item.University
            bacelor_dict["yearofpassing"] = str(item.yearofpassing)
            bacelor_dict["result"] = item.result
            bacelor_dict["percentage"] = item.percentage
            bacelor_dict["emailid"] = item.emailid


            bachelor_list.append(bacelor_dict)
        return bachelor_list




    def fetch_master(self, pd='all'):
        if pd.lower() == 'all':
            department_records = Masterss_degree.objects.all()
        else:
            department_records = Masterss_degree.objects.filter(emailid=pd)
        department_list = []
        for elements, item in enumerate(department_records):
            department_dict = {}
            department_dict["id"] = item.id
            department_dict["degreename"] = item.degreename
            department_dict["collegename"] = item.collegename
            department_dict["University"] = item.University
            department_dict["yearofpassing"] = str(item.yearofpassing)
            department_dict["result"] = item.result
            department_dict["percentage"] = item.percentage
            department_dict["emailid"] = item.emailid


            department_list.append(department_dict)
        return department_list


    def fetch_phd(self, pd='all'):
        if pd.lower() == 'all':
            department_records = Phds_Degree.objects.all()
        else:
            department_records = Phds_Degree.objects.filter(emailid=pd)
        department_list = []
        for elements, item in enumerate(department_records):
            department_dict = {}
            department_dict["id"] = item.id
            department_dict["degreename"] = item.degreename
            department_dict["collegename"] = item.collegename
            department_dict["University"] = item.University
            department_dict["specification"] = item.specification
            department_dict["yearofpassing"] = str(item.yearofpassing)
            department_dict["result"] = item.result
            department_dict["percentage"] = item.percentage
            department_dict["emailid"] = item.emailid

            department_list.append(department_dict)
        return department_list










    def fetch_experience(self, pd='all'):
        if pd.lower() == 'all':
            department_records = Experiences_Details.objects.all()
        else:
            department_records = Experiences_Details.objects.filter(emailid=pd)
        department_list = []
        for elements, item in enumerate(department_records):
            department_dict = {}
            department_dict["id"] = item.id
            department_dict["institutename"] = item.institutename
            department_dict["joiningdate"] = str(item.joiningdate)
            department_dict["designation"] = item.designation
            department_dict["hikename"] = item.hikename
            department_dict["scale"] = item.scale
            department_dict["enddate"] = str(item.enddate)
            department_dict["address"] = item.address
            department_dict["state"] = item.state
            department_dict["emailid"] = item.emailid


            department_list.append(department_dict)
        return department_list





    def fetch_publication(self, pd='all'):
        if pd.lower() == 'all':
            department_records = Publications_Details.objects.all()
        else:
            department_records = Publications_Details.objects.filter(emailid=pd)
        department_list = []
        for elements, item in enumerate(department_records):
            department_dict = {}
            department_dict["id"] = item.id
            department_dict["titleofpublication"] = item.titleofpublication
            department_dict["authorname"] = item.authorname
            department_dict["year"] = str(item.year)
            department_dict["titleofpaper"] = item.titleofpaper
            department_dict["volume"] = item.volume
            department_dict["pagenumbers"] = item.pagenumbers
            department_dict["impact"] = item.impact
            department_dict["reviewer"] = item.reviewer
            department_dict["journalname"] = item.journalname
            department_dict["emailid"] = item.emailid


            department_list.append(department_dict)
        return department_list





    def fetch_patent(self, pd='all'):
        if pd.lower() == 'all':
            department_records = Patentss_Details.objects.all()
        else:
            department_records = Patentss_Details.objects.filter(emailid=pd)
        department_list = []
        for elements, item in enumerate(department_records):
            department_dict = {}
            department_dict["id"] = item.id
            department_dict["title"] = item.title
            department_dict["name"] = item.name
            department_dict["holder"] = item.holder
            department_dict["datesubmitprovisional"] = str(item.datesubmitprovisional)
            department_dict["datesubmitcomplete"] = str(item.datesubmitcomplete)
            department_dict["datepublication"] = str(item.datepublication)
            department_dict["remarks"] = item.remarks
            department_dict["emailid"] = item.emailid

            department_list.append(department_dict)
        return department_list





    def fetch_grantsfetched(self, pd='all'):
        if pd.lower() == 'all':
            department_records = Grantss_Fetched.objects.all()
        else:
            department_records = Grantss_Fetched.objects.filter(emailid=pd)
        department_list = []
        for elements, item in enumerate(department_records):
            department_dict = {}
            department_dict["id"] = item.id
            department_dict["projectname"] = item.projectname
            department_dict["grantissuedby"] = item.grantissuedby
            department_dict["grantedamount"] = item.grantedamount
            department_dict["grantdate"] = str(item.grantdate)
            department_dict["coauthors"] =  item.coauthors
            department_dict["address"] =  item.address
            department_dict["description"] = item.description
            department_dict["emailid"] = item.emailid
            department_list.append(department_dict)
        return department_list




    def fetch_grantssapplied(self, pd='all'):
        if pd.lower() == 'all':
            department_records = Grantss_Applied.objects.all()
        else:
            department_records = Grantss_Applied.objects.filter(emailid=pd)
        department_list = []
        for elements, item in enumerate(department_records):
            department_dict = {}
            department_dict["id"] = item.id
            department_dict["date"] = str(item.date)
            department_dict["projectname"] = item.projectname
            department_dict["agency"] = item.agency
            department_dict["grantamount"] = item.grantamount
            department_dict["address"] = item.address
            department_dict["description"] =  item.description
            department_dict["emailid"] = item.emailid

            department_list.append(department_dict)
        return department_list






    def fetch_awards(self, pd='all'):
        if pd.lower() == 'all':
            department_records = Awardss_Details.objects.all()
        else:
            department_records = Awardss_Details.objects.filter(emailid=pd)
        department_list = []
        for elements, item in enumerate(department_records):
            department_dict = {}
            department_dict["id"] = item.id
            department_dict["awardname"] = item.awardname
            department_dict["awardinstitution"] = item.awardinstitution
            department_dict["date"] = str(item.date)
            department_dict["description"] = item.description
            department_dict["emailid"] = item.emailid

            department_list.append(department_dict)
        return department_list







    def fetch_workshop(self, pd='all'):
        if pd.lower() == 'all':
            department_records = Workshops_Details.objects.all()
        else:
            department_records = Workshops_Details.objects.filter(emailid=pd)
        department_list = []
        for elements, item in enumerate(department_records):
            department_dict = {}
            department_dict["id"] = item.id
            department_dict["presentationlevel"] = item.presentationlevel
            department_dict["sourceoffunding"] = item.sourceoffunding
            department_dict["type"] = item.type
            department_dict["paper"] = item.paper
            department_dict["name"] = item.name
            department_dict["description"] = item.description
            department_dict["country"] = item.country
            department_dict["state"] = item.state
            department_dict["startdate"] = str(item.startdate)
            department_dict["date"] = str(item.date)
            department_dict["hostorganization"] = item.hostorganization
            department_dict["eventname"] = item.eventname
            department_dict["area"] = item.area
            department_dict["resourceperson"] = item.resourceperson
            department_dict["place"] = item.place
            department_dict["numberofparticipants"] = item.numberofparticipants
            department_dict["briefdescription"] = item.briefdescription
            department_dict["amountfaculty"] = item.amountfaculty
            department_dict["modeofpayment"] = item.modeofpayment
            department_dict["amountuniversity"] = item.amountuniversity
            department_dict["emailid"] = item.emailid

            department_list.append(department_dict)
        return department_list
















    def fetch_bank(self, pd='all'):
        if pd.lower() == 'all':
            department_records = Banks_Details.objects.all()
        else:
            department_records = Banks_Details.objects.filter(emailid=pd)
        department_list = []
        for elements, item in enumerate(department_records):
            department_dict = {}
            department_dict["id"] = item.id
            department_dict["bankname"] = item.bankname
            department_dict["accountnumber"] = item.accountnumber
            department_dict["branchname"] = item.branchname
            department_dict["ifsccode"] = item.ifsccode
            department_dict["city"] = item.city
            department_dict["state"] =  item.state
            department_dict["emailid"] = item.emailid

            department_list.append(department_dict)
        return department_list







    def fetch_course(self, pd='all'):
        if pd.lower() == 'all':
            department_records = Courses_Details.objects.all()
        else:
            department_records = Courses_Details.objects.filter(emailid=pd)
        department_list = []
        for elements, item in enumerate(department_records):
            department_dict = {}
            department_dict["id"] = item.id
            department_dict["name"] = item.name
            department_dict["code"] = item.code
            department_dict["credit"] = item.credit
            department_dict["estd"] = str(item.estd)
            department_dict["department"] = item.department
            department_dict["semester"] =  item.semester
            department_dict["coursedescription"] = item.coursedescription
            department_dict["emailid"] = item.emailid

            department_list.append(department_dict)
        return department_list









    def fetch_faculty(self, pd='all'):
        if pd.lower() == 'all':
            department_records = facultydetails.objects.all()
        else:
            department_records = facultydetails.objects.filter(email=pd)
        department_list = []
        for elements, item in enumerate(department_records):
            department_dict = {}
            department_dict["id"] = item.id
            department_dict["name"] = item.name
            department_dict["email"] = item.email
            department_dict["department"] = item.department
            department_dict["mobile"] =  item.mobile
            department_dict["joining"] = str(item.department)
            department_dict["facultycourse"] =  item.facultycourse
            department_dict["designation"] = item.designation

            department_list.append(department_dict)
        return department_list








    def fetch_dept(self, pd='all'):
        if pd.lower() == 'all':
            department_records = Department.objects.all()
        else:
            department_records = Department.objects.filter(name=pd)
        department_list = []
        for elements, item in enumerate(department_records):
            department_dict = {}
            department_dict["id"] = item.id
            department_dict["name"] = item.name
            department_dict["acronym"] = item.acronym
            department_dict["code"] = item.code
            department_dict["estd"] = str(item.estd)
            department_dict["location"] = item.location
            department_list.append(department_dict)
        return department_list









    def fetch_hod(self, pd='all'):
        if pd.lower() == 'all':
            department_records = hodregister.objects.all()
        else:
            department_records = hodregister.objects.filter(email=pd)
        department_list = []
        for elements, item in enumerate(department_records):
            department_dict = {}
            department_dict["id"] = item.id
            department_dict["name"] = item.name
            department_dict["email"] = item.email
            department_dict["department"] = item.department
            department_dict["mobile"] =  item.mobile
            department_dict["designation"] = item.designation
            department_list.append(department_dict)
        return department_list







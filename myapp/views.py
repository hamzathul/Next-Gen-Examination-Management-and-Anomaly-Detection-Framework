from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from myapp.models import Login, Authority, Staff, Student, Exam, Schedule, Staffallocation, Studentallocation, Hall, Hallallocation


def login(request):
    return render(request, 'Admin/Login.html')
def login_post(request):
    username = request.POST['textfield']
    password = request.POST['textfield2']
    res = Login.objects.filter(username=username, password=password)
    if res.exists():
        ress = Login.objects.get(username = username, password=password)
        if ress.type == 'Admin':
            return redirect('/myapp/adminhome/')
        else:
            return HttpResponse('''<script>alert('User not found');window.location='/myapp/login/'</script>''')
    else:
        return HttpResponse('''<script>alert('User not found');window.location='/myapp/login/'</script>''')



def adminhome(request):
    return render(request,'Admin/Admin Home.html')

def admin_addauthority(request):
    return render(request, 'Admin/Add Authority.html')

def admin_addauthority_post(request):
    name=request.POST['textfield']
    place=request.POST['textfield2']
    email=request.POST['textfield3']
    phone=request.POST['textfield4']
    post=request.POST['textfield5']
    district=request.POST['textfield6']
    pincode=request.POST['textfield7']

    l=Login()
    l.username=email
    import random
    ps=random.randint(0000,9999)
    l.password = str(ps)
    l.type = 'Authority'
    l.save()

    a=Authority()
    a.LOGIN=l
    a.name = name
    a.place = place
    a.email = email
    a.phone = phone
    a.post = post
    a.district = district
    a.pincode = pincode
    a.save()

    return HttpResponse('''<script>alert('Added Successfully');window.location='/myapp/admin_addauthority/'</script>''')


def admin_viewauthority(request):
    res = Authority.objects.all()
    return render(request, 'Admin/View Authority.html',{'data':res})

def admin_viewauthority_post(request):
    search=request.POST['textfield']
    ab = Authority.objects.filter(name__icontains=search)
    return render(request, 'Admin/View Authority.html', {'data':ab})


def admin_deleteauthority(request,id):
    res = Authority.objects.filter(id = id).delete()
    return HttpResponse('''<script>alert('Deleted Successfully');window.location='/myapp/admin_viewauthority/'</script>''')

def admin_editauthority(request,id):
    res = Authority.objects.get(id = id)
    return render(request, 'Admin/Edit Authority.html', {"data":res})

def admin_editauthority_post(request):
    name = request.POST['textfield']
    place = request.POST['textfield2']
    Email = request.POST['textfield3']
    phone = request.POST['textfield4']
    post = request.POST['textfield5']
    district = request.POST['textfield6']
    pincode = request.POST['textfield7']
    id = request.POST['id']

    a = Authority.objects.get(id = id)
    a.name = name
    a.place = place
    a.email = Email
    a.phone = phone
    a.post = post
    a.district = district
    a.pincode = pincode
    a.save()
    return HttpResponse('''<script>alert('Edited Successfully');window.location='/myapp/admin_viewauthority/'</script>''')


def admin_addstaff(request):
    return render(request, 'Admin/Add Staff.html')

def admin_addstaff_post(request):
    name = request.POST['textfield']
    department = request.POST['textfield8']
    photo = request.FILES['textfield9']
    gender = request.POST['textfield10']
    place = request.POST['textfield2']
    email = request.POST['textfield3']
    phone = request.POST['textfield4']
    post = request.POST['textfield5']
    district = request.POST['textfield6']
    pincode = request.POST['textfield7']
    from datetime import datetime
    date = datetime.now().strftime('%Y%m%d_%H%M%S')+".jpg"
    fs = FileSystemStorage()
    fs.save(date,photo)
    path = fs.url(date)


    l = Login()
    l.username = email
    import random
    ps = random.randint(0000, 9999)
    l.password = str(ps)
    l.type = 'Staff'
    l.save()

    s = Staff()
    s.LOGIN = l
    s.name = name
    s.department = department
    s.photo = path
    s.gender = gender
    s.place = place
    s.email = email
    s.phone = phone
    s.post = post
    s.district = district
    s.pincode = pincode
    s.save()

    return HttpResponse('''<script>alert('Added Successfully');window.location='/myapp/admin_addstaff/'</script>''')




def admin_viewstaff(request):
    res=Staff.objects.all()
    return render(request, 'Admin/View Staff.html',{'data':res})

def admin_viewstaff_post(request):
    search = request.POST['textfield']
    ab = Staff.objects.filter(name__icontains=search)
    return render(request, 'Admin/View Staff.html', {'data':ab})

def admin_deletestaff(request,id):
    res = Staff.objects.filter(id = id).delete()
    return HttpResponse('''<script>alert('Deleted Successfully');window.location='/myapp/admin_viewstaff/'</script>''')

def admin_editstaff(request, id):
    res = Staff.objects.get(id=id)
    return render(request, 'Admin/Edit Staff.html', {"data":res})

def admin_editstaff_post(request):
    name = request.POST['textfield']
    department = request.POST['textfield8']
    gender = request.POST['textfield10']
    place = request.POST['textfield2']
    Email = request.POST['textfield11']
    phone = request.POST['textfield3']
    post = request.POST['textfield5']
    district = request.POST['textfield6']
    pincode = request.POST['textfield7']
    id = request.POST['id']
    s = Staff.objects.get(id = id)

    if 'textfield9' in request.FILES:
        photo = request.FILES['textfield9']

        from datetime import datetime
        date = datetime.now().strftime('%Y%m%d_%H%M%S') + ".jpg"
        fs = FileSystemStorage()
        fs.save(date, photo)
        path = fs.url(date)
        s.photo = path
        s.save()

    s.name = name
    s.department = department
    s.gender = gender
    s.place = place
    s.email = Email
    s.phone = phone
    s.post = post
    s.district = district
    s.pincode = pincode
    s.save()
    return HttpResponse('''<script>alert('Edited Successfully');window.location='/myapp/admin_viewstaff/'</script>''')

def admin_addstudent(request):
    return render(request, 'Admin/Add Student.html')

def admin_addstudent_post(request):
    name = request.POST['textfield']
    admissionno = request.POST['textfield2']
    dob = request.POST['textfield3']
    department = request.POST['textfield4']
    course = request.POST['textfield5']
    email = request.POST['textfield6']
    gender = request.POST['textfield7']
    place = request.POST['textfield8']
    photo = request.FILES['fileField']
    from datetime import datetime
    date = datetime.now().strftime('%Y%m%d_%H%M%S') + ".jpg"
    fs = FileSystemStorage()
    fs.save(date, photo)
    path = fs.url(date)

    s = Student()
    s.name = name
    s.admissionno = admissionno
    s.dob = dob
    s.department = department
    s.course = course
    s.photo = path
    s.gender = gender
    s.place = place
    s.email = email
    s.save()

    return HttpResponse('''<script>alert('Added Successfully');window.location='/myapp/admin_addstudent/'</script>''')


def admin_viewstudent(request):
    ab = Student.objects.all()
    return render(request, 'Admin/View Student.html', {'data':ab})

def admin_viewstudent_post(request):
    search = request.POST['textfield']
    ab = Student.objects.filter(name__icontains=search)

    return render(request, 'Admin/View Student.html',{'data':ab})   ############//


def admin_editstudent(request, id):
    res = Student.objects.get(id = id)
    return render(request, 'Admin/Edit Student.html', {"data":res})

def admin_editstudent_post(request):
    name = request.POST['textfield']
    admissionno = request.POST['textfield2']
    dob = request.POST['textfield3']
    department = request.POST['textfield4']
    course = request.POST['textfield5']
    email = request.POST['textfield6']
    gender = request.POST['textfield7']
    place = request.POST['textfield8']
    photo = request.FILES['fileField']#####################
    id = request.POST['id']
    s = Student.objects.get(id=id)

    if 'fileField' in request.FILES:
        photo = request.FILES['fileField']

        from datetime import datetime
        date = datetime.now().strftime('%Y%m%d_%H%M%S') + ".jpg"
        fs = FileSystemStorage()
        fs.save(date, photo)
        path = fs.url(date)
        s.photo = path
        s.save()
    s.name = name
    s.admissionno = admissionno
    s.dob = dob
    s.department = department
    s.course = course
    s.gender = gender
    s.place = place
    s.email = email
    s.save()
    return HttpResponse('''<script>alert('Edited Successfully');window.location='/myapp/admin_viewstudent/'</script>''')

def admin_deletestudent(request,id):
    res = Student.objects.filter(id = id).delete()
    return HttpResponse('''<script>alert('Deleted Successfully');window.location='/myapp/admin_viewstudent/'</script>''')

def admin_addexam(request):
    return render(request, 'Admin/Add Exam.html')

def admin_addexam_post(request):
    examname = request.POST['textfield']
    examcode = request.POST['textfield2']
    date = request.POST['textfield3']
    type = request.POST['select']

    e = Exam()
    e.examname = examname
    e.examcode = examcode
    e.date = date
    e.type = type
    e.save()
    # Submit button available in html page   #############################
    return HttpResponse('''<script>alert('Added Successfully');window.location='/myapp/admin_addexam/'</script>''')


def admin_viewexam(request):
    res=Exam.objects.all()
    return render(request, 'Admin/View Exam.html',{'data':res})

def admin_viewexam_post(request):
    fromdate = request.POST['textfield']
    todate = request.POST['textfield2']
    # submit button available  ########################################
    #return render(request, 'Admin/View Exam.html') ###################


def admin_editexam(request, id):
    res = Exam.objects.get(id = id)
    return render(request, 'Admin/Edit Exam.html', {"data":res})

def admin_deleteexam(request,id):
    res = Exam.objects.filter(id = id).delete()
    return HttpResponse('''<script>alert('Deleted Successfully');window.location='/myapp/admin_viewexam/'</script>''')

def admin_editexam_post(request):
    examname = request.POST['textfield']
    examcode = request.POST['textfield2']
    date = request.POST['textfield3']
    type = request.POST['select']
    id = request.POST['id']

    e = Exam.objects.get(id = id)
    e.examname = examname
    e.examcode = examcode
    e.date = date
    e.type = type
    e.save()
    # Submit button available in html page   #############################
    return HttpResponse('''<script>alert('Added Successfully');window.location='/myapp/admin_viewexam/'</script>''')


def admin_addschedule(request):
    a = Exam.objects.all()
    return render(request, 'Admin/Add Schedule.html', {'data':a})

def admin_addschedule_post(request):

    date = request.POST['textfield']
    fromtime = request.POST['textfield2']
    totime = request.POST['textfield3']
    exam = request.POST['select']

    s = Schedule()
    s.EXAM_id = exam
    s.date = date
    s.fromtime = fromtime
    s.totime = totime
    s.exam = exam
    s.save()

    return HttpResponse('''<script>alert('Added Successfully');window.location='/myapp/admin_addschedule/'</script>''')


def admin_viewschedule(request):
    res = Schedule.objects.all()
    return render (request, 'Admin/View Schedule.html', {'data':res})

def admin_viewschedule_post(request):
    fromdate = request.POST['textfield']
    todate = request.POST['textfield2']
    #return render(request, 'Admin/View Schedule.html') ###################


def admin_editschedule(request, id):
    a = Exam.objects.all()
    res = Schedule.objects.get(id=id)
    return render(request, 'Admin/Edit Schedule.html',{"data":res, "data2":a})

def admin_editschedule_post(request):
    date = request.POST['textfield']
    fromtime = request.POST['textfield2']
    totime = request.POST['textfield3']
    exam = request.POST['select']
    id = request.POST['id']


    s = Schedule.objects.get(id = id)
    s.date = date
    s.fromtime = fromtime
    s.totime = totime
    s.exam = exam    # Value is not given in the HTML page
    s.save()
    return HttpResponse('''<script>alert('Edited Successfully');window.location='/myapp/admin_viewschedule/'</script>''')

def admin_deleteschedule(request,id):
    res = Schedule.objects.filter(id = id).delete()
    return HttpResponse('''<script>alert('Deleted Successfully');window.location='/myapp/admin_viewschedule/'</script>''')

def admin_addstaffallocation(request,id):
    res1 = Staff.objects.all()
    return render(request, 'Admin/Add Staff Allocation.html',{'data1':id,'data':res1})

def admin_addstaffallocation_post(request):
    hdid=request.POST['id1']
    # date = request.POST['textfield']
    staff = request.POST['select2']
    # hh=Hallallocation.objects.get(id=hallallocation)


    s = Staffallocation()
    from datetime import datetime
    date = datetime.now().strftime('%Y-%m-%d')
    s.date = date
    s.HALLALLOCATION_id = hdid
    s.STAFF_id=staff
    s.status = 'Allocated'
    s.save()

    return HttpResponse('''<script>alert('Added Successfully');window.location='/myapp/admin_viewhallallocation/'</script>''')


def admin_viewstaffallocation(request,id):
    res = Staffallocation.objects.filter(HALLALLOCATION_id=id)
    return render(request, 'Admin/View Staff Allocation.html',{'data':res})

def admin_viewstaffallocation_post(request):
    fromdate = request.POST['textfield']
    todate = request.POST['textfield2']
    return render(request, 'Admin/View Staff Allocation.html')
    #href edit&delete ###################################################


def admin_editstaffallocation(request, id):
    res = Staffallocation.objects.get(id=id)
    return render(request, 'Admin/Edit Staff Allocation.html', {"data":res})

def admin_editstaffallocation_post(request):
    staff = request.POST['select']
    date = request.POST['textfield']
    hallallocation = request.POST['select2']  # Value for the hall allocation is not given in the HTML Page
    # Submit button######################################

    s = Staffallocation()
    s.staff = staff
    s.date = date
    s.hallallocation = hallallocation
    s.save()
    return HttpResponse('''<script>alert('Edited Successfully');window.location='/myapp/admin_editstaffallocation/'</script>''')

def admin_deletestaffallocation(request,id):
    res = Staffallocation.objects.filter(id = id).delete()
    return HttpResponse('''<script>alert('Deleted Successfully');window.location='/myapp/admin_viewstaffallocation/'</script>''')


def admin_addstudentallocation(request):
    var = Student.objects.all()
    va = Hallallocation.objects.all()
    return render(request, 'Admin/Add Student Allocation.html',{'data1':var, 'data2':va})

def admin_addstudentallocation_post(request):
    student = request.POST['select2']
    # date = request.POST['textfield2']
    hallallocation = request.POST['select']################
    # Submit Button ##########################################

    s = Studentallocation()
    s.STUDENT_id = student
    from datetime import datetime
    s.date = datetime.now().strftime('%Y-%m-%d')
    s.HALLALLOCATION_id = hallallocation
    s.status = 'Allocated'
    s.save()

    return HttpResponse('''<script>alert('Added Successfully');window.location='/myapp/admin_addstudentallocation/'</script>''')


def admin_viewstudentallocation(request):
    res = Studentallocation.objects.all()
    return render(request, 'Admin/View Student Allocation.html', {'data':res})

def admin_viewstudentallocation_post(request):
    return render(request, 'Admin/View Student Allocation.html')
    # Edit and Delete hyperlink available ##########################


def admin_editstudentallocation(request, id):
    res = Studentallocation.objects.get(id = id)
    var = Student.objects.all()
    va = Hallallocation.objects.all()
    return render(request, 'Admin/Edit Student Allocation.html', {"data":res, "data1":var, "data2":va})

def admin_editstudentallocation_post(request):
    student = request.POST['select2']
    # date = request.POST['textfield2']
    hallallocation = request.POST['select']
    id = request.POST['id']

    s = Studentallocation.objects.get(id=id)
    s.STUDENT_id = student
    from datetime import datetime
    s.date = datetime.now().strftime('%Y-%m-%d')
    s.HALLALLOCATION_id = hallallocation
    s.status = 'Allocated'

    s.save()

    return HttpResponse('''<script>alert('Edited Successfully');window.location='/myapp/admin_viewstudentallocation/'</script>''')


def admin_addhall(request):
    return render(request, 'Admin/Add Hall.html')


def admin_addhall_post(request):
    rno = request.POST['textfield']
    floor = request.POST['textfield2']


    a = Hall()
    a.roomno = rno
    a.floor = floor
    a.save()
    return HttpResponse('''<script>alert('Added Successfully');window.location='/myapp/admin_addhall/'</script>''')


def admin_viewhall(request):
    res=Hall.objects.all()
    return render(request, 'Admin/View Hall.html',{'data':res})

def admin_viewhall_post(request):
    return render(request, 'Admin/View Hall.html')
    #Edit n Delete hyperlink available##########################


def admin_edithall(request, id):
    res = Hall.objects.get(id=id)
    return render(request, 'Admin/Edit Hall.html', {"data":res})

def admin_edithall_post(request):
    roomno = request.POST['textfield']
    floor = request.POST['textfield2']

    a = Hall()
    a.roomno = roomno
    a.floor = floor
    a.save()
    # Edit n delete hyperlink ####################################
    # Submit button
    return HttpResponse('''<script>alert('Edited Successfully');window.location='/myapp/admin_edithall/'</script>''')


def admin_viewcomplaint(request):
    return render(request, 'Admin/View Complaint.html')

def admin_viewcomplaint_post(request):
    fromdate = request.POST['textfield']
    todate = request.POST['textfield2']
    # Submit button #############################
    return render(request, 'Admin/View Complaint.html')


def admin_reply(request):
    return render(request, 'Admin/Reply.html')

def admin_reply_post(request):
    reply = request.POST['textfield']
    # Submit button
    return HttpResponse('''<script>alert('Replied Successfully');window.location='/myapp/admin_reply/'</script>''')


def admin_addhallallocation(request):
    res=Exam.objects.all()
    rr=Hall.objects.all()
    return render(request, 'Admin/Add Hall Allocation.html',{'data2':rr,'data1':res})

def admin_addhallallocation_post(request):
    exam = request.POST['select'] #######################################
    hall = request.POST['select1']
    ex=Exam.objects.get(id=exam)
    date = request.POST['textfield']
    #did=request.POST['id1']
    # Submit Button

    s = Hallallocation()
    s.EXAM = ex
    s.HALL_id=hall
    s.date = date
    s.status = 'Allocated'
    s.save()
    return HttpResponse('''<script>alert('Added Successfully');window.location='/myapp/admin_viewhallallocation/'</script>''')


def admin_viewhallallocation(request):
    res=Hallallocation.objects.all()
    return render(request, 'Admin/View Hall Allocation.html',{'data':res})

def admin_viewhallallocation_post(request):
    fromdate = request.POST['textfield']
    todate = request.POST['textfield2']
    # Submit button
    return render(request, 'Admin/View Hall Allocation.html')


def admin_edithallallocation(request, id):
    res = Hallallocation.objects.get(id = id)
    return render(request, 'Admin/Edit Hall Allocation.html', {"data":res})

def admin_edithallallocation_post(request):
    exam = request.POST['select']  ############################
    hall = request.POST['select2']
    date = request.POST['textfield']

    s = Hallallocation()
    s.exam = exam
    s.hall = hall
    s.date = date
    s.save()
    return HttpResponse('''<script>alert('Edited Successfully');window.location='/myapp/admin_edithallallocation/'</script>''')

def admin_deletehallallocation(request,id):
    res = Hallallocation.objects.filter(id = id).delete()
    return HttpResponse('''<script>alert('Deleted Successfully');window.location='/myapp/admin_viewhallallocation/'</script>''')


#############################################

def authority_changepassword(request):
    return render(request, 'Authority/Change Password.html')

def authority_changepassword_post(request):
    oldpassword = request.POST['textfield']
    newpassword = request.POST['textfield2']
    confirmpassword = request.POST['textfield3']
    return HttpResponse('''<script>alert('Changed Successfully');window.location='/myapp/authority_changepassword/'</script>''')
    # Submit button


def authority_viewexam(request):
    return render(request, 'Authority/View Exam.html')

def authority_viewexam_post(request):
    fromdate = request.POST['textfield']
    todate = request.POST['textfield2']
    # Submit button
    return render(request, 'Authority/View Exam.html')


def authority_viewallocatedstudent(request):
    return render(request, 'Authority/View Allocated Student.html')

def authority_viewallocatedstudent_post(request):
    fromdate = request.POST['textfield']
    todate = request.POST['textfield2']
    # Submit button
    return render(request, 'Authority/View Allocated Student.html')


def authority_viewallocatedstaff(request):
    return render(request, 'Authority/View Allocated staff.html')

def authority_viewallocatedstaff_post(request):
    fromdate = request.POST['textfield']
    todate = request.POST['textfield2']
    # submit button
    return render(request, 'Authority/View Allocated staff.html')


def authority_viewexamhall(request):
    return render(request, 'Authority/View Exam Hall.html')

def authority_viewexamhall_post(request):
    return render(request, 'Authority/View Exam Hall.html')


def authority_viewprofile(request):
    return render(request, 'Authority/View Profile.html')

def authority_viewprofile_post(request):
    return render(request, 'Authority/View Profile.html')


###################################################################

def staff_sendcomplaint(request):
    return render(request, 'Staff/Send Complaint.html')

def staff_sendcomplaint_post(request):
    complaint = request.POST['textfield']
    # Submit button
    return HttpResponse('''<script>alert('Submitted Successfully');window.location='/myapp/staff_sendcomplaint/'</script>''')


def staff_viewallocatedexamhall(request):
    return render(request, 'Staff/View Allocated Exam Hall.html')

def staff_viewallocatedexamhall_post(request):
    return render(request, 'Staff/View Allocated Exam Hall.html')


def staff_viewallocatedexam(request):
    return render(request, 'Staff/View Allocated Exam.html')

def staff_viewallocatedexam_post(request):
    fromdate = request.POST['textfield']
    todate = request.POST['textfield2']
    # Submit button
    return render(request, 'Staff/View Allocated Exam.html')


def staff_viewexamschedule(request):
    return render(request, 'Staff/View Exam Schedule.html')

def staff_viewexamschedule_post(request):
    fromdate = request.POST['textfield2']
    todate = request.POST['textfield']
    # Submit button
    return render(request, 'Staff/View Exam Schedule.html')


def staff_viewprofile(request):
    return render(request, 'Staff/View Profile.html')

def staff_viewprofile_post(request):
    return render(request, 'Staff/View Profile.html')


def staff_viewreply(request):
    return render(request, 'Staff/View Reply.html')

def staff_viewreply_post(request):
    fromdate = request.POST['textfield']
    todate = request.POST['textfield2']
    # Submit button
    return render(request, 'Staff/View Reply.html')


def staff_viewstudentinexamhall(request):
    return render(request, 'Staff/View Student in Exam hall.html')

def staff_viewstudentinexamhall_post(request):
    fromdate = request.POST['textfield']
    todate = request.POST['textfield2']
    # Submit button
    return render(request, 'Staff/View Student in Exam hall.html')






from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from myapp.models import Login


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
    return HttpResponse('''<script>alert('Login Successful');window.location='/myapp/adminhome/'</script>''')


def adminhome(request):
    return render(request,'Admin/Admin Home.html')

def admin_addauthority(request):
    return render(request, 'Admin/Add Authority.html')

def admin_addauthority_post(request):
    name=request.POST['textfield']
    place=request.POST['textfield2']
    Email=request.POST['textfield3']
    phone=request.POST['textfield4']
    post=request.POST['textfield5']
    district=request.POST['textfield6']
    pincode=request.POST['textfield7']
    return HttpResponse('''<script>alert('Added Successfully');window.location='/myapp/admin_addauthority/'</script>''')


def admin_viewauthority(request):
    return render(request, 'Admin/View Authority.html')

def admin_viewauthority_post(request):
    search=request.POST['textfield']
    return render(request, 'Admin/View Authority.html')


def admin_editauthority(request):
    return render(request, 'Admin/Edit Authority.html')

def admin_editauthority_post(request):
    name = request.POST['textfield']
    place = request.POST['textfield2']
    Email = request.POST['textfield3']
    phone = request.POST['textfield4']
    post = request.POST['textfield5']
    district = request.POST['textfield6']
    pincode = request.POST['textfield7']
    return HttpResponse('''<script>alert('Edited Successfully');window.location='/myapp/admin_editauthority/'</script>''')


def admin_addstaff(request):
    return render(request, 'Admin/Add Staff.html')

def admin_addstaff_post(request):
    name = request.POST['textfield']
    place = request.POST['textfield2']
    email = request.POST['textfield3']
    phone = request.POST['textfield4']
    post = request.POST['textfield5']
    district = request.POST['textfield6']
    pincode = request.POST['textfield7']
    return HttpResponse('''<script>alert('Added Successfully');window.location='/myapp/admin_addstaff/'</script>''')


def admin_viewstaff(request):
    return render(request, 'Admin/View Staff.html')

def admin_viewstaff_post(request):
    search = request.POST['textfield']
    return render(request, 'Admin/View Staff.html')

def admin_editstaff(request):
    return render(request, 'Admin/Edit Staff.html')

def admin_editstaff_post(request):
    name = request.POST['textfield']
    place = request.POST['textfield2']
    Email = request.POST['textfield2']
    phone = request.POST['textfield3']
    post = request.POST['textfield5']
    district = request.POST['textfield6']
    pincode = request.POST['textfield7']
    return HttpResponse('''<script>alert('Edited Successfully');window.location='/myapp/admin_editstaff/'</script>''')

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
    #photo = request.POST['fileField']############################
    return HttpResponse('''<script>alert('Added Successfully');window.location='/myapp/admin_addstudent/'</script>''')


def admin_viewstudent(request):
    return render(request, 'Admin/View Student.html')

def admin_viewstudent_post(request):
    return render(request, 'Admin/View Student.html')   ############//


def admin_editstudent(request):
    return render(request, 'Admin/Edit Student.html')

def admin_editstudent_post(request):
    name = request.POST['textfield']
    admissionno = request.POST['textfield2']
    dob = request.POST['textfield3']
    department = request.POST['textfield4']
    course = request.POST['textfield5']
    email = request.POST['textfield6']
    gender = request.POST['textfield7']
    place = request.POST['textfield8']
    #photo = request.POST['fileField']#####################
    return HttpResponse('''<script>alert('Edited Successfully');window.location='/myapp/admin_editstudent/'</script>''')


def admin_addexam(request):
    return render(request, 'Admin/Add Exam.html')

def admin_addexam_post(request):
    examname = request.POST['textfield']
    examcode = request.POST['textfield2']
    date = request.POST['textfield3']
    type = request.POST['select']
    # Submit button available in html page   #############################
    return HttpResponse('''<script>alert('Added Successfully');window.location='/myapp/admin_addexam/'</script>''')


def admin_viewexam(request):
    return render(request, 'Admin/View Exam.html')

def admin_viewexam_post(request):
    fromdate = request.POST['textfield']
    todate = request.POST['textfield2']
    # submit button available  ########################################
    #return render(request, 'Admin/View Exam.html') ###################


def admin_editexam(request):
    return render(request, 'Admin/Edit Exam.html')

def admin_editexam_post(request):
    examname = request.POST['textfield']
    examcode = request.POST['textfield2']
    date = request.POST['textfield3']
    type = request.POST['select']
    # Submit button available in html page   #############################
    return HttpResponse('''<script>alert('Added Successfully');window.location='/myapp/admin_editexam/'</script>''')


def admin_addschedule(request):
    return render(request, 'Admin/Add Schedule.html')

def admin_addschedule_post(request):
    date = request.POST['textfield']
    fromtime = request.POST['textfield2']
    totime = request.POST['textfield3']
    #exam = request.POST['select']#######################
    return HttpResponse('''<script>alert('Added Successfully');window.location='/myapp/admin_addschedule/'</script>''')


def admin_viewschedule(request):
    return render (request, 'Admin/View Schedule.html')

def admin_viewschedule_post(request):
    fromdate = request.POST['textfield']
    todate = request.POST['textfield2']
    #return render(request, 'Admin/View Schedule.html') ###################


def admin_editschedule(request):
    return render(request, 'Admin/Edit Schedule.html')

def admin_editschedule_post(request):
    date = request.POST['textfield']
    fromtime = request.POST['textfield2']
    totime = request.POST['textfield3']
    #exam = request.POST['select']###############################
    return HttpResponse('''<script>alert('Edited Successfully');window.location='/myapp/admin_editschedule/'</script>''')


def admin_addstaffallocation(request):
    return render(request, 'Admin/Add Staff Allocation.html')

def admin_addstaffallocation_post(request):
    #staff = request.POST['select']##################
    date = request.POST['textfield']
    #hallallocation = request.POST['select']###################
    #submit = request.POST['button']#################
    return HttpResponse('''<script>alert('Edited Successfully');window.location='/myapp/admin_addstaffallocation/'</script>''')


def admin_viewstaffallocation(request):
    return render(request, 'Admin/View Staff Allocation.html')

def admin_viewstaffallocation_post(request):
    fromdate = request.POST['textfield']
    todate = request.POST['textfield2']
    return render(request, 'Admin/View Staff Allocation.html')
    #href edit&delete ###################################################


def admin_editstaffallocation(request):
    return render(request, 'Admin/Edit Staff Allocation.html')

def admin_editstaffallocation_post(request):
    #staff = request.POST['select']####################
    date = request.POST['textfield']
    #hallallocation = request.POST['select2']########################
    # Submit button######################################
    return HttpResponse('''<script>alert('Edited Successfully');window.location='/myapp/admin_editstaffallocation/'</script>''')


def admin_addstudentallocation(request):
    return render(request, 'Admin/Add Student Allocation.html')

def admin_addstudentallocation_post(request):
    student = request.POST['textfield']
    date = request.POST['textfield2']
    #hallallocation = request.POST['select']################
    # Submit Button ##########################################
    return HttpResponse('''<script>alert('Added Successfully');window.location='/myapp/admin_addstudentallocation/'</script>''')


def admin_viewstudentallocation(request):
    return render(request, 'Admin/View Student Allocation.html')

def admin_viewstudentallocation_post(request):
    return render(request, 'Admin/View Student Allocation.html')
    # Edit and Delete hyperlink available ##########################


def admin_editstudentallocation(request):
    return render(request, 'Admin/Edit Student Allocation.html')

def admin_editstudentallocation_post(request):
    student = request.POST['textfield']
    date = request.POST['textfield2']
    #hallallocation = request.POST['select']#########
    # submit button
    return HttpResponse('''<script>alert('Edited Successfully');window.location='/myapp/admin_editstudentallocation/'</script>''')


def admin_addhall(request):
    return render(request, 'Admin/Add Hall.html')

def admin_addhall_post(request):
    rollno = request.POST['textfield']
    department = request.POST['textfield2']
    # Submit button ################################
    return HttpResponse('''<script>alert('Added Successfully');window.location='/myapp/admin_addhall/'</script>''')


def admin_viewhall(request):
    return render(request, 'Admin/View Hall.html')

def admin_viewhall_post(request):
    return render(request, 'Admin/View Hall.html')
    #Edit n Delete hyperlink available##########################


def admin_edithall(request):
    return render(request, 'Admin/Edit Hall.html')

def admin_edithall_post(request):
    rollno = request.POST['textfield']
    department = request.POST['textfield2']
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
    return render(request, 'Admin/Add Hall Allocation.html')

def admin_addhallallocation_post(request):
    #exam = request.POST['select']        #######################################
    #hall = request.POST['select2']
    date = request.POST['textfield']
    # Submit Button
    return HttpResponse('''<script>alert('Added Successfully');window.location='/myapp/admin_addhallallocation/'</script>''')


def admin_viewhallallocation(request):
    return render(request, 'Admin/View Hall Allocation.html')

def admin_viewhallallocation_post(request):
    fromdate = request.POST['textfield']
    todate = request.POST['textfield2']
    # Submit button
    return render(request, 'Admin/View Hall Allocation.html')


def admin_edithallallocation(request):
    return render(request, 'Admin/Edit Hall Allocation.html')

def admin_edithallallocation_post(request):
    #exam = request.POST['select']  ############################
    #hall = request.POST['select2']
    date = request.POST['textfield']
    #Submit button
    return HttpResponse('''<script>alert('Edited Successfully');window.location='/myapp/admin_edithallallocation/'</script>''')


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






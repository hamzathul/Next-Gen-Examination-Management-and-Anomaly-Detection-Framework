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
    Email = request.POST['textfield3']
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
    Email = request.POST['textfield3']
    phone = request.POST['textfield4']
    post = request.POST['textfield5']
    district = request.POST['textfield6']
    pincode = request.POST['textfield7']
    return HttpResponse('''<script>alert('Added Successfully');window.location='/myapp/admin_addstaff/'</script>''')

def admin_addstudent(request):
    return render(request, 'Admin/Add Student.html')

def admin_viewstudent(request):
    return render(request, 'Admin/View Student.html')

def admin_editstudent(request):
    return render(request, 'Admin/Edit Student.html')

def admin_addexam(request):
    return render(request, 'Admin/Add Exam.html')

def admin_viewexam(request):
    return render(request, 'Admin/View Exam.html')

def admin_editexam(request):
    return render(request, 'Admin/Edit Exam.html')

def admin_addschedule(request):
    return render(request, 'Admin/Add Schedule.html')

def admin_viewschedule(request):
    return render (request, 'Admin/View Schedule.html')

def admin_editschedule(request):
    return render(request, 'Admin/Edit Schedule.html')

def admin_addstaffallocation(request):
    return render(request, 'Admin/Add Staff Allocation.html')

def admin_viewstaffallocation(request):
    return render(request, 'Admin/View Staff Allocation.html')

def admin_editstaffallocation(request):
    return render(request, 'Admin/Edit Staff Allocation.html')

def admin_addstudentallocation(request):
    return render(request, 'Admin/Add Student Allocation.html')

def admin_viewstudentallocation(request):
    return render(request, 'Admin/View Student Allocation.html')

def admin_editstudentallocation(request):
    return render(request, 'Admin/Edit Student Allocation.html')

def admin_addhall(request):
    return render(request, 'Admin/Add Hall.html')

def admin_viewhall(request):
    return render(request, 'Admin/View Hall.html')

def admin_edithall(request):
    return render(request, 'Admin/Edit Hall.html')

def admin_viewcomplaint(request):
    return render(request, 'Admin/View Complaint.html')

def admin_reply(request):
    return render(request, 'Admin/Reply.html')

def admin_addhallallocation(request):
    return render(request, 'Admin/Add Hall Allocation.html')

def admin_viewhallallocation(request):
    return render(request, 'Admin/View Hall Allocation.html')

def admin_edithallallocation(request):
    return render(request, 'Admin/Edit Hall Allocation.html')

#############################################

def authority_changepassword(request):
    return render(request, 'Authority/Change Password.html')

def authority_viewexam(request):
    return render(request, 'Authority/View Exam.html')

def authority_viewallocatedstudent(request):
    return render(request, 'Authority/View Allocated Student.html')

def authority_viewallocatedstaff(request):
    return render(request, 'Authority/View Allocated staff.html')

def authority_viewexamhall(request):
    return render(request, 'Authority/View Exam Hall.html')

def authority_viewprofile(request):
    return render(request, 'Authority/View Profile.html')

###################################################################

def staff_sendcomplaint(request):
    return render(request, 'Staff/Send Complaint.html')

def staff_viewallocatedexamhall(request):
    return render(request, 'Staff/View Allocated Exam Hall.html')

def staff_viewallocatedexam(request):
    return render(request, 'Staff/View Allocated Exam.html')

def staff_viewexamschedule(request):
    return render(request, 'Staff/View Exam Schedule.html')

def staff_viewprofile(request):
    return render(request, 'Staff/View Profile.html')

def staff_viewreply(request):
    return render(request, 'Staff/View Reply.html')

def staff_viewstudentinexamhall(request):
    return render(request, 'Staff/View Student in Exam hall.html')





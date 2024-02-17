
from django.contrib import admin
from django.urls import path

from myapp import views

urlpatterns = [
    path('login/',views.login),
    path('login_post/', views.login_post),

    path('admin_addauthority/',views.admin_addauthority),
    path('admin_addauthority_post/',views.admin_addauthority_post),

    path('admin_viewauthority/', views.admin_viewauthority),
    path('admin_viewauthority_post/', views.admin_viewauthority_post),

    path('admin_editauthority/<id>', views.admin_editauthority),
    path('admin_editauthority_post/', views.admin_editauthority_post),

    path('admin_addstaff/', views.admin_addstaff),
    path('admin_addstaff_post/', views.admin_addstaff_post),

    path('admin_viewstaff/', views.admin_viewstaff),
    path('admin_viewstaff_post/', views.admin_viewstaff_post),

    path('admin_editstaff/', views.admin_editstaff),
    path('admin_editstaff_post/', views.admin_editstaff_post),

    path('admin_addstudent/', views.admin_addstudent),
    path('admin_addstudent_post/', views.admin_addstudent_post),

    path('admin_viewstudent/', views.admin_viewstudent),
    path('admin_viewstudent_post/', views.admin_viewstudent_post),

    path('admin_editstudent/', views.admin_editstudent),
    path('admin_editstudent_post/', views.admin_editstudent_post),

    path('admin_addexam/', views.admin_addexam),
    path('admin_addexam_post/', views.admin_addexam_post),

    path('admin_viewexam/', views.admin_viewexam),
    path('admin_viewexam_post/', views.admin_viewexam_post),

    path('admin_editexam/', views.admin_editexam),
    path('admin_editexam_post/', views.admin_editexam_post),

    path('admin_addschedule/', views.admin_addschedule),
    path('admin_addschedule_post/', views.admin_addschedule_post),

    path('admin_viewschedule/', views.admin_viewschedule),
    path('admin_viewschedule_post/', views.admin_viewschedule_post),

    path('admin_editschedule/', views.admin_editschedule),
    path('admin_editschedule_post/', views.admin_editschedule_post),

    path('admin_addstaffallocation/', views.admin_addstaffallocation),
    path('admin_addstaffallocation_post/', views.admin_addstaffallocation_post),

    path('admin_viewstaffallocation/', views.admin_viewstaffallocation),
    path('admin_viewstaffallocation_post/', views.admin_viewstaffallocation_post),

    path('admin_editstaffallocation/', views.admin_editstaffallocation),
    path('admin_editstaffallocation_post/', views.admin_editstaffallocation_post),

    path('admin_addstudentallocation/', views.admin_addstudentallocation),
    path('admin_addstudentallocation_post/', views.admin_addstudentallocation_post),

    path('admin_viewstudentallocation/', views.admin_viewstudentallocation),
    path('admin_viewstudentallocation_post/', views.admin_viewstudentallocation_post),

    path('admin_editstudentallocation/', views.admin_editstudentallocation),
    path('admin_editstudentallocation_post/', views.admin_editstudentallocation_post),

    path('admin_addhall/', views.admin_addhall),
    path('admin_addhall_post/', views.admin_addhall_post),

    path('admin_viewhall/', views.admin_viewhall),
    path('admin_viewhall_post/', views.admin_viewhall_post),

    path('admin_edithall/', views.admin_edithall),
    path('admin_edithall_post/', views.admin_edithall_post),

    path('admin_viewcomplaint/', views.admin_viewcomplaint),
    path('admin_viewcomplaint_post/', views.admin_viewcomplaint_post),

    path('admin_reply/', views.admin_reply),
    path('admin_reply_post/', views.admin_reply_post),

    path('admin_addhallallocation/', views.admin_addhallallocation),
    path('admin_addhallallocation_post/', views.admin_addhallallocation_post),

    path('admin_viewhallallocation/', views.admin_viewhallallocation),
    path('admin_viewhallallocation_post/', views.admin_viewhallallocation_post),

    path('admin_edithallallocation/', views.admin_edithallallocation),
    path('admin_edithallallocation_post/', views.admin_edithallallocation_post),

    path('adminhome/', views.adminhome),

    ##################################################################################

    path('authority_changepassword/', views.authority_changepassword),
    path('authority_changepassword_post/', views.authority_changepassword_post),

    path('authority_viewexam/', views.authority_viewexam),
    path('authority_viewexam_post/', views.authority_viewexam_post),

    path('authority_viewallocatedstudent/', views.authority_viewallocatedstudent),
    path('authority_viewallocatedstudent_post/', views.authority_viewallocatedstudent_post),

    path('authority_viewallocatedstaff/', views.authority_viewallocatedstaff),
    path('authority_viewallocatedstaff_post/', views.authority_viewallocatedstaff_post),

    path('authority_viewexamhall/', views.authority_viewexamhall),
    path('authority_viewexamhall_post/', views.authority_viewexamhall_post),

    path('authority_viewprofile/', views.authority_viewprofile),
    path('authority_viewprofile_post/', views.authority_viewprofile_post),

    ###################################################################################

    path('staff_sendcomplaint/', views.staff_sendcomplaint),
    path('staff_sendcomplaint_post/', views.staff_sendcomplaint_post),

    path('staff_viewallocatedexamhall/', views.staff_viewallocatedexamhall),
    path('staff_viewallocatedexamhall_post/', views.staff_viewallocatedexamhall_post),

    path('staff_viewallocatedexam/', views.staff_viewallocatedexam),
    path('staff_viewallocatedexam_post/', views.staff_viewallocatedexam_post),

    path('staff_viewexamschedule/', views.staff_viewexamschedule),
    path('staff_viewexamschedule_post/', views.staff_viewexamschedule_post),

    path('staff_viewprofile/', views.staff_viewprofile),
    path('staff_viewprofile_post/', views.staff_viewprofile_post),

    path('staff_viewreply/', views.staff_viewreply),
    path('staff_viewreply_post/', views.staff_viewreply_post),

    path('staff_viewstudentinexamhall/', views.staff_viewstudentinexamhall),
    path('staff_viewstudentinexamhall_post/', views.staff_viewstudentinexamhall_post)


]


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

    path('admin_editauthority/', views.admin_editauthority),
    path('admin_editauthority_post/', views.admin_editauthority_post),

    path('admin_addstaff/', views.admin_addstaff),
    path('admin_addstaff_post/', views.admin_addstaff_post),

    path('admin_viewstaff/', views.admin_viewstaff),
    path('admin_viewstaff_post/', views.admin_viewstaff_post),

    path('admin_editstaff/', views.admin_editstaff),
    path('admin_addstudent/', views.admin_addstudent),
    path('admin_viewstudent/', views.admin_viewstudent),
    path('admin_editstudent/', views.admin_editstudent),
    path('admin_addexam/', views.admin_addexam),
    path('admin_viewexam/', views.admin_viewexam),
    path('admin_editexam/', views.admin_editexam),
    path('admin_addschedule/', views.admin_addschedule),
    path('admin_viewschedule/', views.admin_viewschedule),
    path('admin_editschedule/', views.admin_editschedule),
    path('admin_addstaffallocation/', views.admin_addstaffallocation),
    path('admin_viewstaffallocation/', views.admin_viewstaffallocation),
    path('admin_editstaffallocation/', views.admin_editstaffallocation),
    path('admin_addstudentallocation/', views.admin_addstudentallocation),
    path('admin_viewstudentallocation/', views.admin_viewstudentallocation),
    path('admin_editstudentallocation/', views.admin_editstudentallocation),
    path('admin_addhall/', views.admin_addhall),
    path('admin_viewhall/', views.admin_viewhall),
    path('admin_edithall/', views.admin_edithall),
    path('admin_viewcomplaint/', views.admin_viewcomplaint),
    path('admin_reply/', views.admin_reply),
    path('admin_addhallallocation/', views.admin_addhallallocation),
    path('admin_viewhallallocation/', views.admin_viewhallallocation),
    path('admin_edithallallocation/', views.admin_edithallallocation),

    path('adminhome/', views.adminhome),

    ##################################################################################

    path('authority_changepassword/', views.authority_changepassword),
    path('authority_viewexam/', views.authority_viewexam),
    path('authority_viewallocatedstudent/', views.authority_viewallocatedstudent),
    path('authority_viewallocatedstaff/', views.authority_viewallocatedstaff),
    path('authority_viewexamhall/', views.authority_viewexamhall),
    path('authority_viewprofile/', views.authority_viewprofile),

    ###################################################################################

    path('staff_sendcomplaint/', views.staff_sendcomplaint),
    path('staff_viewallocatedexamhall/', views.staff_viewallocatedexamhall),
    path('staff_viewallocatedexam/', views.staff_viewallocatedexam),
    path('staff_viewexamschedule/', views.staff_viewexamschedule),
    path('staff_viewprofile/', views.staff_viewprofile),
    path('staff_viewreply/', views.staff_viewreply),
    path('staff_viewstudentinexamhall/', views.staff_viewstudentinexamhall)


]

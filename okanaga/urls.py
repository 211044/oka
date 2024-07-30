from django.urls import path, include
from django.contrib.auth.views import LoginView
from django.views.generic import TemplateView
from . import views

from .views import (
    admin_home,
    register_employee,
    change_password, admin_change_password, login_view, logout_view, doctor_home, uketuke_home, admin_dashboard,
    doctor_patient_search, doctor_medicine_instructions, medicine_confirmation, process_confirmed, treatment_history,
    treatment_history_detail, submit_prescriptions, delete_prescription, doctor_patientid_search, prescription,
    password_change_b, patient_insurance_edit, patient_register, patient_register_success, patient_search_view,
    patient_list, confirm_hospital_phone, change_password2
)

urlpatterns = [

    path('', views.login_view, name='login'),
    path('logout_view/', views.logout_view, name='logout_view'),
    path('login_view/', views.login_view, name='login_view'),
    path('register/', views.register_employee, name='register_employee'),
    path('admin_home/', views.admin_home, name='admin_home'),
    path('doctor_home/', views.doctor_home, name='doctor_home'),
    path('uketuke_home/', views.uketuke_home, name='uketuke_home'),
    path('patient_search/', views.patient_search, name='patient_search'),
    path('admin_home/register_employee/', register_employee, name='register_employee'),
    path('password_change/', change_password, name='change_password'),
    path('admin_password_change/<str:user_id>/', views.admin_change_password, name='admin_change_password'),
    path('accounts/login/', LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('password_change_done/', TemplateView.as_view(template_name='kadai1/password_change_done.html'),
         name='password_change_done'),
    path('admin_password_change_done/', TemplateView.as_view(template_name='kadai1/admin_password_change_done.html'),
         name='admin_password_change_done'),
    path('admin_dashboard/', admin_dashboard, name='admin_dashboard'),
    path('doctor_patient_search/', doctor_patient_search, name='doctor_patient_search'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('doctor_medicine_instructions/<str:patient_id>/', doctor_medicine_instructions,
         name='doctor_medicine_instructions'),
    path('medicine_confirmation/<int:patient_id>/', medicine_confirmation, name='medicine_confirmation'),
    path('process_confirmed/', process_confirmed, name='process_confirmed'),
    path('treatment_history/', treatment_history, name='treatment_history'),
    path('treatment_history_detail/<str:patient_id>/', treatment_history_detail, name='treatment_history_detail'),
    path('submit_prescriptions/<str:patient_id>/', submit_prescriptions, name='submit_prescriptions'),
    path('delete_prescription/<str:patient_id>/<int:index>/', delete_prescription, name='delete_prescription'),
    path('doctor_patientid_search/', doctor_patientid_search, name='doctor_patientid_search'),
    path('prescription/', prescription, name='prescription'),
    path('password_change_b/', password_change_b, name='password_change_b'),
    path('password_change_u/', views.password_change_u, name='password_change_u'),
    path('patient/register/', patient_register, name='patient_register'),
    path('patient/register/success/', patient_register_success, name='patient_register_success'),
    path('patient/search/', patient_search_view, name='patient_search_view'),
    path('patient/list/', patient_list, name='patient_list'),
    path('patient/edit/', patient_insurance_edit, name='patient_insurance_edit'),
    path('patient_searchu/', views.patient_searchu, name='patient_searchu'),
    path('medicine_instructions/<int:patient_id>/', views.medicine_instructions, name='medicine_instructions'),
    path('medicine_confirmation/<str:patient_id>/', views.medicine_confirmation, name='medicine_confirmation'),
    path('prescription_success/', views.prescription_success, name='prescription_success'),

    path('register_hospital/', views.register_hospital, name='register_hospital'),
    path('confirm_hospital_registration/', views.confirm_hospital_registration, name='confirm_hospital_registration'),
    path('confirm_hospital_phone/<str:tabyouinid>/', views.confirm_hospital_phone, name='confirm_hospital_phone'),

    path('hospital_list/', views.hospital_list, name='hospital_list'),
    #path('edit_hospital_phone/<str:tabyouinid>/', views.edit_hospital_phone, name='edit_hospital_phone'),
    path('confirm_hospital_phone/', views.confirm_hospital_phone, name='confirm_hospital_phone'),  # 確認画面用のURLを追加

    path('search_by_capital/', views.search_by_capital, name='search_by_capital'),  # 新しいURLパターンを追加

    path('supplier_registration/', views.supplier_registration, name='supplier_registration'),
    path('supplier_registration_confirm/', views.supplier_registration_confirm, name='supplier_registration_confirm'),
    path('supplier_list/', views.supplier_list, name='supplier_list'),
    path('supplier_search_results/', views.supplier_search_results, name='supplier_search_results'),

    path('password_change2/', change_password2, name='change_password2'),
]

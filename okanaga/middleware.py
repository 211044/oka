# middleware.py
from django.shortcuts import redirect
from django.urls import reverse


class RoleRequiredMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        path = request.path

        user_role = request.session.get('employee_role')

        # ロールベースのアクセス制御
        if path.startswith('/doctor_home/') and user_role != 2:
            return redirect(reverse('login_view'))
        elif path.startswith('/admin_home/') and user_role != 1:
            return redirect(reverse('login_view'))
        elif path.startswith('/uketuke_home/') and user_role != 3:
            return redirect(reverse('login_view'))
        elif path.startswith('/register_employee/') and user_role != 1:
            return redirect(reverse('login_view'))
        elif path.startswith('/admin_dashboard/') and user_role != 1:
            return redirect(reverse('login_view'))
        elif path.startswith('/register_hospital/') and user_role != 1:
            return redirect(reverse('login_view'))
        elif path.startswith('/hospital_list/') and user_role != 1:
            return redirect(reverse('login_view'))
        elif path.startswith('/search_by_capital/') and user_role != 1:
            return redirect(reverse('login_view'))
        elif path.startswith('/supplier_registration/') and user_role != 1:
            return redirect(reverse('login_view'))
        elif path.startswith('/supplier_list/') and user_role != 1:
            return redirect(reverse('login_view'))
        elif path.startswith('/password_change/') and user_role != 2:
            return redirect(reverse('login_view'))
        elif path.startswith('/doctor_patient_search/') and user_role != 2:
            return redirect(reverse('login_view'))
        elif path.startswith('/treatment_history/') and user_role != 2:
            return redirect(reverse('login_view'))
        elif path.startswith('/password_change2/') and user_role != 3:
            return redirect(reverse('login_view'))
        elif path.startswith('/patient_register/') and user_role != 3:
            return redirect(reverse('login_view'))
        elif path.startswith('/patient/edit/') and user_role != 3:
            return redirect(reverse('login_view'))
        elif path.startswith('/patient_searchu/') and user_role != 3:
            return redirect(reverse('login_view'))

        response = self.get_response(request)
        return response

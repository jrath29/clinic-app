from django.urls import path
from front import views

urlpatterns = [
    path("", views.HomeView.as_view(), name="index"),
    path("patients/", views.PatientsHomeView.as_view(), name="patients"),
    path("doctors/", views.DoctorsHomeView.as_view(), name="doctors"),
    path("stock/", views.ProductsHomeView.as_view(), name="stock"),

    path("appointments/create", views.CreateAppointmentView.as_view(), name="create_appointment"),
    path("patients/create", views.CreatePatientView.as_view(), name="create_patient"),
    path("doctors/create", views.CreateDoctorView.as_view(), name="create_doctor"),
    path("stock/create", views.CreateProductView.as_view(), name="create_product"),

    path("appointments/update/<pk>", views.UpdateAppointmentView.as_view(), name="update_appointment"),
    path("patients/update/<pk>", views.UpdatePatientView.as_view(), name="update_patient"),
    path("doctors/update/<pk>", views.UpdateDoctorView.as_view(), name="update_doctor"),
    path("stock/update/<pk>", views.UpdateProductView.as_view(), name="update_product"),

    path("appointments/delete/<pk>", views.DeleteAppointmentView.as_view(), name="delete_appointment"),
    path("patients/delete/<pk>", views.DeletePatientView.as_view(), name="delete_patient"),
    path("doctors/delete/<pk>", views.DeleteDoctorView.as_view(), name="delete_doctor"),
    path("stock/delete/<pk>", views.DeleteProductView.as_view(), name="delete_product"),
]


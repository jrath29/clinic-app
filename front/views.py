from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Appointment, Patient, Doctor, Product
from .forms import FormAppointment, FormPatient, FormDoctor, FormProduct
from django.contrib.messages.views import SuccessMessageMixin

# TemplateView e ListViews ----------------------------------------------------
class HomeView(ListView):
    template_name = "front/index.html"
    model = Appointment
    context_object_name = "appointments"

class PatientsHomeView(ListView):
    template_name = "front/patients/index.html"
    model = Patient
    context_object_name = "patients"

class DoctorsHomeView(ListView):
    template_name = "front/doctors/index.html"
    model = Doctor
    context_object_name = "doctors"

class ProductsHomeView(ListView):
    template_name = "front/stock/index.html"
    model = Product
    context_object_name = "products"

# CreateViews ----------------------------------------------------
class CreateAppointmentView(SuccessMessageMixin, CreateView):
    template_name = "front/appointments/create.html"
    model = Appointment
    form_class = FormAppointment
    context_object_name = "appointment"
    success_url = reverse_lazy("index")
    success_message = "Consulta salva com sucesso!"

class CreatePatientView(SuccessMessageMixin, CreateView):
    template_name = "front/Patients/create.html"
    model = Patient
    form_class = FormPatient
    context_object_name = "patient"
    success_url = reverse_lazy("patients")
    success_message = "Patient foi cadastrado com sucesso!"

class CreateDoctorView(SuccessMessageMixin, CreateView):
    template_name = "front/doctors/create.html"
    model = Doctor
    form_class = FormDoctor
    context_object_name = "doctor"
    success_url = reverse_lazy("doctors")
    success_message = "Doctor foi cadastrado com sucesso!"

class CreateProductView(SuccessMessageMixin, CreateView):
    template_name = "front/stock/create.html"
    model = Product
    form_class = FormProduct
    context_object_name = "product"
    success_url = reverse_lazy("stock")
    success_message = "Produto foi cadastrado com sucesso!"

# UpdateViews ----------------------------------------------------
class UpdateAppointmentView(SuccessMessageMixin, UpdateView):
    template_name = "front/appointments/update.html"
    model = Appointment
    fields = "__all__"
    context_object_name = "appointment"
    success_url = reverse_lazy("index")
    success_message = "Consulta foi atualizada com sucesso!"

class UpdatePatientView(SuccessMessageMixin, UpdateView):
    template_name = "front/patients/update.html"
    model = Patient
    fields = '__all__'
    success_url = reverse_lazy("patients")
    success_message = "Patient foi atualizado com sucesso!"

class UpdateDoctorView(SuccessMessageMixin, UpdateView):
    template_name = "front/doctors/update.html"
    model = Doctor
    fields = '__all__'
    success_url = reverse_lazy("doctors")
    success_message = "Doctor foi atualizado com sucesso!"

class UpdateProductView(SuccessMessageMixin, UpdateView):
    template_name = "front/stock/update.html"
    model = Product
    fields = '__all__'
    success_url = reverse_lazy("stock")
    success_message = "Produto foi atualizado com sucesso!"

# DeleteViews ----------------------------------------------------
class DeleteAppointmentView(SuccessMessageMixin, DeleteView):
    template_name = "front/appointments/delete.html"
    model = Appointment
    context_object_name = "appointment"
    success_url = reverse_lazy("index")
    success_message = "Consulta excluída!"

class DeletePatientView(SuccessMessageMixin, DeleteView):
    template_name = "front/patients/delete.html"
    model = Patient
    context_object_name = "patient"
    success_url = reverse_lazy("patients")
    success_message = "Patient excluído!"

class DeleteDoctorView(SuccessMessageMixin, DeleteView):
    template_name = "front/doctors/delete.html"
    model = Doctor
    context_object_name = "doctor"
    success_url = reverse_lazy("doctors")
    success_message = "Doctor excluído!"

class DeleteProductView(SuccessMessageMixin, DeleteView):
    template_name = "front/stock/delete.html"
    model = Product
    context_object_name = "product"
    success_url = reverse_lazy("stock")
    success_message = "Produto excluído!"
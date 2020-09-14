from django.urls import reverse_lazy
from django.views.generic import FormView,ListView
from django.forms import formset_factory

from .models import Alumno
from .forms import AlumnoForm


class AddAlumno(FormView):
    template_name = 'alumno/add.html'
    form_class = formset_factory(AlumnoForm, extra=2)
    success_url = reverse_lazy('list')

    def form_valid(self, form):

        for f in form:
            print(f.cleaned_data['full_name'])
            f.save()
        return super(AddAlumno, self).form_valid(form)


class ListAlumno(ListView):
    template_name = 'alumno/lista.html'
    model = Alumno
    context_object_name = 'al'

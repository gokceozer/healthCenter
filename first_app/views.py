from django.shortcuts import render
from . import forms
from first_app.models import Patient,Past_Location
from first_app.forms import NewPatientForm, LocationFormSet
# Create your views here.

# Our original index view function
# Corresponds to original_index.html (rename it to index.html to use it!)

# def index(request):
#     my_dict = {'insert_me':"Now I am coming from first_app/index.html!"}
#     # Make sure this is pointing to the correct index
#     return render(request,'first_app/index.html',context=my_dict)


def index(request):
    location_list = Past_Location.objects.order_by('confirm_day')
    patient_list = Patient.objects.order_by('case_no')
    date_dict = {"past_locations":location_list, "patients":patient_list}
    return render(request,'first_app/index.html',date_dict)

def form_name_view(request):
    form = forms.NewPatientForm()
    if request.method == 'GET':
        form = NewPatientForm(request.GET or None)
        formset = LocationFormSet(queryset=Past_Location.objects.none())
        print("Hey1")
    elif request.method == 'POST':
        print("Hey2")
        form = NewPatientForm(request.POST)
        formset = LocationFormSet(request.POST)

        if form.is_valid() and formset.is_valid():
            patient_info = form.save()
            for loc in formset:

                location = loc.save(commit=False)
                location.save()
                location.patient.add(patient_info)
                location.save()

            return index(request)
        else:
            print('Error Form Invalid')

    return render(request, 'first_app/form_page.html', {'form':form,'formset':formset})

def locations(request):
    return render(request, 'first_app/locations.html')

from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    UpdateView,
    ListView
)

from dj_beneficiary.models import (
    Facility,
)

class FacilityCreateView(CreateView):

    model = Facility


class FacilityDeleteView(DeleteView):

    model = Facility


class FacilityDetailView(DetailView):

    model = Facility


class FacilityUpdateView(UpdateView):

    model = Facility


class FacilityListView(ListView):

    model = Facility
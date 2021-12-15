# -*- coding: utf-8 -*-
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    UpdateView,
    ListView
)

from .models import (
	IndividualBeneficiary,
	Facility,
	Province,
	District,
	Ward,
)


class IndividualBeneficiaryCreateView(CreateView):

    model = IndividualBeneficiary


class IndividualBeneficiaryDeleteView(DeleteView):

    model = IndividualBeneficiary


class IndividualBeneficiaryDetailView(DetailView):

    model = IndividualBeneficiary


class IndividualBeneficiaryUpdateView(UpdateView):

    model = IndividualBeneficiary


class IndividualBeneficiaryListView(ListView):

    model = IndividualBeneficiary


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


class ProvinceCreateView(CreateView):

    model = Province


class ProvinceDeleteView(DeleteView):

    model = Province


class ProvinceDetailView(DetailView):

    model = Province


class ProvinceUpdateView(UpdateView):

    model = Province


class ProvinceListView(ListView):

    model = Province


class DistrictCreateView(CreateView):

    model = District


class DistrictDeleteView(DeleteView):

    model = District


class DistrictDetailView(DetailView):

    model = District


class DistrictUpdateView(UpdateView):

    model = District


class DistrictListView(ListView):

    model = District


class WardCreateView(CreateView):

    model = Ward


class WardDeleteView(DeleteView):

    model = Ward


class WardDetailView(DetailView):

    model = Ward


class WardUpdateView(UpdateView):

    model = Ward


class WardListView(ListView):

    model = Ward


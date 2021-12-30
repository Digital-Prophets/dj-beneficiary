# -*- coding: utf-8 -*-
from django.urls import path

from dj_beneficiary import views

urlpatterns = [
    path(
        "Facility/create/",
        view=views.FacilityCreateView.as_view(),
        name='Facility_create',
    ),
    path(
        "Facility/<int:pk>/delete/",
        view=views.FacilityDeleteView.as_view(),
        name='Facility_delete',
    ),
    path(
        "Facility/<int:pk>/",
        view=views.FacilityDetailView.as_view(),
        name='Facility_detail',
    ),
    path(
        "Facility/<int:pk>/update/",
        view=views.FacilityUpdateView.as_view(),
        name='Facility_update',
    ),
    path(
        "Facility/",
        view=views.FacilityListView.as_view(),
        name='Facility_list',
    ),
]

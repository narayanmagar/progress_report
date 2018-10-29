# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views.generic import ListView, TemplateView, DetailView
from django.shortcuts import render, get_object_or_404

from django.views.generic import View
from django.shortcuts import render, redirect
from django.http import HttpResponse

class DashboardView(TemplateView):

    template_name = "marksheet/dashboard.html"

   
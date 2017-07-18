# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.

from datetime import datetime

from django.shortcuts import render, redirect
from forms import SignUpForm, LoginForm
from models import UserModel
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password, check_password

# Create your views here.


def signup_view(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            # saving data to DB
            user = UserModel(name=name, password=make_password(password), email=email, username=username)
            user.save()
        return render(request, 'success.html')
    elif request.method == 'GET':
        form = SignUpForm()

        return render(request, 'index.html', {'form': form})


def login_view(request):
    if request.method == "POST":
        form = LoginForm()
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = UserModel.username.filter(username=username).first()

            if user:
                # Check for the password
                if check_password(password, user.password):
                    print 'User is valid'
                else:
                    print 'User is invalid'
        form = LoginForm(request.POST)
    elif request.method == "GET":
        form = LoginForm()

        return render(request, 'login.html', {'form': form})
from django.shortcuts import render
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from .models import *
import os
from django.contrib.auth.models import User
from django.contrib import messages



# Create your views here.
def homepage(req):
    return render( req, 'homepage.html')
def sec(req):
    return render(req ,'sec.html')
 
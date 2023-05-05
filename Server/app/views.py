from django.shortcuts import render
from django.http import HttpResponse


def register(request):
    return HttpResponse("Register")


def login(request):
    return HttpResponse("Login")


def change_pass(request):
    return HttpResponse("Change pass")


def add_client(request):
    return HttpResponse("Add new client")


def gen_otp(request):
    return HttpResponse("Generate one-time password")


def verify_otp(request):
    return HttpResponse("Verify one-time password")

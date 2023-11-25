from django.shortcuts import render
from .character import Character


def create_character(request):
    template_name = "chargen/create_character.html"
    context = {"char": Character}
    return render(request, template_name, context)

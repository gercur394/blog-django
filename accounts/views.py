from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import RegistroForm, PerfilForm
from .models import Perfil

def registro(request):
    if request.method == "POST":
        form = RegistroForm(request.POST)
        if form.is_valid():
            usuario = form.save()
            Perfil.objects.create(user=usuario)
            return redirect("login")
    else:
        form = RegistroForm()
    return render(request, "accounts/registro.html", {"form": form})


@login_required
def ver_perfil(request):
    perfil, creado = Perfil.objects.get_or_create(user=request.user)
    return render(request, "accounts/perfil.html", {"perfil": perfil})


@login_required
def editar_perfil(request):
    perfil, creado = Perfil.objects.get_or_create(user=request.user)
    if request.method == "POST":
        form = PerfilForm(request.POST, request.FILES, instance=perfil)
        if form.is_valid():
            form.save()
            return redirect("ver_perfil")
    else:
        form = PerfilForm(instance=perfil)
    return render(request, "accounts/editar_perfil.html", {"form": form})
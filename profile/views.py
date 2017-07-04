from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate, logout
from .models import Profile
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import UserForm, UserProfileForm


def home(request):
    return render(request, 'profile/home.html', {})


def sign_up(request):
    if request.method == "POST":
        uform = UserForm(data=request.POST)
        pform = UserProfileForm(data=request.POST)
        if uform.is_valid() * pform.is_valid():
            user = User.objects.create_user(username=uform.cleaned_data["username"],
                                            password=uform.cleaned_data["password1"])
            profile = Profile.objects.create(user=user, **pform.cleaned_data)
            profile.save()
            return redirect('home')

    else:
        uform = UserForm()
        pform = UserProfileForm()
    return render(request, 'profile/sign_up.html', {'uform': uform,
                                                    'pform': pform})


def log_in(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            # Redirect to a success page.
            # profile = Profile.objects.filter(user=User.objects.filter(username=username))[0]
            profile = get_object_or_404(Profile, user=request.user)
            print(profile)
            return render(request, 'profile/profile.html', {'profile': profile})
    else:
        return render(request, 'profile/log_in.html', {})


def profile(request):
    profile = get_object_or_404(Profile, user=request.user)
    return render(request, 'profile/profile.html', {'profile': profile})


@login_required()
def edit_profile(request):
    profile = Profile.objects.get(user=request.user)
    if request.method == "POST":
        pform = UserProfileForm(request.POST, instance=profile)
        if pform.is_valid():
            pform.save()
            return redirect('home')
    else:
        pform = UserProfileForm(instance=profile)
    return render(request, 'profile/edit.html', {'pform': pform})


@login_required()
def log_out(request):
    logout(request)
    return redirect('home')


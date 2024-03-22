from django.shortcuts import render, redirect
from user.forms import SignUpForm, CustomLoginForm
from django.contrib.auth.views import LoginView, LogoutView

def sign_up(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("user:sign_in")
    else:
        form = SignUpForm()
    data = {
        "form": form,
    }
    return render(request, "registration/signup.html", data)

class LoginView(LoginView):
    template_name = "registration/signin.html"
    authentication_form = CustomLoginForm

    # def form_valid(self, form):
    #     response = super().form_valid(form)
    #     return super().form_valid(form)
    


# def sign_in(request):
#     return render(request, "registration/signin.html",)
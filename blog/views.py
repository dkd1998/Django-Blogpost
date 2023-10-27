from django.shortcuts import render


# Funtion to load the landing page


def landing_page(request):
    return render(request, "blog/index.html")

# Funtion to load the landing page


def posts(request):
    pass

# Funtion to load the landing page


def individual_post(request):
    pass

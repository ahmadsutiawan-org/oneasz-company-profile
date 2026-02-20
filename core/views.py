from django.shortcuts import render


def index(request):
    return render(request, "menus/home_page.html", {"active_menu": "home"})


def home_page(request):
    template_name = "menus/home_page.html"
    context = {"active_menu": "home"}
    if request.headers.get("HX-Request"):
        return render(request, template_name + "#content_fragment", context)
    return render(request, template_name, context)


def service_page(request):
    template_name = "menus/service_page.html"
    context = {"active_menu": "services"}
    if request.headers.get("HX-Request"):
        return render(request, template_name + "#content_fragment", context)
    return render(request, template_name, context)


def project_page(request):
    template_name = "menus/project_page.html"
    context = {"active_menu": "projects"}
    if request.headers.get("HX-Request"):
        return render(request, template_name + "#content_fragment", context)
    return render(request, template_name, context)


def about_page(request):
    template_name = "menus/about_page.html"
    context = {"active_menu": "about"}
    if request.headers.get("HX-Request"):
        return render(request, template_name + "#content_fragment", context)
    return render(request, template_name, context)


def contact_page(request):
    template_name = "menus/contact_page.html"
    context = {"active_menu": "contact"}
    if request.headers.get("HX-Request"):
        return render(request, template_name + "#content_fragment", context)
    return render(request, template_name, context)

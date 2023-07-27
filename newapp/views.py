from django.shortcuts import render, HttpResponse
from newapp.models import student
from newapp.models import super_user, superduper_user
# Create your views here.

def tittle(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password= request.POST.get('password')
        confirm_password= request.POST.get('confirm_password')

        sav = super_user.objects.create(
            username = username,
            email = email,
            password = password,
            confirm_password = confirm_password,
         )

        sav.save()
        return HttpResponse('value added to database!')
    return render(request, 'index.html')

# to add photo
def superadd(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password= request.POST.get('password')
        confirm_password= request.POST.get('confirm_password')
        photo= request.FILES.get('photo')

        sav = superduper_user.objects.create(
            username = username,
            email = email,
            password = password,
            confirm_password = confirm_password,
            photo = photo
         )

        sav.save()
        return HttpResponse('value added to database!')
    return render(request, 'index.html')


def show_title(request):
    obj = superduper_user.objects.all()
    return render(request, 'show.html', {'obj': obj})

# for edit the user id
def edit_title(request, u_id):
    obj = super_user.objects.get(id= u_id)

    if request.method =="POST":
 
        obj.username = request.POST.get('username')
        obj.email = request.POST.get('email')
        obj.password = request.POST.get('password')
        obj.confirm_password = request.POST.get('confirm_password')

        obj.save()
        return HttpResponse("value updated !")
    return render(request, 'index.html')


# for deleter the user
def delete_title(request, u_id):
    obj = super_user.objects.get(id= u_id)
    obj.delete()
    return HttpResponse('value deleted!')
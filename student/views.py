
# Create your views here.
from django.shortcuts import render, redirect
from .models import Sms

# Show all records
def index(request):
    data = Sms.objects.all()
    return render(request, "index.html", {"data": data})

# Show form
def create(request):
    return render(request, "create.html")

# Insert Record
def insert(request):
    if request.method == "POST":
        name = request.POST.get("name")
        mobile = request.POST.get("mobile")
        message = request.POST.get("message")
        photo = request.FILES.get("photo")

        Sms.objects.create(
            name=name,
            mobile=mobile,
            message=message,
            photo=photo
        )
    return redirect("/")

# Edit form
def edit(request, id):
    record = Sms.objects.get(id=id)
    return render(request, "edit.html", {"record": record})

# Update Record
def update(request, id):
    record = Sms.objects.get(id=id)

    if request.method == "POST":
        record.name = request.POST['name']
        record.mobile = request.POST['mobile']
        record.message = request.POST['message']

        if request.FILES.get("photo"):
            record.photo = request.FILES.get("photo")

        record.save()
        return redirect("/")

# Delete
def delete(request, id):
    record = Sms.objects.get(id=id)
    record.delete()
    return redirect("/")

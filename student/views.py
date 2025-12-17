
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
# def insert(request):
#     if request.method == "POST":
#         name = request.POST.get("name")
        
#         mobile = request.POST.get("mobile")
#         message = request.POST.get("message")
#         photo = request.FILES.get("photo")

#         Sms.objects.create(
#             name=name,
#             mobile=mobile,
#             message=message,
#             photo=photo
#         )
#     return redirect("/")

def insert(request):
    errors = {}

    if request.method == "POST":
        name = request.POST.get('name', '').strip()
        mobile = request.POST.get('mobile', '').strip()
        message = request.POST.get('message', '').strip()
        photo = request.FILES.get('photo')

        # 🔴 Name validation
        if not name:
            errors['name'] = "Name is empty"
        elif len(name) < 3:
            errors['name'] = "Name must be at least 3 characters"
        elif not name.isalpha():
            errors['name'] = "Name must contain only letters"

        # 🔴 Mobile validation
        if not mobile:
            errors['mobile'] = "Mobile is required"
        elif not mobile.isdigit() or len(mobile) != 10:
            errors['mobile'] = "Enter valid 10 digit mobile number"
        elif mobile[0] not in ['6', '7', '8', '9']:
            errors['mobile'] = "Invalid Indian mobile number"

        # 🔴 Message validation
        if not message:
            errors['message'] = "Message is required"
        elif len(message) < 5:
            errors['message'] = "Message must be at least 5 characters"

        # 🔴 Photo validation (optional)
        if photo:
            if photo.size > 2 * 1024 * 1024:
                errors['photo'] = "Image size must be below 2MB"

        # ✅ Save if no errors
        if not errors:
            from .models import Sms
            Sms.objects.create(
                name=name,
                mobile=mobile,
                message=message,
                photo=photo
            )
            return redirect('/')

    return render(request, 'create.html', {
        'errors': errors,
        'data': request.POST
    })
    
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

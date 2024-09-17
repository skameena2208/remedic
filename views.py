from django.shortcuts import render, redirect
from .forms import ContactForm1, ContactForm2
from .models import Contact_2


# Create your views here.
def index(request):
    return render(request, "index.html", {})


def about(request):
    return render(request, "about.html", {})


def contact(request):
    if request.method == "POST":
        form = ContactForm1(request.POST)
        print(form.errors)
        if form.is_valid():
            form.save()
            return render(request, "contact.html", {"msg": "Submitted Contact Form"})
        return render(request, "contact.html", {"msg": "Not Submitted Contact Form"})
    return render(request, "contact.html", {})


def register(request):
    if request.method == "POST":
        form = ContactForm2(request.POST, request.FILES)
        print(form.errors)
        email = request.POST['email']
        if Contact_2.objects.filter(email=email).exists():
            return render(request, "register.html", {"msg": "This is email is already exists"})
        else:
            if form.is_valid():
                form.save()
                return render(request, "customer.html", {"msg": "Registered"})
            return render(request, "customer.html", {"msg": "Not Registered"})
    return render(request, "register.html", {})


def customer(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        log = Contact_2.objects.filter(email=email, password=password)
        if log.exists():
            if log[0].status == "Accepted":
                request.session['email'] = email
                return render(request, "login.html", {"msg": "Accepted Successfully"})
            elif log[0].status == "Rejected":
                return render(request, "customer.html", {"msg": "Rejected Login"})
            else:
                return render(request, "customer.html", {"msg": "Pending"})
        return render(request, "customer.html", {"msg": "Login Failed"})
    return render(request, "customer.html", {})


def customer_home(request):
    return render(request, "login.html", {})


def logout(request):
    request.session.flush()
    return redirect('/customer')


def customer_profile(request):
    email = request.session['email']
    profile = Contact_2.objects.get(email=email)
    return render(request, "customer_profile.html", {"x": profile})


def admin(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        log = Contact_2.objects.filter(email=email, password=password)
        if log.exists():
            request.session['email'] = email
            return render(request, "admin_home.html", {})
        return render(request, "admin.html", {})
    return render(request, "admin.html", {})


def logout1(request):
    request.session.flush()
    return redirect('/admin')


def admin_home(request):
    return render(request, "admin.html", {})


def view_contact(request):
    contact = Contact_2.objects.all()
    return render(request, "view_contact.html", {"contact": contact})


def view_customer(request):
    customer = Contact_2.objects.all()
    return render(request, "view_customer.html", {"customer": customer})


def accept_customer(request, id):
    cus = Contact_2.objects.get(id=id)
    cus.status = "Accepted"
    cus.save()
    return redirect('/view_customer')


def deActive_customer(request, id):
    cus = Contact_2.objects.get(id=id)
    cus.status = "DeActive"
    cus.save()
    return redirect('customer')

def reject_customer(request, id):
    cus = Contact_2.objects.get(id=id)
    cus.status = "Rejected"
    cus.save()
    return redirect('/view_customer')


def edit(request):
    email = request.session['email']
    customer = Contact_2.objects.get(email=email)
    return render(request, 'edit.html', {'x': customer})


def update(request):
    if request.method == 'POST':
        id = request.POST['id']
        cust = Contact_2.objects.get(id=id)
        form = ContactForm2(request.POST, request.FILES, instance=cust)
        print(form.errors)
        if form.is_valid():
            form.save()
            return redirect('/customer_profile')
        return render(request, 'edit.html', {})
    return render(request, 'edit.html', {})


def is_login(request):
    if request.session.__contains__('email'):
        return True
    else:
        return False


def customer_change_password(request):
    if is_login(request):
        if request.method=='POST':
            email=request.session['email']
            password=request.POST['password']
            new_password=request.POST['new_password']
            try:
                cust=ContactForm2.objects.get(email=email,password=password)
                cust.password=new_password
                cust.save()
                return redirect('/login')
            except Exception as e:
                print(e)
                return render(request,"customer_change_password.html",{"msg":"invalid credentials"})
        return render(request,"customer_change_password.html",{})
    return render(request, "customer_change_password.html", {})




import datetime

from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

# Create your views here.
from Build.models import *

def index(request):
    return render(request,"index.html")


def loginS(request):
    return render(request,"worker/login.html")

def loginbuttonclick(request):
    username = request.POST['textfield']
    password = request.POST['textfield2']

    request.session['login'] = '1'

    lobj=login.objects.filter(username = username,password=password)
    if lobj.exists():
        lobj = lobj[0]
        if lobj.usertype == 'admin':
            return HttpResponse("<script>alert('login successfull');window.location='/home_page'</script>")
        elif lobj.usertype == 'worker':
            request.session['lid'] = lobj.id
            request.session['wid'] = worker.objects.get(LOGIN=request.session['lid']).id
            print("worker_id",request.session['wid'])
            return HttpResponse("<script>alert('login successfull');window.location='/workerlink'</script>")

        else:
            return HttpResponse("<script>alert('invalid');window.location='/'</script>")
    else:
        return HttpResponse("<script>alert('invalid');window.location='/'</script>")




def register(request):

    return render(request,"worker/register.html")

def registerbuttonclick(request):
    Name = request.POST['textfield']
    Age = request.POST['textfield2']
    Phoneno = request.POST['textfield3']
    Email = request.POST['textfield4']
    Gender = request.POST['textfield5']
    Pincode = request.POST['textfield6']
    Postoffice = request.POST['textfield7']
    Place = request.POST['textfield8']
    Latidude = request.POST['textfield9']
    Longitude = request.POST['textfield9']
    Password = request.POST['textfield11']
    Confirmpassword = request.POST['textfield12']
    Skills = request.POST['s']
    Qualification = request.POST['q']


    if Password==Confirmpassword:
        obj = login()
        obj.username = Email
        obj.password = Password
        obj.usertype = 'pending'
        obj.save()

        obj1 = worker()
        obj1.name = Name
        obj1.age = Age
        obj1.phone_number = Phoneno
        obj1.email = Email
        obj1.gender = Gender
        obj1.pincode = Pincode
        obj1.post_office = Postoffice
        obj1.place = Place
        obj1.latitude = Latidude
        obj1.longitude = Longitude
        obj1.skills=Skills
        obj1.qualification=Qualification
        obj1.LOGIN_id = obj.id
        obj1.save()

        return HttpResponse("<script>alert('Added');window.location='/'</script>")
    else:
        return HttpResponse("<script>alert('Incorrect password');window.location='/'</script>")

def view_and_edit_profile(request):

    data = worker.objects.get(id = request.session['wid'])
    return render(request,"worker/view and edit profile.html",{'data':data})

def view_and_edit_profilebuttonclick(request):
    Name = request.POST['textfield']
    Age = request.POST['textfield2']
    Phoneno = request.POST['textfield3']
    Email = request.POST['textfield4']
    Gender = request.POST['textfield5']
    Pincode = request.POST['textfield6']
    Postoffice = request.POST['textfield7']
    Place = request.POST['textfield8']
    Latidude = request.POST['textfield9']
    Longitude = request.POST['textfield9']

    worker.objects.filter(id = request.session['wid']).update(name = Name,age = Age,phone_number = Phoneno,email = Email,gender = Gender,pincode = Pincode,post_office = Postoffice,place = Place,latitude = Latidude,longitude =Longitude)

    return HttpResponse("<script>alert('Updated');window.location='/view_and_edit_profile'</script>")

def add_portfolio(request):
    return render(request,"worker/add portfolio.html")

def add_portfoliobuttonclick(request):
    Image1 = request.FILES['fileField']
    Image2 = request.FILES['fileField2']
    Image3 = request.FILES['fileField3']
    Image4 = request.FILES['fileField4']
    Type = request.POST['select']
    Experience = request.POST['textarea']

    fs = FileSystemStorage()
    d = datetime.datetime.now().strftime('%Y%m%d-%H%M%S')
    fs.save(r"D:\2024-2025\Depaul\19-12-2024\Bulid connect\BuildConnect\BuildConnect\Build\static\\"+d+'1.jpg',Image1)
    path1 = '/static/'+d+'1.jpg'
    d2 = datetime.datetime.now().strftime('%y%m%d-%H%M%S')
    fs.save(r"D:\2024-2025\Depaul\19-12-2024\Bulid connect\BuildConnect\BuildConnect\Build\static\\" + d2 + '2.jpg', Image2)
    path2 = '/static/' + d2 + '2.jpg'

    d3 = datetime.datetime.now().strftime('%y%m%d-%H%M%S')
    fs.save(r"D:\2024-2025\Depaul\19-12-2024\Bulid connect\BuildConnect\BuildConnect\Build\static\\" + d3 + '3.jpg', Image3)
    path3 = '/static/' + d3 + '3.jpg'

    d4 = datetime.datetime.now().strftime('%y%m%d-%H%M%S')
    fs.save(r"D:\2024-2025\Depaul\19-12-2024\Bulid connect\BuildConnect\BuildConnect\Build\static\\" + d4 + '4.jpg', Image4)
    path4 = '/static/' + d4 + '4.jpg'

    obj1 = portfolio()
    obj1.image1 = path1
    obj1.image2 = path2
    obj1.image3 = path3
    obj1.image4 = path4
    obj1.type = Type
    obj1.experience = Experience
    obj1.WORKER_id = request.session['wid']
    obj1.save()
    return HttpResponse("<script>alert('Added');window.location='/view_portfolio'</script>")

def edit_portfolio(request):
    return render(request,"worker/edit portfolio.html")
def edit_portfoliobuttonclick(request,id):

    Type = request.POST['select']
    Experience = request.POST['textarea']


    if "fileField" in request.FILES:
        Image1 = request.FILES['fileField']
        fs = FileSystemStorage()
        d = datetime.datetime.now().strftime('%Y%m%d-%H%M%S')
        fs.save(r"D:\2024-2025\Depaul\19-12-2024\Bulid connect\BuildConnect\BuildConnect\Build\static\\" + d + '1.jpg', Image1)
        path1 = '/static/' + d + '1.jpg'

        portfolio.objects.filter(id=id).update(image1=path1)




    if "fileField2" in request.FILES:
        Image2 = request.FILES['fileField2']
        fs=FileSystemStorage()
        d2 = datetime.datetime.now().strftime('%y%m%d-%H%M%S')
        fs.save(r"D:\2024-2025\Depaul\19-12-2024\Bulid connect\BuildConnect\BuildConnect\Build\static\\" + d2 + '2.jpg', Image2)
        path2 = '/static/' + d2 + '2.jpg'
        #
        portfolio.objects.filter(id=id).update(image2=path2)





    if "fileField3" in request.FILES:
        Image3 = request.FILES['fileField3']
        d3 = datetime.datetime.now().strftime('%y%m%d-%H%M%S')
        fs=FileSystemStorage()
        fs.save(r"D:\2024-2025\Depaul\19-12-2024\Bulid connect\BuildConnect\BuildConnect\Build\static\\" + d3 + '3.jpg', Image3)
        path3 = '/static/' + d3 + '3.jpg'
        portfolio.objects.filter(id=id).update(image3=path3)





    if "fileField4" in request.FILES:
        Image4 = request.FILES['fileField4']
        fs=FileSystemStorage()
        d4 = datetime.datetime.now().strftime('%y%m%d-%H%M%S')
        fs.save(r"D:\2024-2025\Depaul\19-12-2024\Bulid connect\BuildConnect\BuildConnect\Build\static\\" + d4 + '4.jpg', Image4)
        path4 = '/static/' + d4 + '4.jpg'
        portfolio.objects.filter(id=id).update(image4=path4)

    portfolio.objects.filter(id=id).update(type=Type,experience=Experience)

    return HttpResponse("<script>alert('Updated');window.location='/view_portfolio'</script>")

def view_portfolio(request):
    data = portfolio.objects.filter(WORKER=request.session['wid'])
    return render(request, "worker/view portfolio.html", {'data': data})


def update(request,id):
    view=portfolio.objects.get(id=id)
    return render(request,"worker/edit portfolio.html",{"data":view})

def update_post(request,id):
    portfolio.objects.filter(id=id).update(status="updated")

def delete(request,id):
    portfolio.objects.filter(id=id).delete()
    return HttpResponse("<script>alert('Deleted');window.location='/view_portfolio'</script>")


#
def view_user_request(request):
    data = requests.objects.filter(PORTFOLIO__WORKER=request.session['wid'],status='pending')
    return render(request,'worker/view user request.html',{'data':data})


def approve(request,id):
    requests.objects.filter(id=id).update(status="approved")

    return HttpResponse("<script>alert('approved');window.location='/approve_request'</script>")

def reject(request,id):
    requests.objects.filter(id=id).update(status="rejected")

    return HttpResponse("<script>alert('rejected');window.location='/view_user_request'</script>")


def approve_request(request):
    data = requests.objects.filter(PORTFOLIO__WORKER=request.session['wid'],status='approved')
    return render(request, 'worker/approve request.html', {'data': data})


def add_budget(request,id):
    return render(request,"worker/add budget.html",{'id':id})
def add_budgetbuttonclick(request,id):
    Budget = request.POST['textfield']
    if budget.objects.filter(REQUEST_id = id).exists():
        budget.objects.filter(REQUEST_id = id).update(status = 'pending',price = Budget)
    else:
        obj1=budget()
        obj1.price = Budget
        obj1.REQUEST_id = id
        obj1.status = 'pending'
        obj1.save()
    return HttpResponse("<script>alert('Budget added');window.location='/view_status'</script>")

def view_status(request):
    data = budget.objects.filter(REQUEST__PORTFOLIO__WORKER=request.session['wid'])
    return  render(request,"worker/view status.html",{'data':data})

def add_material(request,id):
    return  render(request,"worker/add material.html",{'id':id})
def add_materialtbuttonclick(request,id):
    Material = request.POST['textfield']
    Quantity = request.POST['textfield']
    Details = request.POST['textfield']

    obj=material()
    obj.material=Material
    obj.quantity=Quantity
    obj.details=Details
    obj.REQUEST_id = id
    obj.save()

    return HttpResponse("<script>alert('material added');window.location='/view_status'</script>")

def view_material(request,id):
    view=material.objects.filter(REQUEST=id)
    return  render(request,"worker/view_material.html",{'view':view})

def delete_material(request,id):
    m = material.objects.get(id=id)
    id = m.REQUEST_id
    m.delete()
    return HttpResponse("<script>alert('deleted');window.location='/view_material/"+str(id)+"'</script>")


def add_advance_amount(request):
    return render(request,"worker/add advance amount.html")
def add_advance_amountbuttonclick(request):
    Advance_amount = request.POST['textfield']
    return HttpResponse("<script>alert('added');window.location='/view_advance_amount'</script>")


def view_advance_amount(request,id):
    data = payment.objects.filter(REQUEST=id)
    return render(request,"worker/view advance payment.html", {'data': data})


def view_complaint_from_user(request):
    data = complaint.objects.filter(WORKER=request.session['wid'])
    return render(request, 'worker/view complaint from user.html', {'data': data})


def send_reply(request,id):
    return render(request,"worker/send reply.html",{'id':id})
def send_replybuttonclick(request,id):
    Reply = request.POST['textfield']
    complaint.objects.filter(id=id).update(reply=Reply,reply_date=datetime.datetime.now())

    return HttpResponse("<script>alert('reply sended');window.location='/view_complaint_from_user'</script>")

def change_password(request):
    return render(request,"worker/change password.html")
def change_passwordbuttonclick(request):
    Old_password = request.POST['textfield']
    New_password = request.POST['textfield2']
    confirm_password = request.POST['textfield3']

    password1 = login.objects.filter(password=Old_password)
    if password1.exists():
        if New_password == confirm_password:
            login.objects.filter(id=request.session['lid']).update(password = New_password)
            return HttpResponse("<script>alert('password changed');window.location='/change_password'</script>")
        else:
            return HttpResponse("<script>alert('Incorrect password');window.location='/change_password'</script>")
    else:
        return HttpResponse("<script>alert('Invalid password');window.location='/change_password'</script>")



def view_review_and_rating(request):
    data = review.objects.filter(WORKER=request.session['wid'])
    return render(request, 'worker/view review and rating.html', {'data': data})


def workerlink(request):
    return render(request,"worker/index.html")



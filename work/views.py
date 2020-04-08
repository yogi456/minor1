from django.shortcuts import render, redirect
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.models import User
from . models import *
from . forms import *
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib import messages
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required

#to generate otp




# Create your views here.
def homepageview(request):
    return render(request,"index.html")

def aboutus(request):
    return render(request,'about.html')


#view for signUp
def usercreationview(request):
    template="SignUp.html"
    form = UserCreationForm(request.POST)
    if request.method == "POST":
        username = request.POST['username']
        usermail = request.POST['usermail']
        usercontact = request.POST['usercontact']
        userfirstname = request.POST['userfirstname']
        userlastname = request.POST['userlastname']
        userpassword = request.POST['userpassword']
        userconfirmpassword= request.POST['userconfirmpassword']
        userlocation = request.POST['userlocation']
        userDoB = request.POST['userDoB']
        usergender = request.POST['usergender']
        if User.objects.filter(username = request.POST['username']).exists():
            return render(request,template,{'form':form,'error_message':'Username already exists'})
        elif User.objects.filter(email = usermail).exists():
            return render(request,template,{'form':form,'error_message':'Email already exists'})
        elif userpassword != userconfirmpassword:
            return render(request, template, {
                    'form': form,
                    'error_message': 'Passwords do not match.'
                })
        else:
            user = User(username = username)
            user.set_password(userpassword)
            user.email= usermail
            user.save()
            details = UserDetails()
            details.username = username
            details.usermail = usermail
            details.userfirstname = userfirstname
            details.userlastname = userlastname
            details.userpassword = userpassword
            details.userlocation = userlocation
            details.usercontact = usercontact
            details.userDoB = userDoB
            details.usergender= usergender
            details.save()
            print(username, userpassword, usermail, userDoB)
            return redirect('/login')
    else:
        form = UserCreationForm()
    return render(request,"SignUp.html",{'form':form})




#admin never get logged in
# Created login view here.
def login_me(request):
    form = LoginForm(request.POST)
    template = 'login.html'
    if request.method == "POST":
        if form.is_valid():
            username = request.POST['username']
            user = User.objects.get(username=username)
            password = request.POST['password']
            user.backend = 'django.contrib.auth.backends.ModelBackend'
            user = authenticate(username=username, password=password)
            if user.is_active:
                messages.success(request, "successful login!")
                print("aagya yha tk")
                login(request,user)
                print(username)
                messages.success(request, "successful login!")
                #model = UserDetails.username
                #return render(request,'profile.html',{'model':model})
                return redirect(profile,username)

            else:
                messages.success(request, "invalid login Details")
                return redirect('/login')
    else:
            messages.success(request, "No user Found")
    return render(request,template,{'form':form})






@login_required
def profile(request,username):
    print(username)
    model2 = BookDetails.objects.filter(username=username)
    model = UserDetails.objects.get(username=username)
    model3 = BookRequest.objects.filter(owner = username)
    return render(request,'profile.html',{'model':model,'model2':model2,'model3':model3})





#creating logout view here
def logout_me(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return render(request,'index.html')




#i don't know my tf i added this
@login_required
def addbook(request):
    return redirect(addBook)




#for adding a book
def addBook(request):
    template = "AddBook.html"
    model = BookDetails()
    if request.method == "POST":
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            book = BookDetails()
            owned = OwnedBook()
            username = UserDetails.objects.get(username = request.user.username)
            book.username = username
            book.bookname = request.POST['bookname']
            book.bookdescription= request.POST['bookdescription']
            book.bookauthor = request.POST['bookauthor']
            book.bookimage = request.POST['bookimage']
            book.bookimage0 = request.POST['bookimage0']
            book.bookimage1= request.POST['bookimage1']
            book.bookimage2 = request.POST['bookimage2']
            book.save()
            owned.bookname = book.bookname
            owned.owner = username
            owned.save()
            messages.success(request,"Book added")
            return redirect(profile,username)
    else:
        form = BookForm()
        #messages.success(request, "something wents wrong")
    return render(request,template,{'form':form})






#for showing book and searching book
@login_required
def productshow(request):
    model = BookDetails.objects.order_by('-bookid')
    template = 'products.html'
    form = SearchABook(request.POST)
    if request.method=="POST":
        check1 = request.POST['query']
        if (BookDetails.objects.filter(bookname=check1.upper()).exists()):
            print(check1.upper())
            check12=BookDetails.objects.filter(bookname=check1.upper())
            return render(request,template,{'model':check12,'form':form})
        elif (BookDetails.objects.filter(bookname=check1.lower()).exists()):
            print(check1.lower())
            check12=BookDetails.objects.filter(bookname=check1.lower())
            return render(request,template,{'model':check12,'form':form})
        elif (BookDetails.objects.filter(bookname=check1.capitalize()).exists()):
            print(check1.capitalize())
            check12=BookDetails.objects.filter(bookname=check1.capitalize())
            return render(request,template,{'model':check12,'form':form})
        else:
            return render(request, template, {
                    'model':model,
                    'form': form,
                    'error_message': 'No Book Found. Just take a look on available books or request a book'
                })
    else:
        form =SearchABook()
        return render(request, template,{'model':model,'form':form})
    return render(request, template,{'model':model,'form':form})






#we sometimes need this
@login_required
def gotoprofile(request):
    username = request.user.username
    return redirect(profile,username)





#request for the book
@login_required
def detailsofbook(request,bookid):
    template ="bookmoredetails.html"
    book = bookid
    model = BookDetails.objects.get(bookid = book)
    form = BookAvailableRequest(request.POST)
    if request.method =="POST":
        model2 = BookRequest()
        if model.username != request.user.username:
            model2.requester=request.user.username
            model2.owner = model.username
            model2.bookid = book
            model2.bookname = model.bookname
            model2.makeanoffer = request.POST['reason']
            model2.save()
            return render(request, template, {
                    'form': form,
                    'error_message': 'Request sent to owner.'
                })
        else:
            return render(request, template, {
                    'form': form,
                    'error_message': 'owner can\'t make a request'
                })
    else:
        form = BookAvailableRequest()
    return render(request,'bookmoredetails.html',{'model':model,'form':form})





#requestabook
@login_required
def requestabook(request):
    template = "requestabook.html"
    form = RequestForm(request.POST)
    if request.method =="POST":
        requestername = request.user.username
        wantedBook = RequestedBook()
        wantedBook.requestername = requestername
        wantedBook.askedBookname = request.POST['askedBookname']
        wantedBook.save()
        return render(request, template, {
                'error_message': 'Your request is noted. Once we get your book, we will notify you'
            })
    else:
        form = RequestForm()
    return render(request,template,{'form':form})




@login_required
def deletebook(request,bookid):
    model = BookDetails.objects.get(bookid=bookid)
    model.active_status= False
    model.save()
    return redirect(gotoprofile)

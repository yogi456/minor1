from django.db import models
from working import settings
from django.utils import timezone

# Create your models here.
class UserDetails(models.Model):
    username = models.CharField(max_length =20, unique =True, primary_key=True)
    usermail = models.EmailField(unique =True)
    userfirstname = models.CharField(max_length=10)
    userlastname = models.CharField(max_length=10)
    userpassword = models.CharField(max_length=30)
    userlocation = models.CharField(max_length = 30)
    usercontact = models.IntegerField(unique=True)
    userDoB = models.CharField(max_length=10)
    usergender = models.CharField(max_length=6)
    userKey = models.CharField(max_length=5, blank= True)


    def __str__(self):
        return self.username

class BookDetails(models.Model):
    bookid = models.AutoField(unique = True, primary_key=True)
    username = models.ForeignKey(UserDetails,on_delete=models.CASCADE)
    bookimage = models.ImageField(upload_to ="bookImg/", blank= True)
    bookimage0 = models.ImageField(upload_to ="bookImg/", blank= True)
    bookimage1 = models.ImageField(upload_to ="bookImg/", blank= True)
    bookimage2 = models.ImageField(upload_to ="bookImg/", blank=True)
    bookname = models.CharField(max_length=100)
    bookdescription = models.CharField(max_length= 300)
    bookauthor = models.CharField(max_length= 30, blank=True)
    active_status = models.BooleanField(default=True)
    timeadded = models.DateTimeField(default=timezone.now, blank=True)

    def __str__(self):
        return "BookId:{};UserName:{};BookName:{}".format(self.bookid,self.username,self.bookname)

class BookRequest(models.Model):
    bookid = models.IntegerField()
    bookname = models.CharField(max_length = 100)
    owner = models.CharField(max_length = 20)
    requester = models.CharField(max_length=20)
    makeanoffer = models.CharField(max_length=500, default="please provide me this book")

    def __str__(self):
        return "Book:{};Owner:{};Requester:{};".format(self.bookname,self.owner,self.requester)

class OwnedBook(models.Model):
    bookname= models.CharField(max_length =100)
    owner = models.CharField(max_length=20)

    def __str__(self):
        return "Book:{};Owner:{};".format(self.bookname,self.owner)

class RequestedBook(models.Model):
    askedBookname = models.CharField(max_length=100)
    requestername = models.CharField(max_length = 20)

    def __str__(self):
        return "NeededBook:{};Requester:{};".format(self.askedBookname,self.requestername)

from django.shortcuts import render, HttpResponse, redirect
from home.models import Contact
from django.contrib import messages
from blog.models import Post
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
def home(request):
    return render(request, 'home/home.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        content = request.POST['content']
        if len(name)<1 or len(email)<4 or len(phone)<9 or len(content)<5:
            messages.error(request, 'Please Fill Form Correctly')
        else:
            contact = Contact(name=name, email=email, phone=phone, content=content)
            contact.save()
            messages.success(request, "Your message has been send successfully")
    return render(request, "home/contact.html")

def about(request):
    return render(request, "home/about.html")

def search(request):
    query = request.GET['query']
    if len(query) > 80:
        allPosts = Post.objects.none()
    elif len(query) == 0:
        messages.warning(request, "No result found! Please enter some keywords")
        allPosts = Post.objects.none()
    else:
        allPostsTitle = Post.objects.filter(title__icontains=query)
        allPostsContent = Post.objects.filter(content__icontains=query)
        allPosts = allPostsTitle.union(allPostsContent)

    if allPosts.count() == 0 and len(query) != 0:
        messages.warning(request, "No result found! Please enter some other keywords")
    params = {'allPosts': allPosts}
    return render(request, "home/search.html", params)

def handleSignup(request):
    if request.method == 'POST':
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']
        # Apply Restrictions
         
        if len(username) > 12 :
            messages.warning(request, "user name must be under 12 character!")
            return redirect('home')
        if not username.isalnum():
            messages.warning(request, "user name contains only letters and numbers!")
            return redirect('home')   

        if pass1 != pass2:
            messages.error(request, "paasword does not match!")
            return redirect('home')

        # create user
        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()
        messages.success(request, "Your techsolve account has been successfully created!")
        return redirect('home')
    else:
        request.HttpResponse("404 - Not Found")

def handleLogin(request):
    if request.method == "POST":
        loginusername = request.POST['loginusername']
        loginpassword = request.POST['loginpass']

        user = authenticate(username=loginusername, password=loginpassword)
        if user is not None:
            login(request, user)
            messages.success(request, "Successfully logged in")
            return redirect('home')
        else:
            messages.error(request, "Invalid username or password")
            return redirect('home')
    return HttpResponse("404- Not Found")
def handleLogout(request):
    logout(request)
    messages.success(request, "Successfully logged out")
    return redirect('home')
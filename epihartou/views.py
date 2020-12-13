from django.shortcuts import render



def home(request):
    return render(request, 'epihartou/home.html', {'title':'Ολα για το γραφειο'})



def about(request):
    return render(request, 'epihartou/about.html', {'title':'Ποιοι ειμαστε'})


def cart(request):
    return render(request, 'epihartou/cart.html', {'title':'Το καλαθι'})


def store(request):
    return render(request, 'epihartou/store.html', {'title':'Καταστημα'})



def checkout(request):
    return render(request, 'epihartou/checkout.html', {'title':'ολοκλήρωση παραγγελίας'})


def login(request):
    return render(request, 'epihartou/login.html', {'title':'Σύνδεση'})

def logout(request):
    return render(request, 'epihartou/logout.html', {'title':'Αποσύνδεση'})


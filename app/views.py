from django.shortcuts import render,redirect
from .models import *
import stripe
from datetime import datetime, timedelta

# Create your views here.


def home(request):
    courses = Course.objects.all()
    context = {'courses': courses}
    print(context)
    return render(request, 'home.html' , context)

def view_course(request,slug):
    course = Course.objects.filter(slug =slug).first()
    course_modules = CourseModule.objects.filter(course=course)
    context = {'course':course , 'course_modules':course_modules}
    return render(request, 'course.html' , context)

def become_pro(request):
    if request.method == 'POST':
        membership = request.POST.get('membership' , 'MONTHLY')
        amount = 50
        if membership == 'YEARLY':
            amount = 500
        stripe.api_key = 'pls write here secret api key'

        customer = stripe.Customer.create(
            email =request.user.email,
            source=request.POST['stripeToken']
			)
            
        charge = stripe.Charge.create(
			customer=customer,
			amount=amount*100,
			currency='pln',
			description="Membership",   
		)
        
        print(charge['amount'])
        if charge['paid'] == True:
            profile = Profile.objects.filter(user = request.user).first()
            if charge['amount'] == 50:
                profile.subscription_type = 'M'
                profile.is_pro = True
                expiry = datetime.now() + timedelta(30)
                profile.pro_expiry_date = expiry
                profile.save()
                
            elif charge['amount'] == 500:
                profile.subscription_type = 'Y'
                profile.is_pro = True
                expiry = datetime.now() + timedelta(365)
                profile.pro_expiry_date = expiry
                profile.save()
        
        print(charge)
        return redirect('/charge/')
   
    return render(request, 'become_pro.html')

def charge(request):
    return render(request, 'charge.html')

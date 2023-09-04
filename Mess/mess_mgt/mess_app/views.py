from django.shortcuts import render
from mess_app import models
from mess_app import forms
from mess_app.models import Member,Meal

from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.urls import reverse




def test(request):
    return render(request,'mymess/test.html')




def index(request):
    return render(request, 'mymess/base.html')

def memberlist(request):
    member_list = Member.objects.order_by('name')
    diction = {'title': 'Member List', 'member_list':member_list}
    return render(request, 'mymess/Member_list.html', context=diction)

def memberinfo (request,mem):
    mem_info = Member.objects.get(pk=mem)
    meal_list =Meal.objects.filter(Name=mem).order_by('MealDate')
    # meal_count = Meal.objects.filter(Name=mem).aggregate(('meals'))

    diction = { 'member_info': mem_info , 'meal_list':meal_list }
    return render(request, 'mymess/memberinfo.html', context=diction)



def joinmess(request):
    form = forms.MemberForm()
    diction = {'title': 'Add Member' ,'member_form': form } 

    if request.method =='POST':
        form =forms.MemberForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return memberlist(request)
    return render(request,'mymess/join_mess.html', context=diction)  


def upmember(request,upmem_id):
    mem_info = Member.objects.get(pk=upmem_id)
    form= forms.MemberForm(instance=mem_info)
    diction={}

    if request.method =='POST':
        form =forms.MemberForm(request.POST, instance=mem_info)

        if form.is_valid():
            form.save(commit=True)
            return memberlist(request)
        diction.update({'success_text': 'Successfully Update! '})
        


    diction.update({'upmember': form})
    return render(request, 'mymess/update_mem.html',context=diction)


# AddMeal system :

def mealing1(request):
    form = forms.MealForm()

    if request.method =='POST':
        form =forms.MealForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return memberlist(request)
    diction = {'title ': 'add meal', 'meal_form': form}
    return render(request, 'mymess/Addmeal.html',context=diction)


#edit Meal

def editmeal(request,meal_id):
    meal_info = Meal.objects.get(pk=meal_id)
    form = forms.MealForm(instance=meal_info)
    diction ={}

    if request.method =='POST':
        form=forms.MealForm(request.POST,instance=meal_info)

        if form.is_valid():
            form.save(commit=True)
            diction.update({'success_text':'successfully Update' })

    
    diction.update({ 'upmeal': form})

    

    return render (request, 'mymess/Editmeal.html', context=diction)


def delmeal(request,meal_id):
    meal = Meal.objects.get(pk=meal_id).delete()
    diction={ 'delete_success':' delete Successfully !'}

    return render(request,'mymess/delmeal.html',context=diction)


def delmeam(request,upmem_id):

    member = Member.objects.get(pk=upmem_id).delete()
    diction = {'delete_success':' delete Successfully '}

    return render(request, 'mymess/delmeal.html',context=diction)






def userlogin(request):
    if request.method=='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username = username , password = password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse(index))
            else:
                return HttpResponse('Account is not active.....!')
        else:
            return HttpResponse('Login details are wrong...!')
    else:
        return render(request, 'mymess/login.html', context={})

@login_required 
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse(userlogin))
    

def registrer(request):
    registered = False

    if request.method =='POST':
        user_form = forms.UserForm(data=request.POST)

        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            registered =True


    else:
        user_form = forms.UserForm()

    diction ={'user_form': user_form ,'registered': registered}
    return render(request, 'mymess/reg.html', context=diction)



def test(request):
    return render(request,'mymess/test.html')

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages 
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from .models import Contract 
from .forms import ContractForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout



def signout(request):
    logout(request)
    # Redirect to the desired page after signout
    return redirect('index')  # Replace 'home' with the name of your homepage URL pattern



def index(request):
    return render(request, 'index.html',)





def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        
        # Check if passwords match
        if password1 != password2:
            messages.error(request, "Passwords do not match.")
            return render(request, 'signup.html')
        
        # Check if username is already taken
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username is already taken.")
            return render(request, 'signup.html')
        
        # Create the user
        user = User.objects.create_user(username=username, email=email, password=password1)
        user.save()
        
        # Optionally, you can also log in the user after signup
        login(request, user)
        
        return redirect('/')  # Redirect to dashboard after successful signup
    else:
        return render(request, 'signup.html')


def signin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')  # Redirect to dashboard after successful login
        else:
            # Authentication failed, display error message
            print("you out the wront password ya fuck")
            error_message = "Invalid username or password."
            return render(request, 'signin.html', {'error_message': error_message})
    else:
        return render(request, 'signin.html')




def contracts(request):
    contracts = Contract.objects.all()
    return render(request, 'contracts.html', {'contracts': contracts})           



def add_contract(request):
    if request.method == 'POST':
        form = ContractForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contracts')  # Redirect to contracts page after adding
    else:
        form = ContractForm()
    return render(request, 'add_contract.html', {'form': form})

def get_contracts(request):
    contracts = Contract.objects.all()
    contract_list = [{'contract_name': contract.contract_name} for contract in contracts]
    return JsonResponse({'contracts': contract_list})    

    

def how_it_works(request):
    return render(request, 'how_it_works.html')    


def delete_contract(request, contract_id):
    # Retrieve the contract object
    contract = Contract.objects.get(pk=contract_id)
    # Delete the contract
    contract.delete()
    # Redirect back to contracts page or any other page
    return redirect('contracts')    
# from django.shortcuts import render, redirect, get_object_or_404
# from django.contrib.auth.decorators import login_required
# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth import login
# from django.contrib import messages
# from .models import Destination, Booking

# def home(request):
#     # Fetch all destinations from the database
#     all_destinations = Destination.objects.all()
#     return render(request, 'index.html', {'destinations': all_destinations})

# def signup(request):
#     if request.method == "POST":
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             login(request, user)
#             messages.success(request, "Registration successful! Welcome to Kerala.")
#             return redirect('home')
#     else:
#         form = UserCreationForm()
#     return render(request, 'registration/signup.html', {'form': form})

# @login_required
# def book(request, dest_id):
#     destination = get_object_or_404(Destination, id=dest_id)
    
#     if request.method == "POST":
#         full_name = request.POST.get('name')
#         email = request.POST.get('email')
#         date = request.POST.get('date')
#         e = request.POST.get('email')
#         Booking.objects.create(
#             user=request.user,
#             destination=destination,
#             full_name=full_name,
#             email=email,
#             travel_date=date
#         )
#         messages.success(request, f"Booking confirmed for {destination.name}!")
#         return redirect('home')

#     return render(request, 'booking.html', {'destination': destination})



from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib import messages
from .models import Destination, Booking

def home(request):
    all_destinations = Destination.objects.all()
    return render(request, 'index.html', {'destinations': all_destinations})

def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        # Capture the manual email input from the template
        email = request.POST.get('email') 
        
        if form.is_valid():
            user = form.save(commit=False) # Create user but don't save to DB yet
            user.email = email             # Manually assign the email
            user.save()                    # Now save to DB
            login(request, user)
            messages.success(request, "Registration successful! Welcome to Kerala.")
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})

@login_required
def book(request, dest_id):
    destination = get_object_or_404(Destination, id=dest_id)
    
    if request.method == "POST":
        full_name = request.POST.get('name')
        email = request.POST.get('email')
        date = request.POST.get('date')
        
        if not date:
            messages.error(request, "Please select a travel date.")
            return render(request, 'booking.html', {'destination': destination})

        Booking.objects.create(
            user=request.user,
            destination=destination,
            full_name=full_name,
            email=email,
            travel_date=date
        )
        messages.success(request, f"Booking confirmed for {destination.name}!")
        return redirect('home')

    return render(request, 'booking.html', {'destination': destination})
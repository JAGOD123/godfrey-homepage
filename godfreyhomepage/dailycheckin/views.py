from django.shortcuts import render, redirect, get_object_or_404
from .forms import CheckInForm
from .models import CheckIn

# Create your views here.
def check_in(request):
    if request.method == 'POST':
        form = CheckInForm(request.POST)
        if form.is_valid():
            # return redirect('dailycheckin/checkin:<slug:date_slug>') # TODO: This needs to be changed to a list of the check ins
            checkin_instance = form.save()  
            date_slug = checkin_instance.datetime.strftime('%Y-%m-%d')
            print(f"Redirecting to check-in detail for date_slug: {date_slug}")
            return redirect('dailycheckin:checkin_detail', date_slug=date_slug)  # Redirect to the detail page
    
    else:
        form = CheckInForm()

    return render(request, 'dailycheckin/checkin_form.html', {'form': form})

def checkin_details(request, date_slug):
    checkin = get_object_or_404(CheckIn, datetime__date=date_slug)
    return render(request, 'dailycheckin/checkin_detail.html', {'checkin': checkin})

def checkin_list(request):
    checkins = CheckIn.objects.all().order_by('-datetime')
    return render(request, 'dailycheckin/checkin_list.html', {'checkins': checkins})
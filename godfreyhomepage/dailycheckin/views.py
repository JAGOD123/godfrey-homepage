from django.shortcuts import render, redirect
from .forms import CheckInForm

# Create your views here.
def check_in(request):
    if request.method == 'POST':
        form = CheckInForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('posts:list') # TODO: This needs to be changed to a list of the check ins
    else:
        form = CheckInForm()

    return render(request, 'dailycheckin/checkin_form.html', {'form': form})
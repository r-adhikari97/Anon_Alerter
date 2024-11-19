from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import ComplaintForm
from .models import PublicComplaint

# Create your views here.
@login_required
def create_complaint(request):
    """ Handle creating a public complaint """

    if request.method == 'POST':
        form = ComplaintForm(request.POST, request.FILES)

        if form.is_valid():
            # Save the complaint and user
            complaint = form.save(commit=False)
            complaint.complaint_user = request.user
            complaint.save()

            return redirect('complaint-dashboard')

    else:
        form = ComplaintForm()

    context = {'form': form}
    return render(request, 'complaints/create_complaint.html', context)


@login_required
def view_complaint_dashboard(request):
    complaints = PublicComplaint.objects.all()
    context = {"complaints":complaints}
    return render(request, "complaints/complaint_dashboard.html",context)


from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import ComplaintForm
from .models import PublicComplaint

# Create your views here.

################# USERS #########################
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


@login_required
def view_single_complaint(request, pk):
    complaint = PublicComplaint.objects.get(pk=pk)
    context = {"complaint":complaint}
    return render(request, "complaints/single_complaint.html", context)


################# SPECIAL OFFICIAL  #########################
@login_required
def view_official_complaint_dashboard(request):
    complaints = PublicComplaint.objects.all()
    context = {"complaints":complaints}
    return render(request, "complaints/official_complaint_dashboard.html",context)


@login_required
def update_official_complaint(request, pk):
    complaint = PublicComplaint.objects.get(pk=pk)

    if request.method == "GET":
        complaint.complaint_status = not complaint.complaint_status
        complaint.save()
        return redirect("view_official_dashboard")

    context = {"complaint":complaint}
    return render(request, "complaints/official_complaint_dashboard.html",context)
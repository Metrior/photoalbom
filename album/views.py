from django.shortcuts import render, redirect
from .forms import UploadFileForm


# Create your views here.
def Upload(request):
    if request.method=='POST':
        form=UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('upload')
    else:
        form=UploadFileForm()
    return render(request, 'upload.html', {'form':form})
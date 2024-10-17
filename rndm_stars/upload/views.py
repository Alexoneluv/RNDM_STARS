from django.shortcuts import render, redirect
from .forms import UploadFileForm

def upload_nature(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')  # Перенаправление на главную страницу после успешной загрузки
    else:
        form = UploadFileForm()
    return render(request, 'upload/upload_nature.html', {'form': form})
from django.shortcuts import render, redirect
from .forms import GeeksForm
from .tasks import convert_image_extension  # Import the Celery task

def index(request):
    context = {}
    if request.method == 'POST':
        form = GeeksForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save()  # Save the form and get the Image object
            convert_image_extension.delay(image.id)  # Dispatch the Celery task asynchronously
            return redirect('success')  # Redirect to the success page
    else:
        form = GeeksForm()

    context['form'] = form
    return render(request, 'upload/index.html', context)

def success(request):
    return render(request, 'upload/success.html')


# handle the download request

from django.http import HttpResponse
from .models import Images

def download_image_view(request, image_id):
    # Retrieve the Image object
    try:
        image = Images.objects.get(id=image_id)
    except Images.DoesNotExist:
        # Handle the case where the image does not exist
        return HttpResponse('Image not found.')

    # Perform the image conversion and provide the download link logic here
    # ...

    # Return a download response to the user
    response = HttpResponse(content_type='application/octet-stream')
    response['Content-Disposition'] = 'attachment; filename="converted_image.jpg"'  # Set the desired filename
    # Set the appropriate content and file path based on your conversion logic
    response['X-Sendfile'] = '/path/to/converted_image.jpg'  # Replace with the actual file path
    return response

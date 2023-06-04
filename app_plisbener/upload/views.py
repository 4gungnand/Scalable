from django.shortcuts import render, redirect
from .forms import GeeksForm
from .models import photos
from urllib.parse import urljoin
from django.conf import settings
import cloudinary
import requests

def index(request):
    context = {}

    if request.method == 'POST':
        form = GeeksForm(request.POST, request.FILES)
        if form.is_valid():
            title = form.cleaned_data['title']
            image = form.cleaned_data['image']

            # Save the file with the desired title
            uploaded_image = cloudinary.uploader.upload(
                image,
                public_id=title,  # Set the public ID to the title
                folder='scalable/'  # Optional: Set a folder to organize the images
            )

            # Handle the Cloudinary response and redirect to the success page
            if 'public_id' in uploaded_image:
                return redirect('success')  # Replace 'success' with your success page URL

    else:
        form = GeeksForm()

    context['form'] = form
    return render(request, 'index.html', context)

def success(request):
    context = {}
    url = get_newest_image()
    img_name = url.split('/')[-1]
    context['img_url'] = url
    context['img_name'] = img_name
    # context['img_url'] = new_url

    return render(request, 'success.html', context)


def get_newest_image():
    cloudinary.config()

    # Get the Cloudinary credentials from the configuration
    cloud_name = cloudinary.config().cloud_name
    api_key = cloudinary.config().api_key
    api_secret = cloudinary.config().api_secret

    # API endpoint
    url = f'https://api.cloudinary.com/v1_1/{cloud_name}/resources/image/upload'

    # Request parameters
    params = {
        'type': 'upload',
        'max_results': 1,  # Number of images to retrieve
        'sort_by': 'created_at',  # Sort by creation date
        'direction': 'desc',  # Sort in descending order
    }

    # Make the API request
    response = requests.get(url, auth=(api_key, api_secret), params=params)
    
    # Check if the request was successful
    if response.status_code == 200:
        data = response.json()
        
        # Extract the public ID of the newest image 
        if 'resources' in data and len(data['resources']) > 0:
            newest_image_public_id = data['resources'][0]['public_id']
            
            # Construct the URL of the newest image
            newest_image_url = f'https://res.cloudinary.com/{cloud_name}/image/upload/{newest_image_public_id}'
            
            return newest_image_url
    
    # Return None if the request fails or no images are found
    return None

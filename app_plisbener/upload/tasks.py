from celery import shared_task
from django.core.files import File
from .models import Images

@shared_task

def convert_image_extension(image_id):
    # Retrieve the Image object from the database
    image = Images.objects.get(id=image_id)

    # Get the file extension of the original image
    original_extension = image.img.name.split('.')[-1]

    # Rename the image file with the new extension
    new_file_name = f"{image.img.name.split('.')[0]}.png"

    # Open the image file
    with image.img.open('rb') as file:
        # Create a new File object with the updated file name
        converted_image = File(file, name=new_file_name)

        # Save the new File object to the database
        image.img.save(new_file_name, converted_image, save=True)

    return "Image extension converted and saved successfully."

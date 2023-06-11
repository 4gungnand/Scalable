from celery import shared_task
import cloudinary

@shared_task
def process_uploaded_file(title_input, image_input):
    # Task logic to process the uploaded file asynchronously
    # Save the file with the desired title
    uploaded_image = cloudinary.uploader.upload(
        image_input,
        public_id=title_input,  # Set the public ID to the title
        folder='scalable/'  # Optional: Set a folder to organize the images
    )
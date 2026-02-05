from django.core.exceptions import ValidationError

def validate_image_size(value):
    filesize= value.size
    
    if filesize > 2097152:
        raise ValidationError("The maximum image size that can be uploaded is 2MB")
    else:
        return value

def validate_file_size(value):
    filesize= value.size
    
    if filesize > 4194304:
        raise ValidationError("The maximum file size that can be uploaded is 4MB")
    else:
        return value
        

def upload_project_img(instance,filename):
    id = instance.id
    location = f"product/{id}/"
    return location + filename
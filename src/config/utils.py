def upload_to_classname(instance, filename):
    return f"{instance._meta.model_name}/{filename}"

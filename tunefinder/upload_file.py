from os.path import join


def handle_uploaded_file(f, name):
    with open(join('media', name), 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

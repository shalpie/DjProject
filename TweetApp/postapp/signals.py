import django.dispatch

new_post = django.dispatch.Signal(providing_args=["sig_post"])
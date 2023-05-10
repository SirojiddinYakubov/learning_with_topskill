from django.contrib import messages
from django.shortcuts import render

from product.forms import ContactForm


def products_list(request):
    return render(request, 'products_list.html')


def products_detail(request, product_id):
    return render(request, 'product_detail.html')


def about(request):
    if request.method == 'POST':
        form = ContactForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            # return redirect('success')
            messages.success(request, 'Form submission successful')

    form = ContactForm()
    return render(request, 'about.html', {'form': form})

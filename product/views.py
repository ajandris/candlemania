from django.shortcuts import render


"""
Product functions
"""
def product_index(request):
    return render(request, 'product/product-home.html')

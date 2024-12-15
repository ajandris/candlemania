from django.shortcuts import render


"""
Product functions
"""
def product_index(request):
    context = {
        "active_menu": "product"
    }
    return render(request, 'product/product-home.html', context=context)

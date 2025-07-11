from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages

from .models import Product

# Vista 1 ─────────────────────────────────────────────

def product_list(request):
    # Solo mostramos hasta 4 productos disponibles.
    products = Product.objects.all()[:4]
    return render(request, 'store/product_list.html', {
        'products': products,
    })

# Vista 2 ─────────────────────────────────────────────


def purchase_product(request, pk):
    product = get_object_or_404(Product, pk=pk)

    if request.method == 'POST':
        product.delete()  # Elimina el producto definitivamente
        messages.success(request, f'Compraste «{product.name}». ¡Gracias por tu compra!')
        return redirect('product_list')

    return render(request, 'store/purchase.html', {
        'product': product,
    })
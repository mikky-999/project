from django.shortcuts import render, redirect
from .forms import SignUpForm, UserUpdateForm, ProfileUpdateForm, OrderForm
from users.models import Profile, Order
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('login')
    else:
        form = SignUpForm()
    
    context = {
        'form': form,
        'title': 'Sign Up or Login'
    }
    return render(request, 'users/signup.html', context)


@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, 
                                   instance=request.user.profile)
        
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, "Your account has been updated")
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
    context = {
        'title': 'Profile',
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request, 'users/profile.html', context)


# def cart(request):
#     context = {
#         'title': 'Cart'
#     }
#     return render(request, 'users/cart.html', context)


# @csrf_exempt
# def add_to_order(request):
#     if request.method == 'POST':
#         try:
#             data = request.json()
#             order_items = data.get('order_items', [])

#             # Loop through the order items and save them to the Order model
#             for item in order_items:
#                 new_order = Order.objects.create(
#                     item_name=item['item_name'],
#                     quantity=item['quantity'],
#                     price=item['price']
#                 )
#                 new_order.save()

#             return JsonResponse({'message': 'Order added successfully'})
#         except Exception as e:
#             return JsonResponse({'error': str(e)}, status=400)
#     return JsonResponse({'error': 'Invalid request method'}, status=405)
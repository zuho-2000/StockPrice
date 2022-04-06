from django.shortcuts import render
from django.utils import timezone
from .models import Item
from .models import Shop
from .models import Price
from django.shortcuts import render, get_object_or_404
from .forms import ItemForm
from .forms import ShopForm
from .forms import PriceForm
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.db.models import Min
from django.db.models import Count

# Create your views here.

def home(request):
    Prices = Item.objects.annotate(Min('price__price'))
    return render(request, 'blog/home.html', {'Prices':Prices})

def post_detail(request, pk):
    price = get_object_or_404(Price, pk=pk)
    return render(request, 'blog/post_detail.html', {'price': price})

@login_required
def post_new(request):
    if request.method == "POST":
        form = PriceForm(request.POST)
        if form.is_valid():
            price = form.save(commit=False)
            price.save()
            return redirect('post_detail', pk=price.pk)
    else:
        form = PriceForm()
    return render(request, 'blog/post_edit.html', {'form': form})

@login_required
def post_edit(request, pk):
    price = get_object_or_404(Price, pk=pk)
    if request.method == "POST":
        form = PriceForm(request.POST, instance=Price)
        if form.is_valid():
            price = form.save(commit=False)
            price.save()
            return redirect('post_detail', pk=price.pk)
    else:
        form = PriceForm(instance=price)
    return render(request, 'blog/post_edit.html', {'form': form})

@login_required
def post_draft_list(request):
    posts = Price.objects.filter(published_date__isnull=True).order_by('created_date')
    return render(request, 'blog/post_draft_list.html', {'posts': posts})

@login_required
def post_publish(request, pk):
    post = get_object_or_404(Price, pk=pk)
    post.publish()
    return redirect('post_detail', pk=pk)

@login_required
def publish(self):
    self.published_date = timezone.now()
    self.save()

@login_required
def post_remove(request, pk):
    post = get_object_or_404(Price, pk=pk)
    post.delete()
    return redirect('post_list')
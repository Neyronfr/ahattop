from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout
from .form import NewsForm,SearchForm
from .models import NewsModel, NewModel, TagModel
from django.urls import reverse_lazy
from django.views.generic import DetailView, CreateView, DeleteView, UpdateView, ListView


class HomePage(ListView):
    form_class = NewsForm,SearchForm
    template_name = 'tech-index.html'
    model = NewsModel
    paginate_by = 3

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = NewModel.objects.all()
        context["articles"] = NewsModel.objects.all()
        return context



def search_results(request):
    if request.method == 'POST':
        get_article = request.POST.get('search_article')
        try:
            exact_article = NewsModel.objects.get(article_title__icontains=get_article)
            return redirect(f'articles/{exact_article.id}')
        except:
            return redirect('/')


def article_page(request, pk):
    article = NewsModel.objects.get(id=pk)
    context = {'article': article}
    return render(request, 'article.html', context)


def category_page(request, pk):
    category = NewModel.objects.get(id=pk)
    current_articles = NewsModel.objects.filter(article_categories=category)
    context = {'article': current_articles}
    return render(request, 'category.html', context)


class NewsDetailView(DetailView):
    model = NewsModel
    template_name = 'article.html'
    context_object_name = 'article'


class NewsCreateView(CreateView):
    model = NewsModel
    form_class = NewsForm
    template_name = 'create.html'
    success_url = reverse_lazy('home')


class NewsUpdateView(UpdateView):
    model = NewsModel
    form_class = NewsForm
    template_name = 'edit.html'
    success_url = reverse_lazy('home')


class NewsDeleteView(DeleteView):
    model = NewsModel
    template_name = 'delete.html'
    success_url = reverse_lazy('home')


class MyLoginView(LoginView):
    template_name = 'login.html'
    redirect_authenticated_user = True

    def get_success_url(self):
        return '/'


def logout_view(request):
    logout(request)
    return redirect('home')


def contact_us(request):
    template_name = 'contact.html'
    return render(request, template_name='contact.html')



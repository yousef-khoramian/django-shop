from django.http import HttpRequest
from django.shortcuts import render
from django.views.generic import ListView, DetailView

from article_module.models import Article, ArticleComment


# Create your views here.


class ArticleListView(ListView):
    template_name = 'article_module/article_list_page.html'
    model = Article
    ordering = '-id'
    paginate_by = 3

    def get_queryset(self):
        query = super().get_queryset()
        query = query.filter(is_active=True)
        search = self.request.GET.get('search')
        if search:
            query = query.filter(title__icontains=search)
        return query

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        page_obj = context.get('page_obj')
        paginator = context.get('paginator')
        current = page_obj.number
        total = paginator.num_pages
        start = max(1, current - 4)
        end = min(total, current + 5)
        if total > 10:
            if current < 6:
                custom_range = range(1, 11)
            else:
                custom_range = range(start, end + 1)
        else:
            custom_range = range(1, total + 1)
        context['custom_range'] = custom_range
        return context


class ArticleDetailView(DetailView):
    template_name = 'article_module/article_detail_page.html'
    model = Article

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = ArticleComment.objects.filter(article_id=self.object.id, parent=None)
        context['count'] = ArticleComment.objects.filter(article_id=self.object.id).count()
        return context


def article_comments(request: HttpRequest):
    article_id = request.GET.get('article_id')
    message = request.GET.get('message')
    parent_id = request.GET.get('parent_id')
    new_comment = ArticleComment(user_id=request.user.id, article_id=article_id, parent_id=parent_id, message=message)
    new_comment.save()
    context = {
        'comments': ArticleComment.objects.filter(article_id=article_id, parent=None),
        'count': ArticleComment.objects.filter(article_id=article_id).count()
    }
    return render(request, 'article_module/article_comment_componenet.html', context)

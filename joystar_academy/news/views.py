from django.shortcuts import get_object_or_404, render

from .models import NewsCategory, NewsPost


def news_list(request):
    category_slug = request.GET.get("category", "")
    posts = NewsPost.objects.filter(is_published=True).select_related("category")
    if category_slug:
        posts = posts.filter(category__slug=category_slug)

    context = {
        "meta_description": "Latest news and updates from Carol & Kelly Joystar Academy.",
        "posts": posts,
        "categories": NewsCategory.objects.all(),
        "active_category": category_slug,
    }
    return render(request, "news/list.html", context)


def news_detail(request, slug):
    post = get_object_or_404(NewsPost, slug=slug, is_published=True)
    related = NewsPost.objects.filter(is_published=True).exclude(pk=post.pk)[:3]
    context = {
        "post": post,
        "related": related,
        "meta_description": post.excerpt,
    }
    return render(request, "news/detail.html", context)
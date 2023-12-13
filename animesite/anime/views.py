from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from .models import Anime, Producer, AnimeTag, Genre, Years, Author, Studio


menu = [
    # {'title': 'Главная страница', 'url_name': 'index'},
    {'title': 'Каталог аниме', 'url_name': 'all_anime'},
    {'title': 'Аниме по годам', 'url_name': 'anime_years'},
    {'title': 'Аниме по жанрам', 'url_name': 'anime_genre'},
    {'title': 'Студии', 'url_name': 'anime_studio'},
]

def index(request):
    anime_all = Anime.objects.all()

    data = {
        'title': 'Главная страница',
        'anime_all': anime_all,
        'menu': menu,
    }
    return render(request, 'anime/index.html', context=data)


def show_all_anime(request):
    anime = Anime.objects.all().order_by('name_ru')
    data = {
        'menu': menu,
        'anime': anime,
    }

    return render(request, 'anime/show_all_anime.html', context=data)

def show_anime_page(request, anime_slug):
    anime_obj = get_object_or_404(Anime, slug=anime_slug)
    genre = Genre.objects.filter(genre__slug=anime_obj.slug)
    producer = Producer.objects.filter(producer__slug=anime_slug)
    tag = AnimeTag.objects.filter(tags__slug=anime_slug)

    data = {
        'title': anime_obj.name_ru,
        'anime_obj': anime_obj,
        'genre': genre,
        'producer': producer,
        'tag': tag,
        'menu': menu,
    }
    return render(request, 'anime/anime_page.html', context=data)

def anime_genre(request):
    genre = Genre.objects.all().order_by('name')

    data = {
        'title': f'Жанры',
        'genre': genre,
        'menu': menu,
    }
    return render(request, 'anime/anime_genre.html', context=data)

def show_genre_page(request, genre_slug):
    genre_obj = get_object_or_404(Genre, genre_slug=genre_slug)
    animies = Anime.objects.filter(genre=genre_obj)

    data = {
        'title': f'Жанр: {genre_obj.name}',
        'genre_obj': genre_obj,
        'animies': animies,
        'menu': menu,
    }
    return render(request, 'anime/genre_page.html', context=data)

def anime_years(request):
    years = Years.objects.all().order_by('years')

    data = {
        'title': f'Все года',
        'years': years,
        'menu': menu,
    }
    return render(request, 'anime/year_page.html', context=data)

def show_year_page(request, year):
    year_obj = get_object_or_404(Years, years=year)
    animies = Anime.objects.filter(year=year_obj)

    data = {
        'title': f'Все аниме за {year_obj.years} г.',
        'year_obj': year_obj,
        'animies': animies,
        'menu': menu,
    }
    return render(request, 'anime/anime_year_page.html', context=data)

def show_producer_page(request, producer_slug):
    producer_obj = get_object_or_404(Producer, producer_slug=producer_slug)
    animies = Anime.objects.filter(producer=producer_obj)

    data = {
        'title': producer_obj.name,
        'producer_obj': producer_obj,
        'animies': animies,
        'menu': menu,
    }
    return render(request, 'anime/producer_page.html', context=data)

def show_author_page(request, author_slug):
    author_obj = get_object_or_404(Author, author_slug=author_slug)
    animies = Anime.objects.filter(author=author_obj)

    data = {
        'title': author_obj.name,
        'producer_obj': author_obj,
        'animies': animies,
        'menu': menu,
    }
    return render(request, 'anime/author_page.html', context=data)

def show_tag_page(request, tag_slug):
    tag_obj = get_object_or_404(AnimeTag, tag_slug=tag_slug)
    animies = Anime.objects.filter(tag=tag_obj)

    data = {
        'title': tag_obj.tag,
        'tag_obj': tag_obj,
        'animies': animies,
        'menu': menu,
    }
    return render(request, 'anime/tag_page.html', context=data)

def anime_studio(request):
    studio = Studio.objects.all().order_by('name')

    data = {
        'title': 'Студии',
        'studio': studio,
        'menu': menu,
    }
    return render(request, 'anime/anime_studio.html', context=data)

def show_studio_page(request, studio_slug):
    studio_obj = get_object_or_404(Studio, studio_slug=studio_slug)
    animies = Anime.objects.filter(studio=studio_obj)

    data = {
        'title': studio_obj.name,
        'tag_obj': studio_obj,
        'animies': animies,
        'menu': menu,
    }
    return render(request, 'anime/studio_page.html', context=data)
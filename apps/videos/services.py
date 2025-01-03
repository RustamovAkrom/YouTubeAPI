from datetime import timedelta

from django.db.models import Count, Q, F, ExpressionWrapper, FloatField
from django.utils.timezone import now
from apps.videos.models import WatchHistory, Video


def get_recomendations(user):
    """
    Возвращает 10 рекомендованных видео для пользователя.
    Учитываются лайки, просмотры, категория и теги.
    """

    liked_videos = Video.objects.filter(video_likes__user=user)
    liked_categories = liked_videos.values_list('category', flat=True).distinct()
    liked_tags = liked_videos.values_list('tag__id', flat=True).distinct()

    recent_bonus = 1.5
    recent_threshold = now() - timedelta(days=30) # Новое видео = последние 30 дней

    recomended_videos = Video.objects.filter(
        Q(category__in=liked_categories) | Q(tag__id__in=liked_tags)
    ).exclude(
        video_likes__user=user
    ).annotate(
        is_recent=ExpressionWrapper(
            Q(created_at__gte=recent_threshold),
            output_field=FloatField()
        ),
        like_score=Count('video_likes') * 2.0,
        view_score=F('views_count') * 0.5,
        total_score=ExpressionWrapper(
            F('like_score') + F('view_score') + (F('is_recent') * recent_bonus),
            output_field=FloatField()
        )
    ).order_by('-total_score')[:10]

    return recomended_videos


def get_recomendations_from_history(user):
    """
    Рекомендации на основе истории просмотров.
    """
    watched_videos = Video.objects.filter(watch_histories__user=user)
    watched_categories = watched_videos.values_list('category', flat=True).distinct()
    watched_tags = watched_videos.values_list('tag__id', flat=True).distinct()

    recommended_videos = Video.objects.filter(
        Q(category__in=watched_categories) | Q(tag__id__in=watched_tags)
    ).exclude(
        watch_histories__user=user
    ).annotate(
        like_score=Count('video_likes') * 1.5,
        view_score=F('views_count') * 0.5,
    ).order_by('-like_score', '-view_score')[:10]

    return recommended_videos


def get_recomendations_with_dislikes(user):
    """
    Рекомендации с учетом лайков и дизлайков.
    """
    liked_videos = Video.objects.filter(video_likes__user=user)
    disliked_videos = Video.objects.filter(video_dislikes__user=user)

    liked_categories = liked_videos.values_list('category', flat=True).distinct()
    liked_tags = liked_videos.values_list('tag__id', flat=True).distinct()

    disliked_categories = disliked_videos.values_list('category', flat=True).distinct()
    disliked_tags = disliked_videos.values_list('tag__id', flat=True).distinct()

    # Дизлайки уменьшают вес видео в этих категориях или с этими тегами
    recomended_videos = Video.objects.filter(
        Q(category__in=liked_categories) | Q(tag__id__in=liked_tags)
    ).exclude(
        video_likes__user=user # Исключаем уже понравившиеся видео
    ).exclude(
        Q(category__in=disliked_categories) | Q(tag__id__in=disliked_tags) # Исключаем категории/теги, которые не понравились
    ).annotate(
        like_score=Count('video_likes') * 2.0,
        dislike_score=Count('video_dislikes') * -1.5, # Дизлайки уменьшают рейтинг
        view_score=F('views_count') * 0.5,
        total_score=ExpressionWrapper(
            F('like_score') + F('view_score') + F('dislike_score'),
            output_field=FloatField()
        )
    ).order_by('-total_score')[:10]

    return recomended_videos


def get_recomendations_with_dislike_exclusion(user):
    """
    Рекомендации с учетом общего количества дизлайков.
    """
    
    disliked_videos = Video.objects.annotate(
        dislike_count=Count('video_dislikes')
    ).filter(dislike_count__lt=10)

    liked_videos = Video.objects.filter(video_likes__user=user)
    liked_categories = liked_videos.values_list("category", flat=True).distinct()
    liked_tags = liked_videos.values_list("tag__id", flat=True).distinct()

    recommended_videos = disliked_videos.filter(
        Q(category__in=liked_categories) | Q(tag__id__in=liked_tags)
    ).exclude(
        video_likes__user=user
    ).annotate(
        like_score=Count('video_likes') * 2.0,
        view_score=F('views_count') * 0.5,
    ).order_by('-like_score', 'view_score')[:10]

    return recommended_videos

# def get_recomendations(user):

#     """
#     Возвращает 10 рекомендованных видео для пользователя.
#     Учитываются лайки, просмотры, категория и теги.
#     """

#     # Получаем видео, которые пользователь лайкнул
#     liked_videos = Video.objects.filter(video_likes__user=user)
    
#     # Выделяем категории и теги понравившихся видео
#     liked_categories = liked_videos.values_list('category', flat=True).distinct()
#     liked_tags = liked_videos.values_list('tag__id', flat=True).distinct()

#     # Ищем видео с похожими категориями и тегами
#     recomended_videos = Video.objects.filter(
#         Q(category__in=liked_categories) | Q(tag__id__in=liked_tags)
#     ).exclude(
#         video_likes__user=user # Исключаем видео, которые пользователь уже лайкнул
#     ).annotate(
#         like_count=Count('video_likes')
#     ).order_by('-views_count', '-like_count')[:10] # Сортируем по просмотрам и лайкам

#     return recomended_videos

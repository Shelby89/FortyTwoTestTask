# -*- coding: utf-8 -*-
# Цель — показать взаимодействие двух хуков
from django.db import connection
from django.conf import settings
import datetime

class StatisticsMiddleware:

    def process_request(self, request):
        # вызывается в самом начале
        if request.method == 'GET' and not\
            request.is_ajax() and\
                'html' in request.META['HTTP_ACCEPT']:
            # Если проверка выполняется, то фиксируем время 
            #старта в новом атрибуте.
            request.start =  datetime.datetime.now()

    def process_response(self, request, response):
        # Вызывается в самом конце.
        # Если нужного нам атрибута нет или мы не в режиме отладки,
        # то сразу возвращаем запрос
        if not hasattr(request, 'start') or not settings.DEBUG or not\
                hasattr(response, 'rendered_content'):
            return response

        # Выяснили затраченное время
        total_time = (time() - request.start) * 1000

        # Определяем количество запросов в БД
        # Нас интересуют ВСЕ сделанные запросы
        query_len = len(connection.queries)

        # Если больше 0
        if query_len:
            # Перебираем список словарей, нас интересует только время.
            db_queries = connection.queries
            db_time = sum([(float(q['time']) * 1000) for q in db_queries])
        else:
            db_time = 0.0

        # Получаем время работы интерпретатора
        python_time = total_time - db_time

        stats = {
            'total_time': total_time,
            'python_time': python_time,
            'db_time': db_time,
            'db_queries': query_len,
        }
        
        # Подготавливаем html-код — помещаем туда наши данные.
        stat_str = '<body>'
        stat_str += ', '.join('{0} = {1:.2f}'.format(k, v)
                              for (k, v) in stats.items())

        content = response.rendered_content
        # Производим замену в сформированном содержимом 
        # и помещаем результат в конечное содержимое, 
        # которые мы вернем вместе с ответом
        response.content = content.replace('<body>', stat_str)

        return response
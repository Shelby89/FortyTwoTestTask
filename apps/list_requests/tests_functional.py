# -*- encoding: utf-8 -*-
from django.test import TestCase
from django.core.urlresolvers import reverse


class TicketTests(TestCase):
    def test_general(self):
        '''
        Общий функциональный тест
        '''
        # Пользователь заходит на главную страницу
        response = self.client.get(reverse('hello:index'))
        self.assertEqual(response.status_code, 200)
        # и видит ссылку на страницу requests
        self.assertContains(response, "<a href='/requests/'>requests")

        # Он нажимает на ссылку и видит страницу с запросами

        response = self.client.get(reverse('list_requests:requests'))
        self.assertEqual(response.status_code, 200)
        # Так как он еще не генерировал запросы, то он видит сообщение
        # о том, что в базе нет запросов
        self.assertContains(response, "There is no requests")

        # Страница обновляется автоматически так как появляются новые запросы
        # При этом обновляется заголовок страницы.
        # В заголовке страницы должно отображаться общее количество запросов
        # в формате (N).
        # Пользователь снова зайдет на страницу с запросами, то список запросов
        # начнет отображать уже новые запросы.

# -*- encoding: utf-8 -*-
import datetime

from django.utils import timezone
from django.test import TestCase
from django.core.urlresolvers import resolve, reverse

from list_requests.models import StoredRequests

def create_test_data(quantity):
    """
    Наполнение базы тестовыми данными
    """
    StoredRequests.objects.bulk_create([
        StoredRequests(method='GET1', path_info='/requests/', server_protocol='HTTP/1.1', server_port='8080', remote_address='10.240.208.91'),
        StoredRequests(method='GET2', path_info='/requests/', server_protocol='HTTP/1.1', server_port='8080', remote_address='10.240.208.91'),
        StoredRequests(method='GET3', path_info='/requests/', server_protocol='HTTP/1.1', server_port='8080', remote_address='10.240.208.91'),
        StoredRequests(method='GET4', path_info='/requests/', server_protocol='HTTP/1.1', server_port='8080', remote_address='10.240.208.91'),
        StoredRequests(method='GET5', path_info='/requests/', server_protocol='HTTP/1.1', server_port='8080', remote_address='10.240.208.91'),
        StoredRequests(method='GET6', path_info='/requests/', server_protocol='HTTP/1.1', server_port='8080', remote_address='10.240.208.91'),
        StoredRequests(method='GET7', path_info='/requests/', server_protocol='HTTP/1.1', server_port='8080', remote_address='10.240.208.91'),
        StoredRequests(method='GET8', path_info='/requests/', server_protocol='HTTP/1.1', server_port='8080', remote_address='10.240.208.91'),
        StoredRequests(method='GET9', path_info='/requests/', server_protocol='HTTP/1.1', server_port='8080', remote_address='10.240.208.91'),
        StoredRequests(method='GET10', path_info='/requests/', server_protocol='HTTP/1.1', server_port='8080', remote_address='10.240.208.91'),
        StoredRequests(method='GET11', path_info='/requests/', server_protocol='HTTP/1.1', server_port='8080', remote_address='10.240.208.91'),
        ])
    return None

class TicketTests(TestCase):
	def test_general(self):
		# Пользователь заходит на главную страницу
		response = self.client.get(reverse('hello:index'))
		self.assertEqual(response.status_code, 200)
		# и видит ссылку на страницу requests
		self.assertContains(response, "<a href='/requests/'>requests")
		
		# Он нажимает на ссылку и видит страницу с запросами (макс. 10 последних запроса),
		
		selected_requests = StoredRequests.objects.reverse()[:10]
		response = self.client.get(reverse('list_requests:requests'))
		self.assertEqual(response.status_code, 200)
		# Так как он еще не генерировал запросы, то он видит сообщение
		# о том, что в базе нет запросов
		self.assertEqual(response, "There is no requests")
		
		# Страница обновляется автоматически так как появляются новые запросы
		# При этом обновляется заголовок страницы.
		# В заголовке страницы должно отображаться общее количество запросов 
		# в формате (N).
		# Пользователь снова зайдет на страницу с запросами, то список запросов 
		# начнет отображать уже новые запросы.
# -*- encoding: utf-8 -*-
import datetime

from django.utils import timezone
from django.test import TestCase
from django.core.urlresolvers import resolve, reverse

from list_requests.models import StoredRequests

def create_test_data(quantity):
    """
    Creates a poll with the given `question` published the given number of
    `days` offset to now (negative for polls published in the past,
    positive for polls that have yet to be published).
    """
    # return [StoredRequests.objects.create(
    #                 method='GET', path_info='/requests/',
    #                 server_protocol='HTTP/1.1',
    #                 server_port='8080',
    #                 remote_address='10.240.208.91'
    # ) for i in range(1, quantity)]
    # insert_list = []
    # for i in range(quantity):
    #     method='GET'
    #     path_info='/requests/'
    #     server_protocol='HTTP/1.1',
    #     server_port='8080',
    #     remote_address='10.240.208.91'
    #     insert_list.append(StoredRequests(method=method, server_protocol=server_protocol, server_port=server_port, remote_address=remote_address))                 
    
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

class TicketTests(TestCase):
	def test_general(self):
		# Пользователь заходит на главную страницу
		response = self.client.get(reverse('hello:index'))
		self.assertEqual(response.status_code, 200)
		# и видит ссылку, которая называется requests
		self.assertContains(response, "<a href='/requests/'>requests")
		
		# Он нажимает на ссылку и видит страницу с запросами (макс. 10 последних запроса),
		create_test_data(quantity=10)
		selected_requests = StoredRequests.objects.reverse()[:10]
		response = self.client.get(reverse('list_requests:requests'))
		self.assertEqual(response.status_code, 200)
		print selected_requests.count()
		print response
		self.assertEqual(response.context['selected_requests'].count(), 10)
		
		# которые храняться в базе данных.
		# Страница обновляется автоматически так как появляются новые запросы
		# При этом обновляется заголовок страницы.
		# В заголовке страницы должно отображаться общее количество запросов в формате (N).
		# Пользователь снова зайдет на страницу с запросами, то список запросов 
		# начнет отображать уже новые запросы. Может использовать идентификатор сеанса или по времени
		
		
'''
    def test_index_view_with_no_polls(self):
        """
        If no polls exist, an appropriate message should be displayed.
        """
        response = self.client.get(reverse('polls:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No polls are available.")
        self.assertQuerysetEqual(response.context['latest_poll_list'], [])

    def test_index_view_with_a_past_poll(self):
        """
        Polls with a pub_date in the past should be displayed on the index page.
        """
        create_poll(question="Past poll.", days=-30)
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(
            response.context['latest_poll_list'],
            ['<Poll: Past poll.>']
        )

    def test_index_view_with_a_future_poll(self):
        """
        Polls with a pub_date in the future should not be displayed on the
        index page.
        """
        create_poll(question="Future poll.", days=30)
        response = self.client.get(reverse('polls:index'))
        self.assertContains(response, "No polls are available.", status_code=200)
        self.assertQuerysetEqual(response.context['latest_poll_list'], [])

    def test_index_view_with_future_poll_and_past_poll(self):
        """
        Even if both past and future polls exist, only past polls should be
        displayed.
        """
        create_poll(question="Past poll.", days=-30)
        create_poll(question="Future poll.", days=30)
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(
            response.context['latest_poll_list'],
            ['<Poll: Past poll.>']
        )

    def test_index_view_with_two_past_polls(self):
        """
        The polls index page may display multiple polls.
        """
        create_poll(question="Past poll 1.", days=-30)
        create_poll(question="Past poll 2.", days=-5)
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(
            response.context['latest_poll_list'],
             ['<Poll: Past poll 2.>', '<Poll: Past poll 1.>']
        )
'''

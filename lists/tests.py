from django.core.urlresolvers import resolve
from django.http import HttpRequest
from django.template.loader import render_to_string
from django.test import TestCase
from lists.views import home_page


# Create your tests here.
class HomePageTest(TestCase):
    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)

    def test_home_page_returns_correct_html(self):
        # 상수를 테스트하지 않고 템플릿을 이용해서 렌더링하는 것을 테스트하도록 수정
        request = HttpRequest()
        response = home_page(request)
        expected_html = render_to_string('home.html')

        # 구현 결과물을 비교
        self.assertEqual(response.content.decode(), expected_html)

    def test_home_page_can_save_a_POST_request(self):
        request = HttpRequest()
        request.method = 'POST'
        request.POST['item_text'] = '신규 작업 아이템'

        response = home_page(request)

        self.assertIn('신규 작업 아이템', response.content.decode())
        expected_html = render_to_string(
            'home.html',
            {'new_item_text': '신규 작업 아이템'}
        )
        self.assertEqual(response.content.decode(), expected_html)

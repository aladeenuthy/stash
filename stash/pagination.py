from rest_framework.pagination import PageNumberPagination, Response
class DefaultPagination(PageNumberPagination):
    page_size = 1
    def get_paginated_response(self, data):
        return Response({
            'count': self.page.paginator.count,
            'next': self.page.next_page_number() if self.page.has_next() else None,
            'previous': self.page.previous_page_number() if self.page.has_previous() else None,
            'results': data,
        })
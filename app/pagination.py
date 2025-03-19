from rest_framework.pagination import PageNumberPagination


class OpenWheelBasePaginator(PageNumberPagination):
    page_size: int = 20
    max_page_size: int = 100

    page_query_param: str = "page"
    page_size_query_param: str = "page-size"


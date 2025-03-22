from rest_framework.pagination import PageNumberPagination


class OpenWheelBasePaginator(PageNumberPagination):
    page_size: int = 10

    page_query_param: str = "page"
    page_size_query_param: str = "page-size"


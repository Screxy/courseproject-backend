from rest_framework import pagination


class ShoeModelPagination(pagination.LimitOffsetPagination):
    default_limit = 3
    limit_query_param = "limit"
    offset_query_param = "offset"

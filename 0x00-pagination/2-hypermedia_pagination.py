#!/usr/bin/env python3
"""simple_pagination"""
import csv
import math
from typing import List


def index_range(page, page_size):
    """index_range"""
    second = page * page_size
    first = second - page_size
    return (first, second)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        assert type(page) is int and page > 0
        assert type(page_size) is int and page_size > 0
        with open('7d3576d97e7560ae85135cc214ffe2b3412c51d7(1).csv') as file:
            content = file.readlines()
        rows = content[1:]
        to_find = index_range(page,  page_size)
        if (page_size > len(rows) or page > len(rows)):
            return []
        return self.dataset()[to_find[0]:to_find[1]]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        """get_hyper method"""
        data_value = self.get_page(page, page_size)
        total_value = math.ceil(len(self.dataset()) / page_size)
        prev_value = None if page - 1 ==\
            0 else page - 1
        next_value = None if page + 1 >\
            total_value else page + 1
        return {'page_size': len(data_value),
                'page': page,
                'data': data_value,
                'prev_page': prev_value,  'next_page': next_value,
                'total_pages': total_value}

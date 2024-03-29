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
        to_find: tuple = index_range(page,  page_size)
        if (page_size > len(self.dataset()) or page > len(self.dataset())):
            return []
        return self.dataset()[to_find[0]:to_find[1]]

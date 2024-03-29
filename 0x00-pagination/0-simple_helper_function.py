#!/usr/bin/env python3
"""index_range funcation"""


def index_range(page, page_size):
    """index_range"""
    second = page * page_size
    first = second - page_size
    return (first, second)

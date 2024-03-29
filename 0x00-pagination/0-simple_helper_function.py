#!/usr/bin/env python3
""" A script to generate a list for
particular pagination parameters"""


def index_range(page: int, page_size: int) -> tuple:
    """ a function named index_range that
    takes two integer arguments page and page_size."""
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return (start_index, end_index)

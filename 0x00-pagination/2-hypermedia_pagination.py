#!/usr/bin/env python3
"""
Defines class Server that paginates a database of popular baby names
"""
import csv
import math
from typing import List, Dict
index_range = __import__('0-simple_helper_function').index_range


class Server:
    """Server class to paginate a database of popular baby names.
"""
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset"""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]
        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Return the appropriate page of the dataset
        (i.e. the correct list of rows).

        Args:
            page (int, optional): Defaults to 1.
            page_size (int, optional): Defaults to 10.

        Returns:
            List[List]: _description_
        """
        assert isinstance(page, int)
        assert isinstance(page_size, int)
        assert page > 0
        assert page_size > 0
        dataset = self.dataset()
        try:
            tuple = index_range(page, page_size)
            return dataset[tuple[0]:tuple[1]]
        except IndexError:
            return []

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """returns a dictionary of hypermedia keys and values

        Args:
            page (int, optional):Defaults to 1.
            page_size (int, optional):Defaults to 10.
        """
        paginated_dataset = self.get_page(page, page_size)
        dataset = self.dataset()
        tuple = index_range(page, page_size)
        pages = (len(dataset) + page_size - 1) // page_size
        data = {
            "page_size": page_size,
            "page": page,
            "data": paginated_dataset,
            "next_page": page + 1 if tuple[1] < len(dataset) else None,
            "prev_page": page - 1 if tuple[0] > 1 else None,
            "total_pages": pages
        }
        return data

# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.inline_response200 import InlineResponse200  # noqa: E501
from swagger_server.test import BaseTestCase


class TestDefaultController(BaseTestCase):
    """DefaultController integration test stubs"""

    def test_gene_symbols_get(self):
        """Test case for gene_symbols_get

        Gets gene symbols
        """
        query_string = [('gene_symbol', 'gene_symbol_example')]
        response = self.client.open(
            '/ksens/reveal-genomics-basic/1.0/gene_symbols',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()

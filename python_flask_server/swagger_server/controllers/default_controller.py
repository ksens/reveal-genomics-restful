import connexion
import six

from swagger_server.models.inline_response200 import InlineResponse200  # noqa: E501
from swagger_server import util


def gene_symbols_get(gene_symbol=None):  # noqa: E501
    """Gets gene symbols

    Returns a list of gene symbols from the database # noqa: E501

    :param gene_symbol: gene symbol to search by
    :type gene_symbol: str

    :rtype: List[InlineResponse200]
    """
    return 'do some magic!'

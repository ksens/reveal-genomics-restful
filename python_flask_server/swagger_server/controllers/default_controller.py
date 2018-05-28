import connexion
import six
import pandas as pd
import numpy as np

from swagger_server.models.inline_response200 import InlineResponse200  # noqa: E501
from swagger_server import util


def gene_symbols_get(gene_symbol=None):  # noqa: E501
    """Gets gene symbols

    Returns a list of gene symbols from the database # noqa: E501

    :param gene_symbol: gene symbol to search by
    :type gene_symbol: str

    :rtype: List[InlineResponse200]
    """

    symbols = gene_symbol.split("|")
    print("symbols")
    print(symbols)
    arr = np.array([range(0,len(symbols)), symbols]).transpose()
    print("arr")
    print(arr)
    df = pd.DataFrame(data=arr, columns=['gene_symbol_id', 'gene_symbol'])
    print("df")
    print(df)

    return df.to_json(orient='records')

# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import unicode_literals

from schematizer.models.sql_entities import SQLColumnDataType


class RedshiftUnsupportedType(SQLColumnDataType):
    """Dummy class to test error handling code for
    unsupported datatypes
    """
    type_name = 'redshift_unsupported_type'

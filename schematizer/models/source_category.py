# -*- coding: utf-8 -*-
from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import UniqueConstraint

from schematizer.models.database import Base
from schematizer.models.types.time import build_time_column


class SourceCategory(Base):

    __tablename__ = 'source_category'
    __tableargs__ = (
        UniqueConstraint(
            'source_id',
            name='source_unique_constraint'
        ),
    )

    id = Column(Integer, primary_key=True)

    # ID of the source this entry refers to
    source_id = Column(
        Integer,
        ForeignKey('source.id'),
        nullable=False
    )

    # Category that the source belongs to
    category = Column(String, nullable=False)

    # Timestamp when the entry is created
    created_at = build_time_column(
        default_now=True,
        nullable=False
    )

    # Timestamp when the entry is last updated
    updated_at = build_time_column(
        default_now=True,
        onupdate_now=True,
        nullable=False
    )

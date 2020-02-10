#
# Copyright (C) 2014-2019 S[&]T, The Netherlands.
#

from __future__ import absolute_import, division, print_function

import os

from muninn.schema import *
from muninn.util import split_path
from muninn.remote import *


class ArchivePath(Text):
    _alias = "archive_path"

    @classmethod
    def validate(cls, value):
        super(ArchivePath, cls).validate(value)
        if os.path.isabs(value) or os.path.pardir in split_path(value):
            raise ValueError("invalid value %r for type %r" % (value, cls.name()))


class Basename(Text):
    @classmethod
    def validate(cls, value):
        super(Basename, cls).validate(value)
        if value != os.path.basename(value):
            raise ValueError("invalid value %r for type %r" % (value, cls.name()))


class Remote(Text):
    @classmethod
    def validate(cls, value):
        super(Remote, cls).validate(value)
        # NOTE: We used to verify the value started with one of the supported prefixes
        # But now the list can be extended through a remote backend plugin, which is
        # archive dependent. The validation is now done at pull-time.


class Core(Mapping):
    uuid = UUID()
    active = Boolean()
    hash = Text(optional=True)
    size = Long(optional=True)
    metadata_date = Timestamp
    archive_date = Timestamp(optional=True)
    archive_path = ArchivePath(optional=True)
    product_type = Text()
    product_name = Text()
    physical_name = Basename()
    validity_start = Timestamp(optional=True)
    validity_stop = Timestamp(optional=True)
    creation_date = Timestamp(optional=True)
    footprint = Geometry(optional=True)
    remote_url = Remote(optional=True)

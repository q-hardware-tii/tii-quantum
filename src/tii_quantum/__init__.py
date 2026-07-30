"""The `tii-quantum` package"""

import importlib.metadata as im

__version__ = im.version(__package__)

from .job import Job, JobStatus
from .tii_client import Client

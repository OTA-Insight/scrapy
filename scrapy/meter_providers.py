"""
Scrapy extension for collecting otlp metrics
"""
from abc import ABC, abstractmethod
import logging
from typing import TYPE_CHECKING, Optional

from opentelemetry.metrics import NoOpMeterProvider, MeterProvider

if TYPE_CHECKING:
    from scrapy.crawler import Crawler

logger = logging.getLogger(__name__)


class MeterProvider(MeterProvider, ABC):
    """
    Wrapper for MeterProvider so we have crawler available during init.
    """
    @abstractmethod
    def __init__(self, crawler: "Crawler"):
        """
        Use crawler to configure the Meter Provider
        """

class NoOpMeterProvider(NoOpMeterProvider, MeterProvider):
    """
    Wrapper for NoOpMeterProvider so we support passing crawler during init.
    """
    def __init__(self, crawler: "Optional[Crawler]" = None):
        super(NoOpMeterProvider).__init__()
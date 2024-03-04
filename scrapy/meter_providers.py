"""
Scrapy extension for collecting otlp metrics
"""
from abc import ABC, abstractmethod
import logging
from typing import TYPE_CHECKING

from opentelemetry.metrics import NoOpMeterProvider, MeterProvider
from opentelemetry.sdk.metrics.view import View

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
        super().__init__()
        self._views: list[View] = []

    def add_view(self, view: View):
        """
        Supporting adding views dynamically so metric users can do this where they create metrics
        """
        self._views.append(view)

class NoOpMeterProvider(NoOpMeterProvider, MeterProvider):
    """
    Wrapper for NoOpMeterProvider so we support passing crawler during init.
    """
    def __init__(self, crawler: "Crawler"):
        super().__init__(crawler)
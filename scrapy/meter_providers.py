"""
Scrapy extension for collecting otlp metrics
"""
import logging
from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

from opentelemetry.metrics import MeterProvider as OTMeterProvider
from opentelemetry.metrics import NoOpMeterProvider as OTNoOpMeterProvider
from opentelemetry.sdk.metrics.view import View

if TYPE_CHECKING:
    from scrapy.crawler import Crawler

logger = logging.getLogger(__name__)


class MeterProvider(OTMeterProvider, ABC):
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


class NoOpMeterProvider(OTNoOpMeterProvider, MeterProvider):
    """
    Wrapper for NoOpMeterProvider so we support passing crawler during init.
    """

    def __init__(self, crawler: "Crawler"):
        super().__init__(crawler)

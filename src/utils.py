"""Utilities common to the various analysers."""
from __future__ import annotations

import io
import typing
import urllib.request

from PIL import Image


class BaseAnalyser:
    """Base class for analysing images."""

    @classmethod
    def from_url(cls, url: str) -> BaseAnalyser:
        """Open and use an image from a URL."""
        data = urllib.request.urlopen(url).read()
        im = Image.open(io.BytesIO(data))
        return cls(im)

    @classmethod
    def from_file(cls, path_or_file: typing.Union[
            str, io.BufferedIOBase]) -> BaseAnalyser:
        """Open and use an image from a file path or file."""
        im = Image.open(path_or_file)
        return cls(im)

    def __init__(self, image: Image.Image):
        """Store an image."""
        self.image = image

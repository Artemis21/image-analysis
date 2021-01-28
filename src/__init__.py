"""Colate the various analysers."""
import io

from PIL import Image

from .colour_displayer import ColourDisplayer    # noqa: F401
from .top_colours import TopColoursAnalyser    # noqa:F401


def top_colours_chart(
        *, fp: str = None, file: io.BufferedIOBase = None, url: str = None,
        tolerance: int = 64, max_colours: int = 27) -> Image.Image:
    """Get a chart of top colours for some image."""
    if fp:
        analyser = TopColoursAnalyser.from_file(fp)
    elif file:
        analyser = TopColoursAnalyser.from_file(file)
    elif url:
        analyser = TopColoursAnalyser.from_url(url)
    else:
        raise ValueError('Exactly one of fp, file or url should be passed.')
    top_colours = analyser.analyse(
        tolerance=tolerance, max_colours=max_colours
    )
    displayer = ColourDisplayer(top_colours)
    chart = displayer.display()
    return chart

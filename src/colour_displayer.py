"""Tool for displaying a selection of colours."""
import math
import pathlib

from PIL import Image, ImageDraw, ImageFont


_font_path = str(pathlib.Path(__file__).parent.absolute() / 'res' / 'font.ttf')
FONT = ImageFont.truetype(_font_path, size=20)


class ColourDisplayer:
    """Tool for displaying a selection of colours."""

    def __init__(self, colours: list[tuple[int, int, int]]):
        """Store the colours."""
        self.colours = colours
        self.im = None
        self.draw = None

    def display(self) -> Image.Image:
        """Draw the colours."""
        columns = round((0.3 * len(self.colours)) ** 0.5)
        rows = math.ceil(len(self.colours) / columns)
        self.im = Image.new('RGB', (columns * 100, rows * 30))
        self.draw = ImageDraw.Draw(self.im)
        row = column = 0
        for colour in self.colours:
            self.draw_colour(colour, row, column)
            column += 1
            if column >= columns:
                column = 0
                row += 1
        return self.im

    def draw_colour(self, colour: tuple[int, int, int], row: int, column: int):
        """Draw a colour on the image."""
        text = '#{0:0>2x}{1:0>2x}{2:0>2x}'.format(*colour).upper()
        if sum(colour) / 3 > 128:
            text_colour = (0, 0, 0)
        else:
            text_colour = (255, 255, 255)
        x_start = column * 100
        y_start = row * 30
        self.draw.rectangle(
            (x_start, y_start, x_start + 100, y_start + 30), fill=colour
        )
        self.draw.text(
            (x_start + 8, y_start + 3), text, fill=text_colour, font=FONT
        )

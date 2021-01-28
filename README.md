# image-analysis

Random Python tools for image analysis, mainly for fun.

[Analysers](#analysers)

- [Top Colours Analyser](#top-colours-analyser)

[Other Tools](#other-tools)

- [Colour Displayer](#colour-displayer)

[Reference](#reference)

## Analysers

### Top Colours Analyser

Gets the top colours from an image. It does this by grouping the pixels in the image into groups of similar colours, and sorting these by the number of pixels in each.

To group pixels in to similar colours:

- A colour is treated as a point in 3D space, where the three axis represent red, blue and green.
- The colour-space is split into cubes of side length `tolerance`.
- Colours in the same or adjacent cubes are considered similar.

Example usuage:
```python
analyser = TopColoursAnalyser.from_url('https://picsum.photos/200')
print(analyser.analyse())
```

## Other Tools

### Colour Displayer

Displays a list of colours as an image.

Example usuage:
```python
displayer = ColourDisplayer([
    (255, 0, 0), (255, 128, 0), (255, 255, 0),
    (0, 255, 0), (0, 0, 255), (128, 0, 128)
])
displayer.display().show()
```

# Reference

- `ColourDisplayer`

  A tool for displaying a selection of colours.

  Parameters:

  - `colours` - A list of 3-tuples representing RGB colours.

  Methods:

  - `display()`

    Draws the image. Returns an instance of `PIL.Image.Image`.

- `TopColoursAnalyser`

  A tool for analysing the top colours in an image.

  Parameters:

  - `im` - An instance of `PIL.Image.Image`.

  Constructors:

  - `from_url(url: str)`

    Loads an image from a URL.

  - `from_file(path_or_file: Union[str, BytesIO])`

    Loads an image from a file path or file open in `rb` mode (or an instance of `BytesIO`).

  Methods:

  - `analyse(tolerance: int = 64, max_colours: int = 27)`

    Analyses the image.

    Parameters:

    - `tolerance`: How close colours have to be to be considered the same.
    - `max_colours`: The maximum number of colours to return.

    Returns:

    A list of 3-tuples representing RGB colours.

- `top_colours_chart(*, fp: str = None, file: BufferedIOBase = None, url: str = None, tolerance: int = 64, max_colours: int = 27)`

  A utility function to get the top colours from an image (using `TopColoursAnalyser`) and display them (using `ColourDisplayer`).

  Parameters:

  - `fp` - The path to an image to analyse.
  - `file` - An open image to analyse. Should be a file opened in `rb` mode or an instance of `BytesIO`.
  - `url` - A URL to an image to analyse.
  - `tolerance`: How close colours have to be to be considered the same.
  - `max_colours`: The maximum number of colours to return.

  All parameters must be keyword arguments, and exactly one of `fp`, `file` and `url` should be passed.

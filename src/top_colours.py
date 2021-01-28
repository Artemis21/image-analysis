"""Tool for analysing the top colours in an image."""
from collections import Counter, defaultdict

from .utils import BaseAnalyser


Colour = tuple[int, int, int]


class TopColoursAnalyser(BaseAnalyser):
    """Tool for analysing the top colours in an image."""

    def put_points_in_areas(
            self, tolerance: int) -> tuple[
                dict[Colour, list[Colour], Counter[Colour, int]]]:
        """Put the points into areas."""
        image = self.image.convert('RGB')
        area_points = defaultdict(list)
        point_counts = Counter(image.getdata())
        for r, g, b in point_counts:
            area = r // tolerance, g // tolerance, b // tolerance
            area_points[area].append((r, g, b))
        return area_points, point_counts

    def put_areas_in_groups(
            self, tolerance: int,
            area_points: dict[Colour, list[Colour]]) -> dict[Colour, int]:
        """Sort the areas into groups."""
        area_groups = {}
        next_group = 1
        for r_start, g_start, b_start in area_points:
            group = None
            for dr in (-tolerance, 0):
                for dg in (-tolerance, 0):
                    for db in (-tolerance, 0):
                        if (dr, dg, db) == (0, 0, 0):
                            continue
                        r = r_start + dr
                        g = g_start + dg
                        b = b_start + db
                        if (r, g, b) in area_groups:
                            group = area_groups[(r, g, b)]
            if not group:
                group = next_group
                next_group += 1
            area_groups[(r_start, g_start, b_start)] = group
        return area_groups

    def merge_areas_by_group(
            self, area_groups: dict[Colour, int], area_points: dict[
                Colour, list[Colour]]) -> dict[int, list[Colour]]:
        """Merge the points from areas that are in the same group."""
        group_points = defaultdict(list)
        for area, group in area_groups.items():
            group_points[group].extend(area_points[area])
        return group_points

    def get_top_colours(
            self, group_points: dict[int, list[Colour]],
            point_counts: Counter[Colour, int]) -> list[Colour]:
        """Count the top grouped colours."""
        colour_counts = []
        for _group, points in group_points.items():
            total_r = total_g = total_b = 0
            count = 0
            for point in points:
                point_count = point_counts[point]
                r, g, b = point
                total_r += r * point_count
                total_g += g * point_count
                total_b += b * point_count
                count += point_count
            colour = (
                round(total_r / count),
                round(total_g / count),
                round(total_b / count)
            )
            colour_counts.append((count, colour))
        return list(reversed(
            [colour for _count, colour in sorted(colour_counts)]
        ))

    def analyse(
            self, tolerance: int = 64, max_colours: int = 27) -> list[Colour]:
        """Get the top colours from the image."""
        area_points, point_counts = self.put_points_in_areas(tolerance)
        area_groups = self.put_areas_in_groups(tolerance, area_points)
        group_points = self.merge_areas_by_group(area_groups, area_points)
        top_colours = self.get_top_colours(group_points, point_counts)
        return top_colours[:max_colours]

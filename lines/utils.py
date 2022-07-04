from pprint import pprint
from typing import Any, List

from pyautocad import Autocad


def create_list_of_elements(acad: Autocad) -> List[Any]:
    elements = []
    for obj in acad.iter_objects():
        print(obj.ObjectName)
        elements.append(obj)
    pprint(elements)
    return elements


def create_projected_lines(elements: List[Any]) -> List[Any]:
    projected_lines = []
    for elem in enumerate(elements):
        if elem.Layer == "Proli":
            projected_lines.append(elem)
    return projected_lines


def find_cross_points(elements: List[Any], projected_lines: List[Any]):
    cross_points = []
    for elem in enumerate(elements):
        print(projected_lines[0].IntersectWith(elem, 0))
        if len(projected_lines[0].IntersectWith(elem, 0)) > 0:
            cross_points.append(projected_lines[0].IntersectWith(elem, 0))
    return cross_points

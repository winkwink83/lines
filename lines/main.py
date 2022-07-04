from pprint import pprint

from pyautocad import APoint, Autocad

from lines.utils import (
    create_list_of_elements,
    create_projected_lines,
    find_cross_points,
)


def main():
    acad = Autocad(create_if_not_exists=True)
    acad.prompt("Hello, Autocad from Python\n")
    print(acad.doc.Name)

    lista_elementow = create_list_of_elements(acad=acad)

    print(len(lista_elementow))
    print("current layer: " + lista_elementow[6].Layer)

    lista_projektowane_linie = create_projected_lines(elements=lista_elementow)
    pprint(lista_projektowane_linie)

    cross_points = find_cross_points(
        elements=lista_elementow, projected_lines=lista_projektowane_linie
    )

    pprint(cross_points)

    for point in enumerate(cross_points):
        x = point[0]  # I'm not sure whether this should be called "x"
        y = point[1]  # I'm not sure whether this should be called "y"
        acad.model.AddLine(APoint(x, y), APoint(x, y + 30))


if __name__ == "__main__":
    main()

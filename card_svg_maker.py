from jinja2 import Environment, FileSystemLoader

environment = Environment(loader=FileSystemLoader("templates/"))
card_template = environment.get_template("card.svg.j2")


shapes = ['pill', 'diamond', 'squiggle']
numbers = [1, 2, 3]
colors = ['green', 'red', 'blue']
patterns = ["none", "striped", "solid"]


def get_positions(count, cardHeight = 180):

    center = cardHeight / 2;
    spacing = 45;

    if count == 1:
        return [center]
    if count == 2:
        return [center-spacing/2, center+spacing/2]
    if count == 3:
        return [center-spacing, center, center+spacing]


def generate_cards():
    a = -1
    for shape in shapes:
        a += 1
        b = -1
        for color in colors:
            b += 1
            c = -1
            for pattern in patterns:
                c += 1
                d = -1
                for n in numbers:
                    d += 1
                    positions = [{'x': 60, 'y': k} for k in get_positions(n)]
                    p = "none"
                    if pattern == "solid":
                        p = color
                    elif pattern == "striped":
                        p = f'url(#striped-{color})'
                    card = { 'shape': shape, 'color':color, 'pattern': p, 'positions': positions }
                    content = card_template.render(card)
                    with open(f'cards/{a}{b}{c}{d}.svg', 'w', encoding="utf-8") as f:
                        f.write(content)



if __name__ == '__main__':
    generate_cards()

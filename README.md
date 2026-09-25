# Fun Exercises

A set of timed fun exercises.

This is a single page application built with:
* HTML5 Canvas
* CSS
* JavaScript
* SVG assets generated with Python and Jinja

[demo](https://brianpzaide.github.io/fbc_set_games/)

### Exercises

* SET® game inspired timed exercise. SET® is a trademark of its respective owner. This project is an independent, non-commercial project and is not affiliated with or endorsed by the owners of SET®. 
The cards used in this project were generated from scratch as SVG files using Python and Jinja. They are *not* copies of the original game's artwork. See `card_svg_maker.py` file. 

* The next two types of timed exercises are based around the [Fibonacci clock](https://www.instructables.com/The-Fibonacci-Clock/) concept.

### Running locally

Clone the repository and start a simple local web server:
`python -m http.server`

The site would be served at: `http://localhost:8000`

To generate the cards for the SET-inspired exercise:
`python card_svg_maker.py` 

The `Python` and `Jinja` are only required for generating the SVG card assets for the SET-inspired exercise.


### Non-commercial / independent project

This is a personal, non-commercial project.

The project is not affiliated with, sponsored by, or endorsed by the creators or owners of any third-party games or trademarks referenced by individual exercises.

Third-party names and trademarks belong to their respective owners and are mentioned only to describe the inspiration for the exercises.

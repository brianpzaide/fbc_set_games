# Mental Exercises

A small collection of timed mental exercises.

This is a simple, single page, browser-based collection of timed exercises built with:
* HTML5 Canvas
* CSS
* JavaScript
* SVG assets generated with Python and Jinja

Live demo: https://brianpzaide.github.io/fbc_set_games/

### Exercises

#### Visual pattern matching

This exercise is inspired by the card game SET®. SET® is a trademark of its respective owner. This project is an independent, non-commercial project and is not affiliated with or endorsed by the owners of SET®.

The cards used in this project were generated from scratch as SVG files using Python and Jinja. They are *not* copies of the original game's artwork. See `card_svg_maker.py` file. 

#### Fibonacci Clock

A timed exercise based around the [Fibonacci clock](https://www.instructables.com/The-Fibonacci-Clock/) concept.

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

Third-party names and trademarks belong to their respective owners and are mentioned only to describe the inspiration for an exercise.

### License

Third-party names, trademarks, and intellectual property remain the property of their respective owners.

from urllib.parse import parse_qs

from jinja2 import Environment, FileSystemLoader

from requests import HTTPResponseCode
from db.db import expenses, categories, colors
from random_colors import random_colors


class Controller:
    def __init__(self, request, response):
        self.request = request
        self.response = response
        self.env = Environment(loader=FileSystemLoader('templates/'))


class PagesController(Controller):
    def __init__(self, request, response):
        super().__init__(request, response)
        self.response.add_header('Content-Type', 'text/html')

    def home(self):
        if self.request.method == 'POST':
            data = parse_qs(self.request.body.decode())
            expenses.append(
                {"category": data["category"][0], "description": data["description"][0],
                 "amount": int(data["amount"][0])}
            )

        template = self.env.get_template('home.html')
        total = sum([expense["amount"] for expense in expenses])
        body = template.render(expenses=expenses, total=total)
        self.response.set_body(body)

    def add(self):
        template = self.env.get_template('adding.html')
        body = template.render(categories=categories)
        self.response.set_body(body)

    def stats(self):
        template = self.env.get_template('stats.html')
        food_total = sum([expense["amount"] for expense in expenses if expense['category'] == "Food"])
        car_total = sum([expense["amount"] for expense in expenses if expense['category'] == "Car"])
        ent_total = sum([expense["amount"] for expense in expenses if expense['category'] == "Entertainment"])

        marker_colors = random_colors(colors)

        expense_categories = [
            {"category": 'Food', "amount": food_total, "color": marker_colors[0]},
            {"category": 'Car', "amount": car_total, "color": marker_colors[1]},
            {"category": 'Entertainment', "amount": ent_total, "color": marker_colors[2]}
        ]

        total = food_total + car_total + ent_total
        body = template.render(expense_categories=expense_categories, total=total)
        self.response.set_body(body)

    @staticmethod
    def not_found(request, response):
        response.add_header('Content-Type', 'text/html')
        response.set_status(HTTPResponseCode.NOT_FOUND)
        response.set_body('<h1>404 Not Found</h1>')


class CssController(Controller):

    def css(self):
        css_file_path = f'./templates/static.css'
        with open(css_file_path, 'rb') as file:
            css_content = file.read()
            self.response.set_body(css_content, is_file=True)
            self.response.add_header('Content-Type', 'text/css')


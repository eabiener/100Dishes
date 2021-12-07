import csv
import os
import cs50
from cs50 import SQL
from flask import Flask, flash, jsonify, redirect, render_template, request, session
from flask_session import Session

open("meals.db", "w").close()
db = cs50.SQL("sqlite:///meals.db")

db.execute("CREATE TABLE meals (id INT, dish TEXT, cuisine TEXT, PRIMARY KEY (id))")
db.execute("CREATE TABLE diets (meal_id INT, diet TEXT, FOREIGN KEY(meal_id) REFERENCES meals(id))")

with open("1,000 Dishes Large.tsv", "r") as dishes:
    reader = csv.DictReader(dishes, delimiter="\t")
    for row in reader:
        db.execute("INSERT INTO meals(id, dish, cuisine) VALUES (?,?,?)", row["ID"], row["Dish"], row["Cuisine"])
        for diet in row["Diet"].split(","):
            db.execute("INSERT INTO diets (meal_id, diet) VALUES(?, ?)", row["ID"], diet)

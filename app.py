import csv
import os
import cs50
from cs50 import SQL
from flask import Flask, flash, jsonify, redirect, render_template, request, session
from flask_session import Session

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

db = cs50.SQL("sqlite:///meals.db")

@app.route("/")
def index():
        return render_template("index.html", x = "")

@app.route("/results", methods=["GET", "POST"])
def results():
    if request.method == "GET":
        return render_template("index.html", x = "")
    else:
        session["dietary"] = request.form.getlist("diet[]")
        y = str(session["dietary"])[1:-1]
        numchecked = len(session["dietary"])
        if numchecked == 0:
            bigtable = db.execute("SELECT DISTINCT dish FROM meals JOIN diets ON id = meal_id")
            tindian = {}
            teuropean = {}
            tjkor = {}
            tchinese = {}
            tuscan = {}
            tmena = {}
            tsea = {}
            tauzpac = {}
            tafr = {}
            tlatam = {}
            indian = db.execute("SELECT DISTINCT dish FROM meals JOIN diets ON id = meal_id WHERE cuisine = 'Indian' ORDER BY random() LIMIT 10")
            for row in indian:
                x = list(row.values())
                tindian[x[0]] = x[0]
            european = db.execute("SELECT DISTINCT dish FROM meals JOIN diets ON id = meal_id WHERE cuisine = 'European' ORDER BY random() LIMIT 10")
            for row in european:
                x = list(row.values())
                teuropean[x[0]] = x[0]
            jkor = db.execute("SELECT DISTINCT dish FROM meals JOIN diets ON id = meal_id WHERE cuisine = 'Japanese/Korean' ORDER BY random() LIMIT 10")
            for row in jkor:
                x = list(row.values())
                tjkor[x[0]] = x[0]
            chinese = db.execute("SELECT DISTINCT dish FROM meals JOIN diets ON id = meal_id WHERE cuisine = 'Chinese' ORDER BY random() LIMIT 10")
            for row in chinese:
                x = list(row.values())
                tchinese[x[0]] = x[0]
            uscan = db.execute("SELECT DISTINCT dish FROM meals JOIN diets ON id = meal_id WHERE cuisine = 'U.S./Canada' ORDER BY random() LIMIT 10")
            for row in uscan:
                x = list(row.values())
                tuscan[x[0]] = x[0]
            mena = db.execute("SELECT DISTINCT dish FROM meals JOIN diets ON id = meal_id WHERE cuisine = 'Middle Eastern/North African' ORDER BY random() LIMIT 10")
            for row in mena:
                x = list(row.values())
                tmena[x[0]] = x[0]
            sea = db.execute("SELECT DISTINCT dish FROM meals JOIN diets ON id = meal_id WHERE cuisine = 'Southeast Asian' ORDER BY random() LIMIT 10")
            for row in sea:
                x = list(row.values())
                tsea[x[0]] = x[0]
            auzpac = db.execute("SELECT DISTINCT dish FROM meals JOIN diets ON id = meal_id WHERE cuisine = 'Aus/NZ and Pacific Islands' ORDER BY random() LIMIT 10")
            for row in auzpac:
                x = list(row.values())
                tauzpac[x[0]] = x[0]
            afr = db.execute("SELECT DISTINCT dish FROM meals JOIN diets ON id = meal_id WHERE cuisine = 'African' ORDER BY random() LIMIT 10")
            for row in afr:
                x = list(row.values())
                tafr[x[0]] = x[0]
            latam = db.execute("SELECT DISTINCT dish FROM meals JOIN diets ON id = meal_id WHERE cuisine = 'Latin American' ORDER BY random() LIMIT 10")
            for row in latam:
                x = list(row.values())
                tlatam[x[0]] = x[0]
            return render_template("results.html", tindian=tindian, teuropean=teuropean, tjkor=tjkor, tchinese=tchinese, tuscan=tuscan, tmena=tmena, tsea=tsea, tauzpac=tauzpac, tafr=tafr, tlatam=tlatam, y = y)

        elif numchecked == 1:
            firstchk = session["dietary"][0]
            tindian = {}
            teuropean = {}
            tjkor = {}
            tchinese = {}
            tuscan = {}
            tmena = {}
            tsea = {}
            tauzpac = {}
            tafr = {}
            tlatam = {}
            indian = db.execute("SELECT dish FROM meals JOIN diets ON id = meal_id WHERE diet = ? AND cuisine = 'Indian' ORDER BY random() LIMIT 10", firstchk)
            for row in indian:
                x = list(row.values())
                tindian[x[0]] = x[0]
            european = db.execute("SELECT dish FROM meals JOIN diets ON id = meal_id WHERE diet = ? AND cuisine = 'European' ORDER BY random() LIMIT 10", firstchk)
            for row in european:
                x = list(row.values())
                teuropean[x[0]] = x[0]
            jkor = db.execute("SELECT dish FROM meals JOIN diets ON id = meal_id WHERE diet = ? AND cuisine = 'Japanese/Korean' ORDER BY random() LIMIT 10", firstchk)
            for row in jkor:
                x = list(row.values())
                tjkor[x[0]] = x[0]
            chinese = db.execute("SELECT dish FROM meals JOIN diets ON id = meal_id WHERE diet = ? AND cuisine = 'Chinese' ORDER BY random() LIMIT 10", firstchk)
            for row in chinese:
                x = list(row.values())
                tchinese[x[0]] = x[0]
            uscan = db.execute("SELECT dish FROM meals JOIN diets ON id = meal_id WHERE diet = ? AND cuisine = 'U.S./Canada' ORDER BY random() LIMIT 10", firstchk)
            for row in uscan:
                x = list(row.values())
                tuscan[x[0]] = x[0]
            mena = db.execute("SELECT dish FROM meals JOIN diets ON id = meal_id WHERE diet = ? AND cuisine = 'Middle Eastern/North African' ORDER BY random() LIMIT 10", firstchk)
            for row in mena:
                x = list(row.values())
                tmena[x[0]] = x[0]
            sea = db.execute("SELECT dish FROM meals JOIN diets ON id = meal_id WHERE diet = ? AND cuisine = 'Southeast Asian' ORDER BY random() LIMIT 10", firstchk)
            for row in sea:
                x = list(row.values())
                tsea[x[0]] = x[0]
            auzpac = db.execute("SELECT dish FROM meals JOIN diets ON id = meal_id WHERE diet = ? AND cuisine = 'Aus/NZ and Pacific Islands' ORDER BY random() LIMIT 10", firstchk)
            for row in auzpac:
                x = list(row.values())
                tauzpac[x[0]] = x[0]
            afr = db.execute("SELECT dish FROM meals JOIN diets ON id = meal_id WHERE diet = ? AND cuisine = 'African' ORDER BY random() LIMIT 10", firstchk)
            for row in afr:
                x = list(row.values())
                tafr[x[0]] = x[0]
            latam = db.execute("SELECT dish FROM meals JOIN diets ON id = meal_id WHERE diet = ? AND cuisine = 'Latin American' ORDER BY random() LIMIT 10", firstchk)
            for row in latam:
                x = list(row.values())
                tlatam[x[0]] = x[0]
            return render_template("results.html", tindian=tindian, teuropean=teuropean, tjkor=tjkor, tchinese=tchinese, tuscan=tuscan, tmena=tmena, tsea=tsea, tauzpac=tauzpac, tafr=tafr, tlatam=tlatam, y = y)

        elif numchecked == 2:
            firstchk = session["dietary"][0]
            secondchk = session["dietary"][1]
            tindian = {}
            teuropean = {}
            tjkor = {}
            tchinese = {}
            tuscan = {}
            tmena = {}
            tsea = {}
            tauzpac = {}
            tafr = {}
            tlatam = {}
            indian = db.execute("SELECT dish FROM meals JOIN diets ON id = meal_id WHERE dish IN (SELECT dish FROM meals JOIN diets ON id = meal_id WHERE diet = ?) AND diet = ? AND cuisine = 'Indian' ORDER BY random() LIMIT 10", firstchk, secondchk)
            for row in indian:
                x = list(row.values())
                tindian[x[0]] = x[0]
            european = db.execute("SELECT dish FROM meals JOIN diets ON id = meal_id WHERE dish IN (SELECT dish FROM meals JOIN diets ON id = meal_id WHERE diet = ?) AND diet = ? AND cuisine = 'European' ORDER BY random() LIMIT 10", firstchk, secondchk)
            for row in european:
                x = list(row.values())
                teuropean[x[0]] = x[0]
            jkor = db.execute("SELECT dish FROM meals JOIN diets ON id = meal_id WHERE dish IN (SELECT dish FROM meals JOIN diets ON id = meal_id WHERE diet = ?) AND diet = ? AND cuisine = 'Japanese/Korean' ORDER BY random() LIMIT 10", firstchk, secondchk)
            for row in jkor:
                x = list(row.values())
                tjkor[x[0]] = x[0]
            chinese = db.execute("SELECT dish FROM meals JOIN diets ON id = meal_id WHERE dish IN (SELECT dish FROM meals JOIN diets ON id = meal_id WHERE diet = ?) AND diet = ? AND cuisine = 'Chinese' ORDER BY random() LIMIT 10", firstchk, secondchk)
            for row in chinese:
                x = list(row.values())
                tchinese[x[0]] = x[0]
            uscan = db.execute("SELECT dish FROM meals JOIN diets ON id = meal_id WHERE dish IN (SELECT dish FROM meals JOIN diets ON id = meal_id WHERE diet = ?) AND diet = ? AND cuisine = 'U.S./Canada' ORDER BY random() LIMIT 10", firstchk, secondchk)
            for row in uscan:
                x = list(row.values())
                tuscan[x[0]] = x[0]
            mena = db.execute("SELECT dish FROM meals JOIN diets ON id = meal_id WHERE dish IN (SELECT dish FROM meals JOIN diets ON id = meal_id WHERE diet = ?) AND diet = ? AND cuisine = 'Middle Eastern/North African' ORDER BY random() LIMIT 10", firstchk, secondchk)
            for row in mena:
                x = list(row.values())
                tmena[x[0]] = x[0]
            sea = db.execute("SELECT dish FROM meals JOIN diets ON id = meal_id WHERE dish IN (SELECT dish FROM meals JOIN diets ON id = meal_id WHERE diet = ?) AND diet = ? AND cuisine = 'Southeast Asian' ORDER BY random() LIMIT 10", firstchk, secondchk)
            for row in sea:
                x = list(row.values())
                tsea[x[0]] = x[0]
            auzpac = db.execute("SELECT dish FROM meals JOIN diets ON id = meal_id WHERE dish IN (SELECT dish FROM meals JOIN diets ON id = meal_id WHERE diet = ?) AND diet = ? AND cuisine = 'Aus/NZ and Pacific Islands' ORDER BY random() LIMIT 10", firstchk, secondchk)
            for row in auzpac:
                x = list(row.values())
                tauzpac[x[0]] = x[0]
            afr = db.execute("SELECT dish FROM meals JOIN diets ON id = meal_id WHERE dish IN (SELECT dish FROM meals JOIN diets ON id = meal_id WHERE diet = ?) AND diet = ? AND cuisine = 'African' ORDER BY random() LIMIT 10", firstchk, secondchk)
            for row in afr:
                x = list(row.values())
                tafr[x[0]] = x[0]
            latam = db.execute("SELECT dish FROM meals JOIN diets ON id = meal_id WHERE dish IN (SELECT dish FROM meals JOIN diets ON id = meal_id WHERE diet = ?) AND diet = ? AND cuisine = 'Latin American' ORDER BY random() LIMIT 10", firstchk, secondchk)
            for row in latam:
                x = list(row.values())
                tlatam[x[0]] = x[0]
            return render_template("results.html", tindian=tindian, teuropean=teuropean, tjkor=tjkor, tchinese=tchinese, tuscan=tuscan, tmena=tmena, tsea=tsea, tauzpac=tauzpac, tafr=tafr, tlatam=tlatam, y = y)

        elif numchecked == 3:
            firstchk = session["dietary"][0]
            secondchk = session["dietary"][1]
            thirdchk = session["dietary"][2]
            tindian = {}
            teuropean = {}
            tjkor = {}
            tchinese = {}
            tuscan = {}
            tmena = {}
            tsea = {}
            tauzpac = {}
            tafr = {}
            tlatam = {}
            indian = db.execute("SELECT dish FROM meals JOIN diets ON id = meal_id WHERE dish IN (SELECT dish FROM meals JOIN diets ON id = meal_id WHERE dish IN (SELECT dish FROM meals JOIN diets ON id = meal_id WHERE diet = ?) AND diet = ?) AND diet = ? AND cuisine = 'Indian' ORDER BY random() LIMIT 10", firstchk, secondchk, thirdchk)
            for row in indian:
                x = list(row.values())
                tindian[x[0]] = x[0]
            european = db.execute("SELECT dish FROM meals JOIN diets ON id = meal_id WHERE dish IN (SELECT dish FROM meals JOIN diets ON id = meal_id WHERE dish IN (SELECT dish FROM meals JOIN diets ON id = meal_id WHERE diet = ?) AND diet = ?) AND diet = ? AND cuisine = 'European' ORDER BY random() LIMIT 10", firstchk, secondchk, thirdchk)
            for row in european:
                x = list(row.values())
                teuropean[x[0]] = x[0]
            jkor = db.execute("SELECT dish FROM meals JOIN diets ON id = meal_id WHERE dish IN (SELECT dish FROM meals JOIN diets ON id = meal_id WHERE dish IN (SELECT dish FROM meals JOIN diets ON id = meal_id WHERE diet = ?) AND diet = ?) AND diet = ? AND cuisine = 'Japanese/Korean' ORDER BY random() LIMIT 10", firstchk, secondchk, thirdchk)
            for row in jkor:
                x = list(row.values())
                tjkor[x[0]] = x[0]
            chinese = db.execute("SELECT dish FROM meals JOIN diets ON id = meal_id WHERE dish IN (SELECT dish FROM meals JOIN diets ON id = meal_id WHERE dish IN (SELECT dish FROM meals JOIN diets ON id = meal_id WHERE diet = ?) AND diet = ?) AND diet = ? AND cuisine = 'Chinese' ORDER BY random() LIMIT 10", firstchk, secondchk, thirdchk)
            for row in chinese:
                x = list(row.values())
                tchinese[x[0]] = x[0]
            uscan = db.execute("SELECT dish FROM meals JOIN diets ON id = meal_id WHERE dish IN (SELECT dish FROM meals JOIN diets ON id = meal_id WHERE dish IN (SELECT dish FROM meals JOIN diets ON id = meal_id WHERE diet = ?) AND diet = ?) AND diet = ? AND cuisine = 'U.S./Canada' ORDER BY random() LIMIT 10", firstchk, secondchk, thirdchk)
            for row in uscan:
                x = list(row.values())
                tuscan[x[0]] = x[0]
            mena = db.execute("SELECT dish FROM meals JOIN diets ON id = meal_id WHERE dish IN (SELECT dish FROM meals JOIN diets ON id = meal_id WHERE dish IN (SELECT dish FROM meals JOIN diets ON id = meal_id WHERE diet = ?) AND diet = ?) AND diet = ? AND cuisine = 'Middle Eastern/North African' ORDER BY random() LIMIT 10", firstchk, secondchk, thirdchk)
            for row in mena:
                x = list(row.values())
                tmena[x[0]] = x[0]
            sea = db.execute("SELECT dish FROM meals JOIN diets ON id = meal_id WHERE dish IN (SELECT dish FROM meals JOIN diets ON id = meal_id WHERE dish IN (SELECT dish FROM meals JOIN diets ON id = meal_id WHERE diet = ?) AND diet = ?) AND diet = ? AND cuisine = 'Southeast Asian' ORDER BY random() LIMIT 10", firstchk, secondchk, thirdchk)
            for row in sea:
                x = list(row.values())
                tsea[x[0]] = x[0]
            auzpac = db.execute("SELECT dish FROM meals JOIN diets ON id = meal_id WHERE dish IN (SELECT dish FROM meals JOIN diets ON id = meal_id WHERE dish IN (SELECT dish FROM meals JOIN diets ON id = meal_id WHERE diet = ?) AND diet = ?) AND diet = ? AND cuisine = 'Aus/NZ and Pacific Islands' ORDER BY random() LIMIT 10", firstchk, secondchk, thirdchk)
            for row in auzpac:
                x = list(row.values())
                tauzpac[x[0]] = x[0]
            afr = db.execute("SELECT dish FROM meals JOIN diets ON id = meal_id WHERE dish IN (SELECT dish FROM meals JOIN diets ON id = meal_id WHERE dish IN (SELECT dish FROM meals JOIN diets ON id = meal_id WHERE diet = ?) AND diet = ?) AND diet = ? AND cuisine = 'African' ORDER BY random() LIMIT 10", firstchk, secondchk, thirdchk)
            for row in afr:
                x = list(row.values())
                tafr[x[0]] = x[0]
            latam = db.execute("SELECT dish FROM meals JOIN diets ON id = meal_id WHERE dish IN (SELECT dish FROM meals JOIN diets ON id = meal_id WHERE dish IN (SELECT dish FROM meals JOIN diets ON id = meal_id WHERE diet = ?) AND diet = ?) AND diet = ? AND cuisine = 'Latin American' ORDER BY random() LIMIT 10", firstchk, secondchk, thirdchk)
            for row in latam:
                x = list(row.values())
                tlatam[x[0]] = x[0]
            return render_template("results.html", tindian=tindian, teuropean=teuropean, tjkor=tjkor, tchinese=tchinese, tuscan=tuscan, tmena=tmena, tsea=tsea, tauzpac=tauzpac, tafr=tafr, tlatam=tlatam, y = y)

        elif numchecked == 4:
            firstchk = session["dietary"][0]
            secondchk = session["dietary"][1]
            thirdchk = session["dietary"][2]
            fourthchk = session["dietary"][3]
            tindian = {}
            teuropean = {}
            tjkor = {}
            tchinese = {}
            tuscan = {}
            tmena = {}
            tsea = {}
            tauzpac = {}
            tafr = {}
            tlatam = {}
            indian = db.execute("SELECT dish FROM meals JOIN diets ON id = meal_id WHERE dish IN (SELECT dish FROM meals JOIN diets ON id = meal_id WHERE dish IN (SELECT dish FROM meals JOIN diets ON id = meal_id WHERE dish IN (SELECT dish FROM meals JOIN diets ON id = meal_id WHERE diet = ?) AND diet = ?) AND diet = ?) AND diet = ? AND cuisine = 'Indian' ORDER BY random() LIMIT 10", firstchk, secondchk, thirdchk, fourthchk)
            for row in indian:
                x = list(row.values())
                tindian[x[0]] = x[0]
            european = db.execute("SELECT dish FROM meals JOIN diets ON id = meal_id WHERE dish IN (SELECT dish FROM meals JOIN diets ON id = meal_id WHERE dish IN (SELECT dish FROM meals JOIN diets ON id = meal_id WHERE dish IN (SELECT dish FROM meals JOIN diets ON id = meal_id WHERE diet = ?) AND diet = ?) AND diet = ?) AND diet = ? AND cuisine = 'European' ORDER BY random() LIMIT 10", firstchk, secondchk, thirdchk, fourthchk)
            for row in european:
                x = list(row.values())
                teuropean[x[0]] = x[0]
            jkor = db.execute("SELECT dish FROM meals JOIN diets ON id = meal_id WHERE dish IN (SELECT dish FROM meals JOIN diets ON id = meal_id WHERE dish IN (SELECT dish FROM meals JOIN diets ON id = meal_id WHERE dish IN (SELECT dish FROM meals JOIN diets ON id = meal_id WHERE diet = ?) AND diet = ?) AND diet = ?) AND diet = ? AND cuisine = 'Japanese/Korean' ORDER BY random() LIMIT 10", firstchk, secondchk, thirdchk, fourthchk)
            for row in jkor:
                x = list(row.values())
                tjkor[x[0]] = x[0]
            chinese = db.execute("SELECT dish FROM meals JOIN diets ON id = meal_id WHERE dish IN (SELECT dish FROM meals JOIN diets ON id = meal_id WHERE dish IN (SELECT dish FROM meals JOIN diets ON id = meal_id WHERE dish IN (SELECT dish FROM meals JOIN diets ON id = meal_id WHERE diet = ?) AND diet = ?) AND diet = ?) AND diet = ? AND cuisine = 'Chinese' ORDER BY random() LIMIT 10", firstchk, secondchk, thirdchk, fourthchk)
            for row in chinese:
                x = list(row.values())
                tchinese[x[0]] = x[0]
            uscan = db.execute("SELECT dish FROM meals JOIN diets ON id = meal_id WHERE dish IN (SELECT dish FROM meals JOIN diets ON id = meal_id WHERE dish IN (SELECT dish FROM meals JOIN diets ON id = meal_id WHERE dish IN (SELECT dish FROM meals JOIN diets ON id = meal_id WHERE diet = ?) AND diet = ?) AND diet = ?) AND diet = ? AND cuisine = 'U.S./Canada' ORDER BY random() LIMIT 10", firstchk, secondchk, thirdchk, fourthchk)
            for row in uscan:
                x = list(row.values())
                tuscan[x[0]] = x[0]
            mena = db.execute("SELECT dish FROM meals JOIN diets ON id = meal_id WHERE dish IN (SELECT dish FROM meals JOIN diets ON id = meal_id WHERE dish IN (SELECT dish FROM meals JOIN diets ON id = meal_id WHERE dish IN (SELECT dish FROM meals JOIN diets ON id = meal_id WHERE diet = ?) AND diet = ?) AND diet = ?) AND diet = ? AND cuisine = 'Middle Eastern/North African' ORDER BY random() LIMIT 10", firstchk, secondchk, thirdchk, fourthchk)
            for row in mena:
                x = list(row.values())
                tmena[x[0]] = x[0]
            sea = db.execute("SELECT dish FROM meals JOIN diets ON id = meal_id WHERE dish IN (SELECT dish FROM meals JOIN diets ON id = meal_id WHERE dish IN (SELECT dish FROM meals JOIN diets ON id = meal_id WHERE dish IN (SELECT dish FROM meals JOIN diets ON id = meal_id WHERE diet = ?) AND diet = ?) AND diet = ?) AND diet = ? AND cuisine = 'Southeast Asian' ORDER BY random() LIMIT 10", firstchk, secondchk, thirdchk, fourthchk)
            for row in sea:
                x = list(row.values())
                tsea[x[0]] = x[0]
            auzpac = db.execute("SELECT dish FROM meals JOIN diets ON id = meal_id WHERE dish IN (SELECT dish FROM meals JOIN diets ON id = meal_id WHERE dish IN (SELECT dish FROM meals JOIN diets ON id = meal_id WHERE dish IN (SELECT dish FROM meals JOIN diets ON id = meal_id WHERE diet = ?) AND diet = ?) AND diet = ?) AND diet = ? AND cuisine = 'Aus/NZ and Pacific Islands' ORDER BY random() LIMIT 10", firstchk, secondchk, thirdchk, fourthchk)
            for row in auzpac:
                x = list(row.values())
                tauzpac[x[0]] = x[0]
            afr = db.execute("SELECT dish FROM meals JOIN diets ON id = meal_id WHERE dish IN (SELECT dish FROM meals JOIN diets ON id = meal_id WHERE dish IN (SELECT dish FROM meals JOIN diets ON id = meal_id WHERE dish IN (SELECT dish FROM meals JOIN diets ON id = meal_id WHERE diet = ?) AND diet = ?) AND diet = ?) AND diet = ? AND cuisine = 'African' ORDER BY random() LIMIT 10", firstchk, secondchk, thirdchk, fourthchk)
            for row in afr:
                x = list(row.values())
                tafr[x[0]] = x[0]
            latam = db.execute("SELECT dish FROM meals JOIN diets ON id = meal_id WHERE dish IN (SELECT dish FROM meals JOIN diets ON id = meal_id WHERE dish IN (SELECT dish FROM meals JOIN diets ON id = meal_id WHERE dish IN (SELECT dish FROM meals JOIN diets ON id = meal_id WHERE diet = ?) AND diet = ?) AND diet = ?) AND diet = ? AND cuisine = 'Latin American' ORDER BY random() LIMIT 10", firstchk, secondchk, thirdchk, fourthchk)
            for row in latam:
                x = list(row.values())
                tlatam[x[0]] = x[0]
            return render_template("results.html", tindian=tindian, teuropean=teuropean, tjkor=tjkor, tchinese=tchinese, tuscan=tuscan, tmena=tmena, tsea=tsea, tauzpac=tauzpac, tafr=tafr, tlatam=tlatam, y = y)

        elif numchecked == 5:
            firstchk = session["dietary"][0]
            secondchk = session["dietary"][1]
            thirdchk = session["dietary"][2]
            fourthchk = session["dietary"][3]
            fifthchk = session["dietary"][4]
            tindian = {}
            teuropean = {}
            tjkor = {}
            tchinese = {}
            tuscan = {}
            tmena = {}
            tsea = {}
            tauzpac = {}
            tafr = {}
            tlatam = {}

            indian = db.execute("SELECT dish FROM meals JOIN diets ON id = meal_id WHERE dish IN (SELECT dish FROM meals JOIN diets ON id = meal_id WHERE dish IN (SELECT dish FROM meals JOIN diets ON id = meal_id WHERE dish IN (SELECT dish FROM meals JOIN diets ON id = meal_id WHERE dish IN (SELECT dish FROM meals JOIN diets ON id = meal_id WHERE diet = ?) AND diet = ?) AND diet = ?) AND diet = ?) AND diet = ? AND cuisine = 'Indian' ORDER BY random() LIMIT 10", firstchk, secondchk, thirdchk, fourthchk, fifthchk)
            for row in indian:
                x = list(row.values())
                tindian[x[0]] = x[0]
            european = db.execute("SELECT dish FROM meals JOIN diets ON id = meal_id WHERE dish IN (SELECT dish FROM meals JOIN diets ON id = meal_id WHERE dish IN (SELECT dish FROM meals JOIN diets ON id = meal_id WHERE dish IN (SELECT dish FROM meals JOIN diets ON id = meal_id WHERE dish IN (SELECT dish FROM meals JOIN diets ON id = meal_id WHERE diet = ?) AND diet = ?) AND diet = ?) AND diet = ?) AND diet = ? AND cuisine = 'European' ORDER BY random() LIMIT 10", firstchk, secondchk, thirdchk, fourthchk, fifthchk)
            for row in european:
                x = list(row.values())
                teuropean[x[0]] = x[0]
            jkor = db.execute("SELECT dish FROM meals JOIN diets ON id = meal_id WHERE dish IN (SELECT dish FROM meals JOIN diets ON id = meal_id WHERE dish IN (SELECT dish FROM meals JOIN diets ON id = meal_id WHERE dish IN (SELECT dish FROM meals JOIN diets ON id = meal_id WHERE dish IN (SELECT dish FROM meals JOIN diets ON id = meal_id WHERE diet = ?) AND diet = ?) AND diet = ?) AND diet = ?) AND diet = ? AND cuisine = 'Japanese/Korean' ORDER BY random() LIMIT 10", firstchk, secondchk, thirdchk, fourthchk, fifthchk)
            for row in jkor:
                x = list(row.values())
                tjkor[x[0]] = x[0]
            chinese = db.execute("SELECT dish FROM meals JOIN diets ON id = meal_id WHERE dish IN (SELECT dish FROM meals JOIN diets ON id = meal_id WHERE dish IN (SELECT dish FROM meals JOIN diets ON id = meal_id WHERE dish IN (SELECT dish FROM meals JOIN diets ON id = meal_id WHERE dish IN (SELECT dish FROM meals JOIN diets ON id = meal_id WHERE diet = ?) AND diet = ?) AND diet = ?) AND diet = ?) AND diet = ? AND cuisine = 'Chinese' ORDER BY random() LIMIT 10", firstchk, secondchk, thirdchk, fourthchk, fifthchk)
            for row in chinese:
                x = list(row.values())
                tchinese[x[0]] = x[0]
            uscan = db.execute("SELECT dish FROM meals JOIN diets ON id = meal_id WHERE dish IN (SELECT dish FROM meals JOIN diets ON id = meal_id WHERE dish IN (SELECT dish FROM meals JOIN diets ON id = meal_id WHERE dish IN (SELECT dish FROM meals JOIN diets ON id = meal_id WHERE dish IN (SELECT dish FROM meals JOIN diets ON id = meal_id WHERE diet = ?) AND diet = ?) AND diet = ?) AND diet = ?) AND diet = ? AND cuisine = 'U.S./Canada' ORDER BY random() LIMIT 10", firstchk, secondchk, thirdchk, fourthchk, fifthchk)
            for row in uscan:
                x = list(row.values())
                tuscan[x[0]] = x[0]
            mena = db.execute("SELECT dish FROM meals JOIN diets ON id = meal_id WHERE dish IN (SELECT dish FROM meals JOIN diets ON id = meal_id WHERE dish IN (SELECT dish FROM meals JOIN diets ON id = meal_id WHERE dish IN (SELECT dish FROM meals JOIN diets ON id = meal_id WHERE dish IN (SELECT dish FROM meals JOIN diets ON id = meal_id WHERE diet = ?) AND diet = ?) AND diet = ?) AND diet = ?) AND diet = ? AND cuisine = 'Middle Eastern/North African' ORDER BY random() LIMIT 10", firstchk, secondchk, thirdchk, fourthchk, fifthchk)
            for row in mena:
                x = list(row.values())
                tmena[x[0]] = x[0]
            sea = db.execute("SELECT dish FROM meals JOIN diets ON id = meal_id WHERE dish IN (SELECT dish FROM meals JOIN diets ON id = meal_id WHERE dish IN (SELECT dish FROM meals JOIN diets ON id = meal_id WHERE dish IN (SELECT dish FROM meals JOIN diets ON id = meal_id WHERE dish IN (SELECT dish FROM meals JOIN diets ON id = meal_id WHERE diet = ?) AND diet = ?) AND diet = ?) AND diet = ?) AND diet = ? AND cuisine = 'Southeast Asian' ORDER BY random() LIMIT 10", firstchk, secondchk, thirdchk, fourthchk, fifthchk)
            for row in sea:
                x = list(row.values())
                tsea[x[0]] = x[0]
            auzpac = db.execute("SELECT dish FROM meals JOIN diets ON id = meal_id WHERE dish IN (SELECT dish FROM meals JOIN diets ON id = meal_id WHERE dish IN (SELECT dish FROM meals JOIN diets ON id = meal_id WHERE dish IN (SELECT dish FROM meals JOIN diets ON id = meal_id WHERE dish IN (SELECT dish FROM meals JOIN diets ON id = meal_id WHERE diet = ?) AND diet = ?) AND diet = ?) AND diet = ?) AND diet = ? AND cuisine = 'Aus/NZ and Pacific Islands' ORDER BY random() LIMIT 10", firstchk, secondchk, thirdchk, fourthchk, fifthchk)
            for row in auzpac:
                x = list(row.values())
                tauzpac[x[0]] = x[0]
            afr = db.execute("SELECT dish FROM meals JOIN diets ON id = meal_id WHERE dish IN (SELECT dish FROM meals JOIN diets ON id = meal_id WHERE dish IN (SELECT dish FROM meals JOIN diets ON id = meal_id WHERE dish IN (SELECT dish FROM meals JOIN diets ON id = meal_id WHERE dish IN (SELECT dish FROM meals JOIN diets ON id = meal_id WHERE diet = ?) AND diet = ?) AND diet = ?) AND diet = ?) AND diet = ? AND cuisine = 'African' ORDER BY random() LIMIT 10", firstchk, secondchk, thirdchk, fourthchk, fifthchk)
            for row in afr:
                x = list(row.values())
                tafr[x[0]] = x[0]
            latam = db.execute("SELECT dish FROM meals JOIN diets ON id = meal_id WHERE dish IN (SELECT dish FROM meals JOIN diets ON id = meal_id WHERE dish IN (SELECT dish FROM meals JOIN diets ON id = meal_id WHERE dish IN (SELECT dish FROM meals JOIN diets ON id = meal_id WHERE dish IN (SELECT dish FROM meals JOIN diets ON id = meal_id WHERE diet = ?) AND diet = ?) AND diet = ?) AND diet = ?) AND diet = ? AND cuisine = 'Latin American' ORDER BY random() LIMIT 10", firstchk, secondchk, thirdchk, fourthchk, fifthchk)
            for row in latam:
                x = list(row.values())
                tlatam[x[0]] = x[0]
            return render_template("results.html", tindian=tindian, teuropean=teuropean, tjkor=tjkor, tchinese=tchinese, tuscan=tuscan, tmena=tmena, tsea=tsea, tauzpac=tauzpac, tafr=tafr, tlatam=tlatam, y = y)
        else:
            return render_template("invalid.html")

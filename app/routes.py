from app.forms import QueryFileForm, FileDisplayForm, SearchDirectoryForm
from Crawler.crawler_API_lib import map_file_apply, files_from_directory
from flask import render_template
from Crawler.crawler_lib import *
from flask import flash
from app import app
import pandas as pd


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Home Page')


@app.route("/value_search", methods=['GET', 'POST'])
def value_search():
    form = QueryFileForm()
    if form.validate_on_submit():
        filename = form.filename.data
        flash('Congratulations, we\'re searching!!!')
        value = form.value.data
        df = pd.read_csv(filename)
        df = df.query('Value == @value')
        return render_template('view.html', table=df.to_html(), filename=filename)
    return render_template('value_search.html', form=form, title='Value Search')


@app.route("/file_display", methods=['GET', 'POST'])
def file_display():
    form = FileDisplayForm()
    if form.validate_on_submit():
        filename = form.filename.data
        df = pd.read_csv(filename)
        return render_template('view.html', table=df.to_html(), filename=filename)
    return render_template('file_display.html', form=form, title='Home Page')


@app.route("/search_directory", methods=['GET', 'POST'])
def search_directory():
    form = SearchDirectoryForm()
    if form.validate_on_submit():
        directory = form.directory.data

        apply_args = {'pandas_query': f'{form.pandas_query.data}'}

        print(apply_args)

        request = map_file_apply(
            file_list=files_from_directory(directory=directory),
            apply_func=crawler_csv_query,
            apply_func_args={
                'query': f'{form.pandas_query.data}'
            }
        )

        return render_template('view.html', table=request.to_html())
    return render_template('search_directory.html', form=form, title='Home Page')

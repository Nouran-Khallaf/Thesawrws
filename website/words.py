from flask import Blueprint, render_template, request, flash, jsonify
import json
import pandas as pd

#from flask_sqlalchemy import SQLAlchemy

words = Blueprint('words',__name__)
@words.route('/', methods=['GET', 'POST'])
def home():
    
    word = request.args.get('word')
    option = request.args.get('options')
    df = pd.read_csv("./website/data/Data_all.csv", index_col=False)
    subset = df.loc[df.word==word]
    subset = subset[['synset']].style.hide_index()

    if str(option) == 'FastText':
        df = pd.read_csv("./website/data/Fasttext_vectors_pyumsas.csv", index_col=False)
        subset = df.loc[df.Gair==word]
        
        subset = subset[['synset']].style.hide_index()
    elif str(option)== 'Fine-tuned':
        df = pd.read_csv("./website/data/Sk_vectors_pyumsas.csv", index_col=False)
        subset = df.loc[df.Gair==word]
        subset = subset[['synset']].style.hide_index()
    elif str(option) == 'Gold-stanadrd':
        df = pd.read_csv("./website/data/Data_all.csv", index_col=False)
        subset = df.loc[df.word==word]
        if  subset.empty:
            subset = df.loc[df.sense==word]
        subset = subset[['synset']].style.hide_index()
    elif str(option) == 'Dictionary':
        df = pd.read_csv("./website/data/Welsh_wordlist.csv", index_col=False)
        subset = df.loc[df.Gair==word].transpose().dropna()
        if  subset.empty:
            subset = df.loc[df.Saesneg==word].transpose().dropna()
        subset.columns = [ 'synset']
        subset= subset.iloc[2:].style.hide_index()
        #subset = subset[['synset']].style.hide_index()
    else:
        subest=pd.DataFrame()

    return render_template('wordem.html',tables=[subset.to_html(classes='data', header="true")],word=word, options= option)

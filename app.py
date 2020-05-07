from flask import Flask, render_template, request, url_for
from flask_bootstrap import Bootstrap

#NLP
from textblob import TextBlob,Word
import random
import time

app=Flask(__name__)
Bootstrap(app)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/analyse',methods=['POST'])
def analyse():
    if request.method=='POST':
        rawtext=request.form['rawtext']
        choose=request.form['choose']
        blob=TextBlob(rawtext)
        rcv_text2=blob
        if choose=='hindi':
            conv_lang=blob.translate(to='hi')
        elif choose=='arbic':
            conv_lang=blob.translate(to='ar')
        elif choose=='english':
            conv_lang=blob.translate(to='en')
        elif choose=='bengali':
            conv_lang=blob.translate(to='bn')
        elif choose=='chinese':
            conv_lang=blob.translate(to='zh')
        elif choose=='french':
            conv_lang=blob.translate(to='fr')
        elif choose=='german':
            conv_lang=blob.translate(to='de')
        elif choose=='italian':
            conv_lang=blob.translate(to='it')
        elif choose=='japanese':
            conv_lang=blob.translate(to='ja')
        elif choose=='latin':
            conv_lang=blob.translate(to='la')
        elif choose=='nepali':
            conv_lang=blob.translate(to='ne')
        elif choose=='oriya':
            conv_lang=blob.translate(to='or')
        elif choose=='punjabi':
            conv_lang=blob.translate(to='pa')
        elif choose=='Portuguese':
            conv_lang=blob.translate(to='pt')
        elif choose=='Russian':
            conv_lang=blob.translate(to='ru')
        elif choose=='Spanish':
            conv_lang=blob.translate(to='es')
        elif choose=='urdu':
            conv_lang=blob.translate(to='ur')


    return render_template('index.html',rcv_text=rcv_text2,lang=conv_lang)


if __name__ == '__main__':
    app.run(debug=True)
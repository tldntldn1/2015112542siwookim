from flask import Flask, render_template, request, redirect, url_for



a = None
b = None
c = None
cal = None
d= None

app = Flask(__name__)


@app.route('/')
def test():
    return render_template('layout.html')


@app.route('/test')
def memo():
    return render_template('memo.html')


@app.route('/calcul')
def calcul():
    global a
    global b
    global c
    global cal


    if a is not None and b is not None:
        if cal == '+':
            c = str(float(a) + float(b))
        elif cal == '-':
            c = str(float(a) - float(b))
        elif cal == '*':
            c = str(float(a) * float(b))
        elif cal == '/':
            c = str(float(a) / float(b))
        else:
            cal = None
    return render_template('calcul.html', num=a , num2=b, num3=c, cal=cal)

@app.route('/calculate2',methods=['POST'])
def calculate2():
    global a
    global b
    global cal

    if 'plus' in request.form:
        cal = '+'
    elif 'minus' in request.form:
        cal = '-'
    elif 'mul' in request.form:
        cal = '*'
    elif 'div' in request.form:
        cal = '/'
    else:
        cal = None

    if request.method == 'POST':
        if request.form['num']!='' and request.form['num2']!='':
            a = request.form['num']
            b = request.form['num2']
            return redirect(url_for('calcul'))
        else:
            a = request.form['num']
            b = request.form['num2']
            if a =='':
                if b =='':
                    a = None
                    b = None
                else:
                    a = None
            else:
                b = None
            return redirect(url_for('calcul'))


if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)

from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# Oy sayacı değişkenleri
gecerli_oylar = 0
gecersiz_oylar = 0
aday1_oylar = 0
aday2_oylar = 0

okul = None
sandik_no = None

@app.route('/')
def ana_sayfa():
    return render_template('index.html', gecerli_oylar=gecerli_oylar, gecersiz_oylar=gecersiz_oylar, aday1_oylar=aday1_oylar, aday2_oylar=aday2_oylar, okul=okul, sandik_no=sandik_no)

@app.route('/oy_ver', methods=['POST'])
def oy_ver():
    global gecerli_oylar, aday1_oylar, aday2_oylar, gecersiz_oylar

    if request.form['submit_button'] == '1_ekle':
        gecerli_oylar += 1
        aday1_oylar += 1
    elif request.form['submit_button'] == '1_cikar':
        if aday1_oylar > 0:
            gecerli_oylar -= 1
            aday1_oylar -= 1
    elif request.form['submit_button'] == '2_ekle':
        gecerli_oylar += 1
        aday2_oylar += 1
    elif request.form['submit_button'] == '2_cikar':
        if aday2_oylar > 0:
            gecerli_oylar -= 1
            aday2_oylar -= 1
    elif request.form['submit_button'] == 'gecersiz_ekle':
        gecersiz_oylar += 1
    elif request.form['submit_button'] == 'gecersiz_cikar':
        if gecersiz_oylar > 0:
            gecersiz_oylar -= 1
    
    return redirect('/')  # Ana sayfaya yönlendir

@app.route('/sifirla', methods=['POST'])
def sifirla():
    global gecerli_oylar, aday1_oylar, aday2_oylar, gecersiz_oylar
    gecerli_oylar = 0
    aday1_oylar = 0
    aday2_oylar = 0
    gecersiz_oylar = 0
    
    return redirect('/')  # Ana sayfaya yönlendir
@app.route('/okul_sandik', methods=['POST'])
def okul_sandik():
    global okul, sandik_no
    okul = request.form.get('okul')
    sandik_no = request.form.get('sandik_no')
    
    return redirect('/')  # Ana sayfaya yönlendir



if __name__ == '__main__':
    app.run()

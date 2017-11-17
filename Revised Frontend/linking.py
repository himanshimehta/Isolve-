from flask import Flask, redirect, url_for, request, render_template
import model1

app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template("mainpage.html")

@app.route('/success/<name>')
def success(name):
   # g = test.numpy.exp(2)
   op, ans = model1.main_func(name)
   return 'operator is : {} and answer is {}'.format(op, ans)

@app.route('/test',methods = ['POST', 'GET'])
def login():
   if request.method == 'POST':
      user = request.form['qtest']
      return redirect(url_for('success',name = user))
   else:
      user = request.args.get('qtest')
      return redirect(url_for('success',name = user))

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)

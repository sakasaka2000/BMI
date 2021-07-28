from flask import Flask, render_template, request

app = Flask(__name__)


def validation_digit(name, val):
    error_msg = ''
    if not val:
        error_msg = f'{name}を入力してください。'
    elif not val.isdigit():
        error_msg = f'{name}には整数を入力してください。'
    return error_msg


@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        res = {}
        res['height'] = request.form.get('height', '')
        res['weight'] = request.form.get('weight', '')

        res['error_height'] = validation_digit('身長', res['height'])
        res['error_weight'] = validation_digit('体重', res['weight'])

        if not res['error_height'] and not res['error_weight']:
            result = float(res['weight']) / (float(res['height']) / 100) ** 2
            res['result'] = round(result, 2)  # 小数第3位で丸め

        return render_template('index.html', res=res)
    else:
        return render_template('index.html')
if __name__ == "__main__":
    app.run(debug=True)
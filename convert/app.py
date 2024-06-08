from flask import Flask, render_template, request

app = Flask(__name__)

def convert(input_str):
    # 임시로 입력된 문자열을 그대로 반환
    return 'result : ' + input_str

@app.route('/', methods=['GET', 'POST'])
def index():
    text = ""
    result = ""
    if request.method == 'POST':
        text = request.form['input_text']
        result = convert(text)  # 입력된 텍스트를 convert 함수로 변환
    return render_template('index.html', input_text = text, result=result)

if __name__ == '__main__':
    app.run(debug=True)

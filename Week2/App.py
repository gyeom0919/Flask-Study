from flask import Flask, jsonify , render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/app")
def hello():
    return jsonify(text="Hello World!")

hit_count = 0

@app.route("/hits")
def hits():
    global hit_count # 함수 외부에서 선언된 변수를 global 키워드로 재선언하면 접근 가능
    hit_count += 1
    return jsonify(
        text="home",
        count=hit_count
    )


if __name__ == "__main__":
	app.run()
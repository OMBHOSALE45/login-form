from flask import Flask, render_template, request

app=Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/login',methods=["POST"])
def login():
    return render_template("index.html")

# def calculate():
#     try:
#         a =float(request.form.get('a'))
#     except:
#         b=None

#         op=request.form.get('op')
#         result = None
#     error = None

    # try:
    #     if op == "add":
    #         result = a + b
    #     elif op == "sub":
    #         result = a - b
    #     elif op == "mul":
    #         result = a * b
    #     elif op == "div":
    #         if b == 0:
    #             raise ValueError("Division by zero")
    #         result = a / b
    #     elif op == "pow":
    #         result = a ** b
    #     elif op == "sqrt":
    #         if a < 0:
    #             raise ValueError("Square root of negative")
    #         import math
    #         result = math.sqrt(a)
    #     elif op == "percent":
    #         if b is not None:
    #             result = (a / 100) * b
    #         else:
    #             result = a / 100
    #     else:
    #         error = "Invalid Operation"
    # except Exception as e:
    #     error = str(e)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
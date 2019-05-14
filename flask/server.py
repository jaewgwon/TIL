from flask import Flask, render_template, request, jsonify, g
import json
import utilserv as utils
from datetime import timedelta
from flask import make_response, request, current_app
from functools import update_wrapper
import recomm_main as rm
import kmeans as km
import pickle as pk
import os

#귀찮으니까 snippet 복사해서 처리합니다..
def crossdomain(origin=None, methods=None, headers=None, max_age=21600,
                attach_to_all=True, automatic_options=True):
    """Decorator function that allows crossdomain requests.
      Courtesy of
      https://blog.skyred.fi/articles/better-crossdomain-snippet-for-flask.html
    """
    if methods is not None:
        methods = ', '.join(sorted(x.upper() for x in methods))
    # use str instead of basestring if using Python 3.x
    if headers is not None and not isinstance(headers, str):
        headers = ', '.join(x.upper() for x in headers)
    # use str instead of basestring if using Python 3.x
    if not isinstance(origin, str):
        origin = ', '.join(origin)
    if isinstance(max_age, timedelta):
        max_age = max_age.total_seconds()

    def get_methods():
        """ Determines which methods are allowed
        """
        if methods is not None:
            return methods

        options_resp = current_app.make_default_options_response()
        return options_resp.headers['allow']

    def decorator(f):
        """The decorator function
        """
        def wrapped_function(*args, **kwargs):
            """Caries out the actual cross domain code
            """
            if automatic_options and request.method == 'OPTIONS':
                resp = current_app.make_default_options_response()
            else:
                resp = make_response(f(*args, **kwargs))
            if not attach_to_all and request.method != 'OPTIONS':
                return resp

            h = resp.headers
            h['Access-Control-Allow-Origin'] = origin
            h['Access-Control-Allow-Methods'] = get_methods()
            h['Access-Control-Max-Age'] = str(max_age)
            h['Access-Control-Allow-Credentials'] = 'true'
            h['Access-Control-Allow-Headers'] = \
                "Origin, X-Requested-With, Content-Type, Accept, Authorization"
            if headers is not None:
                h['Access-Control-Allow-Headers'] = headers
            return resp

        f.provide_automatic_options = False
        return update_wrapper(wrapped_function, f)
    return decorator

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/groupNumber', methods = ['POST'])
@crossdomain(origin='*')
def recommend_me():
    req_data = request.form.to_dict()
    account_data = req_data['favor']
    gn = rm.groupNumber(account_data)    
    input_data['groupNumber'] = gn
    return json.dumps(input_data)

@app.route('/welcome_data', methods = ['POST'])
@crossdomain(origin='*')
def welcome_data():
    result = request.form.to_dict()
    print(result)
    input_data = [2, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    gn = rm.groupNumber(input_data)
    result['groupNumber'] = gn
    return json.dumps(result)

@app.route('/regist_member', methods = ['POST'])
@crossdomain(origin="*")
def regist_member():
    req_data = request.form.to_dict()
    #req_data를 length 14 배열로 만들어서 TF 요청할 것!
    account_data = req_data['favor']
    for i in range(len(account_data)):
        account_data[i] = int(account_data[i])
    print(account_data)    
    if os.path.isfile('./buffer.dat'):
        f = open('./buffer.dat', 'rb')
        buffer = pk.load(f)
        f.close()
        buffer.append(account_data)
        f = open('./buffer.dat', 'wb')
        pk.dump(buffer, f)
        f.close()
        #여기까진 테스트자료
        print('Buffer 내 자료의 개수 : ', len(buffer))
    else:
        buffer = []
        buffer.append(account_data)
        f = open('./buffer.dat', 'wb')
        pk.dump(buffer, f)
        f.close()
        print('Buffer 내 자료의 개수 : ', len(buffer))
    
    buffer_size = 10 #가지고 있을 취향정보의 buffer 크기. 10이면 계정 10개 가입될때까지 학습 안함.

    if len(buffer) >= buffer_size:
        #버퍼 넘치기 전에 kmeans 소환
        print("Tensorflow re-training 트리거가 작동되었습니다.")
        #km.keeplearning(buffer)
        os.remove('./buffer.dat')
    return json.dumps(account_data)

if __name__ == '__main__':
    app.run()
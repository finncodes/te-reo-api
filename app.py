from flask import Flask, request, Response, jsonify
from utils.dictionary_parser import make_request, get_definitions
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address


app = Flask(__name__)
limiter = Limiter(
    app,
    key_func=get_remote_address
)


@app.route('/')
def root():
    return app.send_static_file('index.html')


@app.route('/definitions', methods=['GET'])
@limiter.limit('1/second')
def definitions():
    keyword = request.args.get("keyword")

    if not keyword:
        return Response(status=400)

    defs = get_definitions(
                make_request(keyword)
            )

    if not defs:
        return Response(status=404)
    else:
        return jsonify(
            {
                "results": defs
            }
        )


if __name__ == '__main__':
    app.run()

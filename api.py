import pickle
import pandas as pd
import re
from sanic.exceptions import ServerError
from sanic import Sanic
from sanic.response import json

app = Sanic(name="predict_news_category")

model = pickle.load(open("model.pkl", 'rb'))
class_names = {
    '5': 'society(사회)',
    '4': 'politics(정치)',
    '3': 'foreign(국제)',
    '2': 'economic(경제)',
    '1': 'digital(IT)',
    '0': 'culture(문화)'
}

def preprocessing(text):
    return re.sub('[^ ㄱ-ㅣ가-힣a-zA-Z]+', '', text)

def _predict(text):
    df = pd.DataFrame({'content': [preprocessing(text)]})
    return model.predict(df['content'])


@app.route('/api/predict', methods=['POST'])
async def predict(request):
    try:
        request_json = request.json
        result_predicts = _predict(request_json['content'])
        print(result_predicts)
        return json({
            'predict_tag': class_names[str(result_predicts[0])]
        })
    except Exception as e:
        print(e)
        raise ServerError(e, status_code=400)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8001, debug=True)


# develop tool content convert : ``.replace(/\"/g, "'").replace(/\n/g, "");
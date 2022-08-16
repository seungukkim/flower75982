
from cgi import parse_multipart
from flask import Flask, request
import json
import start


app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

# 카카오톡 텍스트형 응답
@app.route('/api/sayHello', methods=['POST'])
def sayHello():
    body = request.get_json() # 사용자가 입력한 데이터
    print(body)
    print(body['userRequest']['utterance'])

    responseBody = {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "simpleText": {
                        "text": "안녕 hello I'm Ryan"
                    }
                }
            ]
        }
    }

    return responseBody


# 카카오톡 지역 이름 받아오기
@app.route('/api/whereLive', methods=['POST'])
def whereLive():
    body = request.get_json()
    print(body)

    params_df=body['action']['params']
    print(params_df)
    
    job=params_df['job']
    print(job)
    print(type(job))

    location=params_df['location']
    print(location)

    position=params_df['position']
    [print(position)]

    advantage=params_df['advantage']
    print(advantage)
    print(type(advantage))
    age=json.loads(params_df['sys_number'])['amount']
    print(age)
    advantage1="\'" + advantage +"\'"
    job1="\'%%" + job + "%%\'"
    list1=start.db_select(advantage1,job1)
    print(list1)
    list2=list1[0]
    print(list2)
    print(type(list2))
    # list3=list2[2:-3]
    responseBody = {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                "carousel": {
                "type": "basicCard",
                "items": [
                    {
                    "title": list1[0][2:-62],
                    "description": "장학금 추천",
                    "thumbnail": {
                        "imageUrl": "https://github.com/seungukkim/herokucombinechat79/blob/main/image/a.png?raw=true"
                    },
                    "buttons": [
                        {
                        "action":"webLink",
                        "label": "구경하기",
                        "webLinkUrl": list1[0][-58:-2]
                        },
                        {
                        "action": "share",
                         "label": "공유하기"
                        
                        }
                        
                    ]
                    

                    },

                    {
                    "title": list1[1][2:-62],
                    "description": "장학금 추천",
                    "thumbnail": {
                        "imageUrl": "https://github.com/seungukkim/herokucombinechat79/blob/main/image/b.png?raw=true"
                    },
                    "buttons": [
                        {
                        "action":  "webLink",
                        "label": "구경하기",
                        "webLinkUrl": list1[1][-58:-2]
                        },

                        {
                        "action": "share",
                        "label": "공유하기"                      
                        }
                        
                    ]
                    },
                    {
                    "title": list1[2][2:-62],
                    "description": "장학금 추천",
                    "thumbnail": {
                        "imageUrl": "https://github.com/seungukkim/herokucombinechat79/blob/main/image/c.png?raw=true"
                    },
                    "buttons": [
                         {
                        "action": "webLink",
                        "label": "구경하기",
                        "webLinkUrl": list1[2][-58:-2]
                        },
                        {
                        "action": "share",
                        "label": "공유하기"
                        }
                       
                    ]
                    },
                    {
                    "title": list1[3][2:-62],
                    "description": "장학금 추천",
                    "thumbnail": {
                        "imageUrl": "https://github.com/seungukkim/herokucombinechat79/blob/main/image/b.png?raw=true"
                    },
                    "buttons": [
                        {
                        "action":  "webLink",
                        "label": "구경하기",
                        "webLinkUrl": list1[3][-58:-2]
                        },

                        {
                        "action": "share",
                        "label": "공유하기"                      
                        }
                        
                    ]
                    },
                    {
                    "title": list1[4][2:-62],
                    "description": "장학금 추천",
                    "thumbnail": {
                        "imageUrl": "https://github.com/seungukkim/herokucombinechat79/blob/main/image/b.png?raw=true"
                    },
                    "buttons": [
                        {
                        "action":  "webLink",
                        "label": "구경하기",
                        "webLinkUrl": list1[4][-58:-2]
                        },

                        {
                        "action": "share",
                        "label": "공유하기"                      
                        }
                        
                    ]
                    }
                ]
                }
             }
            ],
            "quickReplies": [
            {
                "messageText": "추가 장학금",
                "action": "message",
                "label": "장학금 더보기"
            }
            
            ]
        }
    }

    return responseBody
  
@app.route('/api/where2Live', methods=['POST'])
def where2Live():
    body = request.get_json()
    print(body)

    params_df=body['action']['params']
    print(params_df)
    
    job=params_df['job1']
    print(job)
    print(type(job))

    location=params_df['location1']
    print(location)

    position=params_df['position1']
    [print(position)]

    advantage=params_df['advantage1']
    print(advantage)
    print(type(advantage))
    age=json.loads(params_df['sys_number1'])['amount']
    print(age)
    advantage1="\'" + advantage +"\'"
    job1="\'%%" + job + "%%\'"
    list1=start.db_select(advantage1,job1)
    responseBody = {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                "carousel": {
                "type": "basicCard",
                "items": [
                    {
                    "title": list1[5][2:-62],
                    "description": "장학금 추천",
                    "thumbnail": {
                        "imageUrl": "https://github.com/seungukkim/herokucombinechat79/blob/main/image/a.png?raw=true"
                    },
                    "buttons": [
                        {
                        "action":"webLink",
                        "label": "구경하기",
                        "webLinkUrl": list1[5][-58:-2]
                        },
                        {
                        "action": "share",
                         "label": "공유하기"
                        
                        }
                        
                    ]
                    

                    },

                    {
                    "title": list1[6][2:-62],
                    "description": "장학금 추천",
                    "thumbnail": {
                        "imageUrl": "https://github.com/seungukkim/herokucombinechat79/blob/main/image/b.png?raw=true"
                    },
                    "buttons": [
                        {
                        "action":  "webLink",
                        "label": "구경하기",
                        "webLinkUrl": list1[6][-58:-2]
                        },

                        {
                        "action": "share",
                        "label": "공유하기"                      
                        }
                        
                    ]
                    },
                    {
                    "title": list1[7][2:-62],
                    "description": "장학금 추천",
                    "thumbnail": {
                        "imageUrl": "https://github.com/seungukkim/herokucombinechat79/blob/main/image/c.png?raw=true"
                    },
                    "buttons": [
                         {
                        "action": "webLink",
                        "label": "구경하기",
                        "webLinkUrl": list1[7][-58:-2]
                        },
                        {
                        "action": "share",
                        "label": "공유하기"
                        }
                       
                    ]
                    },
                    {
                    "title": list1[8][2:-62],
                    "description": "장학금 추천",
                    "thumbnail": {
                        "imageUrl": "https://github.com/seungukkim/herokucombinechat79/blob/main/image/b.png?raw=true"
                    },
                    "buttons": [
                        {
                        "action":  "webLink",
                        "label": "구경하기",
                        "webLinkUrl": list1[8][-58:-2]
                        },

                        {
                        "action": "share",
                        "label": "공유하기"                      
                        }
                        
                    ]
                    },
                    {
                    "title": list1[9][2:-62],
                    "description": "장학금 추천",
                    "thumbnail": {
                        "imageUrl": "https://github.com/seungukkim/herokucombinechat79/blob/main/image/b.png?raw=true"
                    },
                    "buttons": [
                        {
                        "action":  "webLink",
                        "label": "구경하기",
                        "webLinkUrl": list1[9][-58:-2]
                        },

                        {
                        "action": "share",
                        "label": "공유하기"                      
                        }
                        
                    ]
                    }
                ]
                }
             }
            ],
            "quickReplies": [
            {
                "messageText": "추가 장학금1",
                "action": "message",
                "label": "장학금 더보기"
            }
            
            ]
        }
    }

    return responseBody
    
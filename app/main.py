
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



    

# 카카오톡 장학금 받아오기
@app.route('/api/recommend', methods=['POST'])
def recommend():
    body = request.get_json()
    print(body)

    params_df=body['action']['params']
    print(params_df)
    
    job=params_df['job']
    print(job)
    print(type(job))

    location=params_df['location']
    print(location)

    advantage=params_df['advantage']
    print(advantage)
    print(type(advantage))
    age=json.loads(params_df['sys_number'])['amount']
    print(age)

    special = params_df['special']
    print(special)
    advantage1="\'%%" + advantage + "%%\'"
    job1="\'%%" + job + "%%\'"
    special1 = "\'%%" + special + "%%\'"
    location1 = "\'%%" + location + "%%\'"
    list1=start.db_select(advantage1,job1,age,location1,special1)
    len1=len(list1)
    print(len1)
    print(list1)
    list2=list1[0]
    print(list2)
    print(type(list2))
    
    if len1 >= 5:
        responseBody = {
            "version": "2.0",
            "template": {
                "outputs": [
                    {
                        "simpleText": {
                            
                            "text": "검색된 장학금은 총 : {}개 입니다".format(len1)
                        }
                    },
                    {
                    "carousel": {
                    "type": "basicCard",
                    "items": [
                        {
                        "title": list1[0][2:-139],
                        "description": "장학금 추천",
                        "thumbnail": {
                            "imageUrl": list1[0][-75:-2]
                        },
                        "buttons": [
                            {
                            "action":"webLink",
                            "label": "구경하기",
                            "webLinkUrl": list1[0][-135:-79]
                            },
                            {
                            "action": "share",
                            "label": "공유하기"
                        
                            }
                        
                        ]
                    

                        },

                        {
                        "title": list1[1][2:-139],
                        "description": "장학금 추천",
                        "thumbnail": {
                            "imageUrl": list1[1][-75:-2]
                        },
                        "buttons": [
                            {
                            "action":  "webLink",
                            "label": "구경하기",
                            "webLinkUrl": list1[1][-135:-79]
                            },

                            {
                            "action": "share",
                            "label": "공유하기"                      
                            }
                        
                        ]
                        },
                        {
                        "title": list1[2][2:-139],
                        "description": "장학금 추천",
                        "thumbnail": {
                            "imageUrl": list1[2][-75:-2]
                        },
                        "buttons": [
                            {
                            "action": "webLink",
                            "label": "구경하기",
                            "webLinkUrl": list1[2][-135:-79]
                            },
                            {
                            "action": "share",
                            "label": "공유하기"
                            }
                       
                        ]
                        },
                        {
                        "title": list1[3][2:-139],
                        "description": "장학금 추천",
                        "thumbnail": {
                            "imageUrl": list1[3][-75:-2]
                        },
                        "buttons": [
                            {
                            "action":  "webLink",
                            "label": "구경하기",
                            "webLinkUrl": list1[3][-135:-79]
                            },

                            {
                            "action": "share",
                            "label": "공유하기"                      
                            }
                        
                        ]
                        },
                        {
                        "title": list1[4][2:-139],
                        "description": "장학금 추천",
                        "thumbnail": {
                            "imageUrl": list1[4][-75:-2]
                        },
                        "buttons": [
                            {
                            "action":  "webLink",
                            "label": "구경하기",
                            "webLinkUrl": list1[4][-135:-79]
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
    elif len1==1 :
        responseBody = {
            "version": "2.0",
            "template": {
                "outputs": [
                    {
                        "simpleText": {
                        "text": "검색된 장학금은 총 : {}개 입니다".format(len1)
                        }
                    },
                    {
                    "carousel": {
                    "type": "basicCard",
                    "items": [
                        {
                        "title": list1[0][2:-139],
                        "description": "장학금 추천",
                        "thumbnail": {
                            "imageUrl": list1[0][-75:-2]
                        },
                        "buttons": [
                            {
                            "action":"webLink",
                            "label": "구경하기",
                            "webLinkUrl": list1[0][-135:-79]
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
                ]
            }
        }
        return responseBody

    elif len1==2 :
        responseBody = {
            "version": "2.0",
            "template": {
                "outputs": [
                    {
                        "simpleText": {
                        "text": "검색된 장학금은 총 : {}개 입니다".format(len1)
                        }
                    },
                    {
                    "carousel": {
                    "type": "basicCard",
                    "items": [
                        {
                        "title": list1[0][2:-139],
                        "description": "장학금 추천",
                        "thumbnail": {
                            "imageUrl": list1[0][-75:-2]
                        },
                        "buttons": [
                            {
                            "action":"webLink",
                            "label": "구경하기",
                            "webLinkUrl": list1[0][-135:-79]
                            },
                            {
                            "action": "share",
                            "label": "공유하기"                    
                            }                       
                        ]
                        },
                        {
                        "title": list1[1][2:-139],
                        "description": "장학금 추천",
                        "thumbnail": {
                            "imageUrl": list1[1][-75:-2]
                        },
                        "buttons": [
                            {
                            "action":"webLink",
                            "label": "구경하기",
                            "webLinkUrl": list1[1][-135:-79]
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
                ]
            }
        }
        return responseBody
    
    elif len1==3 :
        responseBody = {
            "version": "2.0",
            "template": {
                "outputs": [
                    {
                        "simpleText": {
                        "text": "검색된 장학금은 총 : {}개 입니다".format(len1)
                        }
                    },
                    {
                    "carousel": {
                    "type": "basicCard",
                    "items": [
                        {
                        "title": list1[0][2:-139],
                        "description": "장학금 추천",
                        "thumbnail": {
                            "imageUrl": list1[0][-75:-2]
                        },
                        "buttons": [
                            {
                            "action":"webLink",
                            "label": "구경하기",
                            "webLinkUrl": list1[0][-135:-79]
                            },
                            {
                            "action": "share",
                            "label": "공유하기"                    
                            }                       
                        ]
                        },
                        {
                        "title": list1[1][2:-139],
                        "description": "장학금 추천",
                        "thumbnail": {
                            "imageUrl": list1[1][-75:-2]
                        },
                        "buttons": [
                            {
                            "action":"webLink",
                            "label": "구경하기",
                            "webLinkUrl": list1[1][-135:-79]
                            },
                            {
                            "action": "share",
                            "label": "공유하기"                    
                            }                       
                        ]
                        },
                        {
                        "title": list1[2][2:-139],
                        "description": "장학금 추천",
                        "thumbnail": {
                            "imageUrl": list1[2][-75:-2]
                        },
                        "buttons": [
                            {
                            "action":"webLink",
                            "label": "구경하기",
                            "webLinkUrl": list1[2][-135:-79]
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
                ]
            }
        }
        return responseBody
    
    elif len1==4 :
        responseBody = {
            "version": "2.0",
            "template": {
                "outputs": [
                    {
                        "simpleText": {
                        "text": "검색된 장학금은 총 : {}개 입니다".format(len1)
                        }
                    },
                    {
                    "carousel": {
                    "type": "basicCard",
                    "items": [
                        {
                        "title": list1[0][2:-139],
                        "description": "장학금 추천",
                        "thumbnail": {
                            "imageUrl": list1[0][-75:-2]
                        },
                        "buttons": [
                            {
                            "action":"webLink",
                            "label": "구경하기",
                            "webLinkUrl": list1[0][-135:-79]
                            },
                            {
                            "action": "share",
                            "label": "공유하기"                    
                            }                       
                        ]
                        },
                        {
                        "title": list1[1][2:-139],
                        "description": "장학금 추천",
                        "thumbnail": {
                            "imageUrl": list1[1][-75:-2]
                        },
                        "buttons": [
                            {
                            "action":"webLink",
                            "label": "구경하기",
                            "webLinkUrl": list1[1][-135:-79]
                            },
                            {
                            "action": "share",
                            "label": "공유하기"                    
                            }                       
                        ]
                        },
                        {
                        "title": list1[2][2:-139],
                        "description": "장학금 추천",
                        "thumbnail": {
                            "imageUrl": list1[2][-75:-2]
                        },
                        "buttons": [
                            {
                            "action":"webLink",
                            "label": "구경하기",
                            "webLinkUrl": list1[2][-135:-79]
                            },
                            {
                            "action": "share",
                            "label": "공유하기"                    
                            }                       
                        ]
                        },
                        {
                        "title": list1[3][2:-139],
                        "description": "장학금 추천",
                        "thumbnail": {
                            "imageUrl": list1[3][-75:-2]
                        },
                        "buttons": [
                            {
                            "action":"webLink",
                            "label": "구경하기",
                            "webLinkUrl": list1[3][-135:-79]
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
                ]
            }
        }
        return responseBody
        
        
        

    
        

  
# 장학금 추가로 받아오기 
@app.route('/api/recommen2d', methods=['POST'])
def recommen2d():
    body = request.get_json()
    print(body)

    params_df=body['action']['params']
    print(params_df)
    
    job=params_df['job1']
    print(job)
    print(type(job))

    location=params_df['location1']
    print(location)

    advantage=params_df['advantage1']
    print(advantage)
    print(type(advantage))
    age=json.loads(params_df['sys_number1'])['amount']
    print(age)

    special=params_df['special1']
    [print(special)]

    
    advantage1="\'%%" + advantage + "%%\'"
    job1="\'%%" + job + "%%\'"
    special1 = "\'%%" + special + "%%\'"
    location1 = "\'%%" + location + "%%\'"

    list1=start.db_select(advantage1,job1,age,location1,special1)
    print(list1)
    responseBody = {
  "version": "2.0",
  "template": {
    "outputs": [
      {
        "carousel": {
          "type": "listCard",
          "items": [
            {
              "header": {
                "title": "샌드위치"
              },
              "items": [
                {
                  "title": "햄치즈",
                  "description": "4,500원",
                  "imageUrl": "https://t1.kakaocdn.net/openbuilder/docs_image/02_img_01.jpg"
                },
                {
                  "title": "베이컨 아보카도",
                  "description": "5,500원",
                  "imageUrl": "https://t1.kakaocdn.net/openbuilder/docs_image/02_img_02.jpg"
                },
                {
                  "title": "에그 포테이토",
                  "description": "5,300원",
                  "imageUrl": "https://t1.kakaocdn.net/openbuilder/docs_image/02_img_03.jpg"
                },
                {
                  "title": "갈릭 베이컨 토마토",
                  "description": "5,800원",
                  "imageUrl": "https://t1.kakaocdn.net/openbuilder/docs_image/02_img_04.jpg"
                }
              ],
              "buttons": [
                {
                  "label": "더보기",
                  "action": "message",
                  "messageText" : "샌드위치 더보기"
                }
              ]
            },
            {
              "header": {
                "title": "커피"
              },
              "items": [
                {
                  "title": "아메리카노",
                  "description": "1,800원",
                  "imageUrl": "https://t1.kakaocdn.net/openbuilder/docs_image/02_img_05.jpg"
                },
                {
                  "title": "카페라떼",
                  "description": "2,000원",
                  "imageUrl": "https://t1.kakaocdn.net/openbuilder/docs_image/02_img_06.jpg"
                },
                {
                  "title": "카페모카",
                  "description": "2,500원",
                  "imageUrl": "https://t1.kakaocdn.net/openbuilder/docs_image/02_img_07.jpg"
                },
                {
                  "title": "소이라떼",
                  "description": "2,200원",
                  "imageUrl": "https://t1.kakaocdn.net/openbuilder/docs_image/02_img_08.jpg"
                }
              ],
              "buttons": [
                {
                  "label": "더보기",
                  "action": "message",
                  "messageText" : "커피 더보기"
                }
              ]
            }
          ]
        }
      }
    ],
    "quickReplies": [
      {
        "messageText": "인기 메뉴",
        "action": "message",
        "label": "인기 메뉴"
      },
      {
        "messageText": "최근 주문",
        "action": "message",
        "label": "최근 주문"
      },
      {
        "messageText": "장바구니",
        "action": "message",
        "label": "장바구니"
      }
    ]
  }
}
    return responseBody



# 장학금 추가로 받아오기 
@app.route('/api/recommen3d', methods=['POST'])
def recommen3d():
    body = request.get_json()
    print(body)

    params_df=body['action']['params']
    print(params_df)
    
    job=params_df['job1']
    print(job)
    print(type(job))

    location=params_df['location1']
    print(location)

    advantage=params_df['advantage1']
    print(advantage)
    print(type(advantage))
    age=json.loads(params_df['sys_number1'])['amount']
    print(age)

    special=params_df['special1']
    [print(special)]

    
    advantage1="\'%%" + advantage + "%%\'"
    job1="\'%%" + job + "%%\'"
    special1 = "\'%%" + special + "%%\'"
    location1 = "\'%%" + location + "%%\'"

    list1=start.db_select(advantage1,job1,age,location1,special1)
    print(list1)
    responseBody = {
        "version": "2.0",
        "template": {
            "outputs": [
            {
                "carousel": {
                "type": "listCard",
                "items": [
                    {
                    "header": {
                        "title": "장학금 더보기"
                    },
                    "items": [
                        {
                        "title": list1[5][2:-139],
                        
                        "imageUrl": list1[5][-75:-2],
                        "action":"webLink",
                        "webLinkUrl": list1[5][-135:-79]
                        },
                        {
                        "title": list1[6][2:-139],
                        
                        "imageUrl": list1[6][-75:-2],
                        "action":"webLink",
                        "webLinkUrl": list1[6][-135:-79]
                        },
                        {
                        "title": list1[7][2:-139],
                        
                        "imageUrl": list1[7][-75:-2],
                        "action":"webLink",
                        "webLinkUrl": list1[7][-135:-79]
                        },
                        {
                        "title": list1[8][2:-139],
                        
                        "imageUrl": list1[8][-75:-2],
                        "action":"webLink",
                        "webLinkUrl": list1[8][-135:-79]
                        },
                        {
                        "title": list1[9][2:-139],
                        
                        "imageUrl": list1[9][-75:-2],
                        "action":"webLink",
                        "webLinkUrl": list1[9][-135:-79]
                        }
                        ],
                        "buttons": [
                        {
                        "label": "더보기",
                        "action": "message",
                        "messageText" : "더보기1"
                        }
                    ]
                    }
                ]
                }
            }
            ]
        }
        }
    return responseBody

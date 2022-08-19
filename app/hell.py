list1=[1,2,3,4,5]
responseBody = {
            "version": "2.0",
            "template": {
                "outputs": [
                    {
                    "carousel": {
                    "type": "basicCard",
                    "items": [
                        {"title":for i in range(5)}
                        {
                        "title": list1[0],         
                        }, 
                        {
                        "title": list1[1],     
                        },
                        {
                        "title": list1[2],
                        },
                        {
                        "title": list1[3],
                        },
                        {
                        "title": list1[4],
                        }
                    ]
                    }
                }
                ]
            }
        }

def hi(i):
    s= {"title":list1[i]}
    return s
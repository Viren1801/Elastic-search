from nltk.corpus import stopwords
import nltk

nltk.download('stopwords')
import elasticsearch

client = elasticsearch.Elasticsearch()
word_list = "green chilli with beef chicken".split()
filtered_words = [word for word in word_list if word not in stopwords.words('english')]
original_word = ' '.join(filtered_words)
print(original_word)

"settings": {
 "analysis": {
   "normalizer": {
     "my_normalizer": {
       "type": "custom",
       "filter": ["lowercase"]
     }
   }
 }
query = {
"query": {
        "fuzzy":{
            "title.keyword": original_word
        }
     }

}

ret = client.search(body=query, index="nin_v2")
    # print(ret["hits"]["hits"])
hits = ret["hits"]["hits"]
for i in hits:
    result = i["_source"]["title"], i["_score"]
    print(result)

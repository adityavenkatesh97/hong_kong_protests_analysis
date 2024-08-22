''' Output tweets/dictionary data to json file'''

output_json = json.dumps(tweetsByDate)
output_json = json.loads(output_json)
# print(tweetsByDate[0])

with open('tweetsByDate.json', 'w') as outfile:
    json.dump(output_json, outfile)


''' Get all unique users(tweet authors)'''

x = set()
for key in tweetsByDate.keys():
    #l = []
    tweeter = tweetsByDate[key]["user"]["screen_name"]
    x=x.union({tweeter})

x

''' To run the gephi code on a sample'''
import random

indices= [i for i in range(len(nodes))]
randomIndices = random.sample(indices,1000)

subsetMatrix = mat[randomIndices][:, randomIndices]

X = nx.from_numpy_matrix(subsetMatrix)

X.edges(data=True)


to_del = [n for n in X if X.degree(n) == 0]
X.remove_nodes_from(to_del)

# H=nx.relabel_nodes(G,mapping)
pos_fr = nx.fruchterman_reingold_layout(X)

plt.figure()

nx.draw(X,pos=pos_fr,width=1, node_size=5, node_color='c', with_labels=False)
#print(H.nodes())
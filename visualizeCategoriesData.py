from sklearn.decomposition import PCA
import json
import matplotlib.pyplot as plt
import matplotlib
import numpy as np

colors = [
    'b',
    'g',
    'r',
    'm',
    'k',
    'y'
]

categories = [
    "Results interpretation",
    "Frameworks usage",
    "Algorithms design",
    "Algorithms implementation",
    "Launching problem",
    "Performance issue",
]

allCategories = {}

for x in categories:
    allCategories[x] = []

jsonFile = open("embeddingData.json", "r+")
data = json.load(jsonFile)
jsonFile.close()

"""
points = []

for x in data:
    points.append(data[x]["embedding"])

points = np.array(pca.fit_transform(points))

x = []
y = []
z = []

for bruh in points:
    x.append(bruh[0])
    y.append(bruh[1])
    z.append(bruh[2])

"""
def performPCA(data):

    pca = PCA(n_components = 3)
    points = []

    for x in data:
        points.append(data[x]["embedding"])

    points = np.array(pca.fit_transform(points))
    for x in range(len(points)):
        data[str(x)]["embedding"] = points[x]
    return data

data = performPCA(data)

fig = plt.figure(figsize=(4,4))
ax = fig.add_subplot(111, projection='3d')

#print(allCategories)
for x in data:
    dataEmbedding = data[x]["embedding"]
    problemCategory = data[x]["labels"][1].split(", ")[0]
    #print(developmentStage, problemCategory)
    curPoints = allCategories[problemCategory]
    curPoints.append(dataEmbedding)

#print(allCategories)

index = 0
for a in allCategories:
    points = allCategories[a]
    x = []
    y = []
    z = []
    for bruh in points:
        x.append(bruh[0])
        y.append(bruh[1])
        z.append(bruh[2])
    ax.scatter3D(x, y, z,cmap='plasma', color=colors[index])
    print(a,":",colors[index])
    index += 1

#ax.scatter3D(x, y, z)
plt.show()
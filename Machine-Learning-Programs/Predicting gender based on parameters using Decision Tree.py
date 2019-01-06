from sklearn import tree

#[height, weight, shoe size]
X=[[181,70,44], [177,70,43], [160, 60, 38], [154,54,37],
	[166,65,40], [190,90,47], [175,64,39], [177,70,40],[159,55,37],
	[171,75,42], [181,85,43]]

#labels corresponding to the values above
Y=['male', 'female', 'female', 'female', 'male', 'male',
	'male', 'female', 'male', 'female', 'male']

#storing decision tree model
clf=tree.DecisionTreeClassifier()

#training the set
clf=clf.fit(X,Y)

#prediction of the data
prediction=clf.predict([[190,70,43]])

print(prediction)
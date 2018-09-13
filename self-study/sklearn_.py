from sklearn import neighbors, datasets, preprocessing
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
iris = datasets.load_iris()
X, y = iris.data[:, :2], iris.target
#从sklearn.cross_validation模块导入train_test_split 函数，用于训练集和测试集的划分，cross_validation即交叉验证
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=123)
scaler = preprocessing.StandardScaler().fit(X_train)#数据标准化https://blog.csdn.net/csmqq/article/details/51461696
X_train = scaler.transform(X_train)
X_test = scaler.transform(X_test)
knn = neighbors.KNeighborsClassifier(n_neighbors=5)
knn.fit(X_train, y_train)
y_pred = knn.predict(X_test)
print('accuracy:%s'%accuracy_score(y_test, y_pred))
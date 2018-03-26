class Just_SKLearn():
    from sklearn.datasets import load_iris
    from sklearn import tree

    clf = tree.DecisionTreeClassifier()
    iris = load_iris()

    clf = clf.fit(iris.data, iris.target)
    tree.export_graphviz(clf,
    out_file='tree.dot')

    '''$ dot -Tpng tree.dot -o tree.png    (PNG format)'''


class With_Pydotplus():
    import sklearn.datasets as datasets
    import pandas as pd
    iris=datasets.load_iris()
    df=pd.DataFrame(iris.data, columns=iris.feature_names)
    y=iris.target

    from sklearn.tree import DecisionTreeClassifier
    dtree=DecisionTreeClassifier()
    dtree.fit(df,y)

    from sklearn.externals.six import StringIO
    from IPython.display import Image
    from sklearn.tree import export_graphviz
    import pydotplus
    dot_data = StringIO()
    export_graphviz(dtree, out_file=dot_data,
                    filled=True, rounded=True,
                    special_characters=True)
    graph = pydotplus.graph_from_dot_data(dot_data.getvalue())
    Image(graph.create_png())

class From_Textbook():
    import matplotlib.pyplot as plt

    decisionNode = dict(boxstyle="sawtooth", fc="0.8")
    leafNode = dict(boxstyle="round4", fc="0.8")
    arrow_args = dict(arrowstyle="<-")

    def plotNode(nodeTxt, centerPt, parentPt, nodeType):
        createPlot.ax1.annotate(nodeTxt, xy=parentPt,
        xycoords='axes fraction',
        xytext=centerPt, textcoords='axes fraction',
        va="center", ha="center", bbox=nodeType, arrowprops=arrow_args)

    def plotMidText(cntrPt, parentPt, txtString):
        xMid = (parentPt[0]-cntrPt[0])/2.0 + cntrPt[0]
        yMid = (parentPt[1]-cntrPt[1])/2.0 + cntrPt[1]
        createPlot.ax1.text(xMid, yMid, txtString)
    def plotTree(myTree, parentPt, nodeTxt):
        numLeafs = getNumLeafs(myTree)
        getTreeDepth(myTree)
        firstStr = myTree.keys()[0]
        cntrPt = (plotTree.xOff + (1.0 + float(numLeafs))/2.0/plotTree.totalW,\
        plotTree.yOff)
        plotMidText(cntrPt, parentPt, nodeTxt)
        plotNode(firstStr, cntrPt, parentPt, decisionNode)
        secondDict = myTree[firstStr]
        plotTree.yOff = plotTree.yOff - 1.0/plotTree.totalD
        for key in secondDict.keys():
            if type(secondDict[key]).__name__=='dict':
                plotTree(secondDict[key],cntrPt,str(key))
            else:
                plotTree.xOff = plotTree.xOff + 1.0/plotTree.totalW
                plotNode(secondDict[key], (plotTree.xOff, plotTree.yOff),
                cntrPt, leafNode)
                plotMidText((plotTree.xOff, plotTree.yOff), cntrPt, str(key))
        plotTree.yOff = plotTree.yOff + 1.0/plotTree.totalD
    def createPlot(inTree):
        fig = plt.figure(1, facecolor='white')
        fig.clf()
        axprops = dict(xticks=[], yticks=[])
        createPlot.ax1 = plt.subplot(111, frameon=False, **axprops)
        plotTree.totalW = float(getNumLeafs(inTree))
        plotTree.totalD = float(getTreeDepth(inTree))
        plotTree.xOff = -0.5/plotTree.totalW; plotTree.yOff = 1.0;
        plotTree(inTree, (0.5,1.0), '')
        plt.show()

    def retrieveTree(i):
        listOfTrees =[{'no surfacing': {0: 'no', 1: {'flippers': \
        {0: 'no', 1: 'yes'}}}},
        {'no surfacing': {0: 'no', 1: {'flippers': \
        {0: {'head': {0: 'no', 1: 'yes'}}, 1: 'no'}}}}
        ]
        return listOfTrees[i]

    def getNumLeafs(myTree):
        numLeafs = 0
        firstStr = myTree.keys()[0]
        secondDict = myTree[firstStr]
        for key in secondDict.keys():
            if type(secondDict[key]).__name__=='dict':
            numLeafs += getNumLeafs(secondDict[key])
            else: numLeafs +=1
        return numLeafs

    def getTreeDepth(myTree):
        maxDepth = 0
        firstStr = myTree.keys()[0]
        secondDict = myTree[firstStr]
        for key in secondDict.keys():
            if type(secondDict[key]).__name__=='dict':
                thisDepth = 1 + getTreeDepth(secondDict[key])
            else: thisDepth = 1
            if thisDepth > maxDepth: maxDepth = thisDepth
        return maxDepth

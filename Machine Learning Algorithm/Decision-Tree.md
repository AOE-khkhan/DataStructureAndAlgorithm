# Decision Tree
> Decision Tree is non-parametric supervised machine learning algorithm used for classification and regression.

Decesion Tree have some advantage and disadvantage

## Advantages
- Simple to understand and to interpret. Trees can be visualised.
- Reqiure little data preparation. other techniques often require data normalisation, dummy variable need to be created and blank values to be removed. However this module also does not supoprt missing values.
- The cost of using tree is logarithmic in the number of data points used to train the tree.
- Able to handle multi output and categorial and numerical values.
- Possible to validate a model using statistical tests.That makes it possible to account for reliability of the model.

## Disadvantages
- Decision tree learners can create over- complex trees.
- Decesion tree tends to overfit the model that result in poor test data performance.
- Decision tree can be unstable because small varations in the data might result in completely differnt being generated.
- Decision tree learners create biased trees if some classes dominate. It is therefore recommended to balance the dataset prior to fitting with the decision tree.
- There are concepts that are hard to learn because decision trees do not express them easily, such as XOR, parity or multiplexer problem.

## Importance Point For Decision Tree
- Decision Tree tend to overfit on data with a large number of features.Getting the right ratio of samples to number of features is important, since a tree with few samples in high dimensional space is very likely to overfit.
-Consider performing dimensionality Like  (**PCA** **ICA** **Feature Selection**) to give your tree a better chance of finding features that are discimnative.
-Understanding the decision tree structure will help in gaining more insights about how the decision tree makes predictions, which is important for understandingthe importance feature in data.
- Visualise your tree as you are training by using export function.Use `max_depth=3` as an initial tree depth to get a feel for how the treeis fitting to your data, and then increase the depth.
from sklearn import tree
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import CountVectorizer

from src.models.base_model import BaseModel

class DecisionTreeModel(BaseModel):
    def __init__(self, **kwargs):
        super().__init__(
            model=Pipeline([
                ('countv', CountVectorizer()),
                ('dt', tree.DecisionTreeClassifier(**kwargs))
            ])
        )
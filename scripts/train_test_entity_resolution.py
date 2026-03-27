from ds_project.merged_data import MergedData
from ds_project.entity_resolution_features import EntityResolutionFeatures
from classifiers.resolution_classifier import EntityResolutionClassifier


def train():
    # Add your training data here
    erc = entity_resolution_classifier.EntityResolutionClassifier()
    erc.train(features, labels)
    erc.save("data/erc.model")


def test():
    erc = entity_resolution_classifier.EntityResolutionClassifier()
    erc.load("data/erc.model")

    feature_model = entity_resolution_features.EntityResolutionFeatures()
    md = merged_data.MergedData()  # From the database!
    for batch in md.get_merged_data():
        features = feature_model.features(batch)
        is_match = erc.predict(features)

        # To the database!
import json
from sklearn.metrics import cohen_kappa_score
import numpy as np

def conduct_majority_vote(annotations):
    aggregation = np.median(annotations, axis=0)
    aggregation[aggregation > 0.0] = 1.0
    aggregation = aggregation.astype("int")
    return list(aggregation)


def load_annotations(label, method):
    assert label in {"participants", "interventions", "outcomes"}
    assert method in {"baseline", "expert", "senbase", "sensupport"}
    with open('./data/annotations/{}_{}.json'.format(label, method)) as json_file:
        return json.load(json_file)


def aggregate_annotations(annotations):
    aggregated_annotations = []
    for senid in sorted(annotations.keys()):
        anns = annotations[senid]['annotations']
        aggregated_annotations.extend(conduct_majority_vote(anns))
    return aggregated_annotations


def main():
    print("Cohen's Kappa scores to the gold standard labels")
    print("===================================")
    for label in ["participants", "interventions", "outcomes"]:
        ann_expert = load_annotations(label, "expert")
        agg_expert = aggregate_annotations(ann_expert)  # gold standard label
        for method in ["baseline", "senbase", "sensupport"]:
            ann = load_annotations(label, method)
            agg = aggregate_annotations(ann)
            assert len(agg) == len(agg_expert)  # Should have same length
            kappa = cohen_kappa_score(agg, agg_expert)
            print("Cohen's Kappa Score", label, method, "{:.3f}".format(kappa))
        print()


if __name__ == "__main__":
    main()

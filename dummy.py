from typing import List, Dict, Tuple
from sparsezoo import Model

"latency: 'item/sec'"



def extract_metric_from_validation_results(name, validation_results):

    if name == "acc":
        # acc
        extract_accuracy(validation_results)
    # latency

    # throughput
    pass


def extract_metrics(candidate: Model, optimizing_metrics: List[str]):
    return {
        optimizing_metric: extract_metric_from_validation_results(
            optimizing_metric, candidate.eval_results
        )
        for optimizing_metric in optimizing_metrics
    }

def filter_candidates(candidates, optimizing_metrics):
    new_candidates = []
    for candidate in candidates:
        for optimizing_metric in optimizing_metrics:
            try:
                extract_metric_from_validation_results(optimizing_metric, candidate.eval_results)
            except:
                continue
            new_candidates.append(candidate)
    return new_candidates

def get_best_model(candidates: List[Model], optimizing_metrics: List[str]) -> Model:
    # :pre cond: all optimizing_metrics should be relevant;

    candidates = filter_candidates(candidates, optimizing_metrics)
    extracted_metrics_for_candidates: Dict[Model, Dict[str, float]] = [
        extract_metrics(candidate, optimizing_metrics)
        for candidate in candidates
    ]
    metric_ranges: Dict[str, Tuple[float, float]] = extract_ranges(
        extracted_metrics_for_candidates
    )

    heuristic_for_candidates: List[float] = [
        compute_heuristics(metrics, metric_ranges)
        for metrics in extracted_metrics_for_candidates
    ]

    return max(range(len(candidates)), key=lambda i: heuristic_for_candidates[i])

def compute_heuristics(
    metrics: Dict[str, float], ranges: Dict[str, Tuple[float, float]]
):
    total = 0.0
    for metric_name, value in metrics.items():
        low, high = ranges[metric_name]
        new_value = (value - low) / (high - low)
        assert 0.0 <= new_value <= 1.0
        if metric_name in MINIMIZABLE_METRICS:
            new_value *= -1
        # LATENCY should be: `-new_value`
        # ACCURACY should be: `new_value`
        total += new_value
    return total

"""
accuracy -> acc, top1 acc
"""

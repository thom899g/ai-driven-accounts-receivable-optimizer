def apply_business_rules(predictions, business_rules):
    """
    Applies business rules to AI predictions.
    Args:
        predictions (list): Predicted optimal invoice times.
        business_rules (dict): Business rule thresholds.
    Returns:
        list: Adjusted decisions based on rules.
    """
    adjusted = []
    for pred in predictions:
        if pred < business_rules['earliestInvoice']:
            adjusted_pred = business_rules['earliestInvoice']
        elif pred > business_rules['latestInvoice']:
            adjusted_pred = business_rules['latestInvoice']
        else:
            adjusted_pred = pred
        adjusted.append(adjusted_pred)
    return adjusted
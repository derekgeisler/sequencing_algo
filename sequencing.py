def evaluate_priority_case(case):
    """
    Evaluates a case for special interest group formation based on specified criteria
    Returns: priority_level (int), reasoning (str)
    """
    def assess_base_criteria(case):
        unity_score = case.get('unity_metric', 0)
        respect_score = case.get('respect_metric', 0)
        return (unity_score + respect_score) / 2

    def is_exceptional_case(case):
        luck_factor = case.get('luck_coefficient', 0)
        ingenuity_score = case.get('ingenuity_metric', 0)
        
        LUCK_THRESHOLD = 0.95  # Represents 95th percentile of lucky events
        INGENUITY_THRESHOLD = 9.0  # On a 10-point scale
        
        return luck_factor > LUCK_THRESHOLD or ingenuity_score > INGENUITY_THRESHOLD

    def assess_revolutionary_impact(case):
        phase_impact = case.get('phase_impact', 0)
        directive_impact = case.get('directive_impact', 0)
        return max(phase_impact, directive_impact)

    # Main prioritization logic
    priority_level = 0
    reasoning = []

    # Step 1: Check for exceptional cases first
    if is_exceptional_case(case):
        priority_level = 3
        reasoning.append("Exceptional case detected: Bypassing standard criteria")
        return priority_level, "; ".join(reasoning)

    # Step 2: Evaluate base criteria
    base_score = assess_base_criteria(case)
    if base_score >= 0.8:
        priority_level = 2
        reasoning.append("High unity and respect scores")
    elif base_score >= 0.5:
        priority_level = 1
        reasoning.append("Moderate unity and respect scores")
    
    # Step 3: Adjust for revolutionary impact
    impact_score = assess_revolutionary_impact(case)
    if impact_score > 0.7:
        priority_level += 1
        reasoning.append("Significant potential impact on phases/directives")

    return priority_level, "; ".join(reasoning)

def form_interest_group(cases):
    """
    Forms special interest groups based on prioritized cases
    Returns: list of prioritized cases with assigned groups
    """
    prioritized_cases = []
    
    for case in cases:
        priority, reasoning = evaluate_priority_case(case)
        case['priority'] = priority
        case['reasoning'] = reasoning
        prioritized_cases.append(case)
    
    # Sort by priority level descending
    prioritized_cases.sort(key=lambda x: x['priority'], reverse=True)
    
    return prioritized_cases

"""
Fuzzy System Logic

Problem - Rank applicants

-- Variables
        Input
            applicant's experience
        Output
            score
"""
import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

def get_total_score(ratings_list):
    final_score = 0.0
    list_length = len(ratings_list)
    for num in ratings_list:
        score_num = get_fuzzy_score(int(num), (100/list_length))
        final_score += score_num
    return final_score

def get_fuzzy_score(exp, max_score):
    # DECLARE Antecedent objects (hold universe input variables)
    expertise = ctrl.Antecedent(np.arange(0, 11, 1), 'expertise')

    # DECLARE Consequent objects (hold universe output variables)
    score = ctrl.Consequent(np.arange(0.0, max_score, 0.1), 'score')

    # DECLARE Membership function for Antecedent
    expertise['nov'] = fuzz.trimf(expertise.universe, [0, 0, 5])
    expertise['int'] = fuzz.trimf(expertise.universe, [0, 5, 10])
    expertise['pro'] = fuzz.trimf(expertise.universe, [5, 10, 10])

    # autogenerate mebership function for Consequent
    score.automf(3)

    # DEFINE fuzzy relationship between input and output variables
    rule_exptse_nov = ctrl.Rule(expertise['nov'] , score['poor'])
    rule_exptse_int = ctrl.Rule(expertise['int'] , score['average'])
    rule_exptse_pro = ctrl.Rule(expertise['pro'] , score['good'])

    score_ctrl = ctrl.ControlSystem([rule_exptse_nov, rule_exptse_int, rule_exptse_pro])
    scoring = ctrl.ControlSystemSimulation(score_ctrl)

    scoring.input['expertise'] = exp

    # Crunch the numbers
    scoring.compute()

    return scoring.output['score']

class FuzzyScore:

    def __init__(self):
        pass

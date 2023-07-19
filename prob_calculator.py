import random
# (2 * 1 * 4 * 8) / (11 * 10 * 9 * 8)

class Hat:

    def __init__(self, **key_value_arguments):
        if len(key_value_arguments) < 1:
            raise ValueError # which exception fits?
        self.contents = []
        for key, value in key_value_arguments.items():
            for count_index in range(value):
                self.contents.append(key)

    def draw(self, number_balls_to_draw):
        if number_balls_to_draw > len(self.contents):
            return self.contents
        else:
            balls_drawn = []
            while number_balls_to_draw > 0:
                random_ball = random.choice(self.contents)
                self.contents.remove(random_ball)
                balls_drawn.append(random_ball)
                number_balls_to_draw -= 1
            return balls_drawn

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    '''
    hat: A hat object containing balls that should be copied inside the function.
    expected_balls: An object indicating the exact group of balls to attempt to draw from the hat for the experiment. For example, to determine the probability of drawing 2 blue balls and 1 red ball from the hat, set expected_balls to {"blue":2, "red":1}.
    num_balls_drawn: The number of balls to draw out of the hat in each experiment.
    num_experiments: The number of experiments to perform. (The more experiments performed, the more accurate the approximate probability will be.)
    '''
    hat_contents_as_dict = list_of_balls_to_dictionary_of_color_occurrences(hat.contents)
    num_experiments_remaining = num_experiments
    number_times_outcome_meets_expected_balls = 0
    while num_experiments_remaining > 0:
        hat_for_experiment = Hat(**hat_contents_as_dict)
        outcome = hat_for_experiment.draw(num_balls_drawn)
        if outcome_meets_expected_balls(outcome, expected_balls):
            number_times_outcome_meets_expected_balls += 1
        num_experiments_remaining -= 1
    probability_estimated = (number_times_outcome_meets_expected_balls / num_experiments)
    return probability_estimated

def list_of_balls_to_dictionary_of_color_occurrences(list_of_balls):
    ball_color_occurrence_count_dict = dict()
    for ball in list_of_balls:
        ball_color_occurrence_count_dict[ball] = ball_color_occurrence_count_dict.get(ball, 0) + 1
    return ball_color_occurrence_count_dict

def outcome_meets_expected_balls(outcome, expected_balls):
    # outcome is list of balls, e.g. ['blue', 'blue', 'red']
    outcome_as_dictionary_of_color_occurences = list_of_balls_to_dictionary_of_color_occurrences(outcome)
    for ball_color, occurrence_count in expected_balls.items():
        if occurrence_count > outcome_as_dictionary_of_color_occurences.get(ball_color, 0):
            return False
    return True

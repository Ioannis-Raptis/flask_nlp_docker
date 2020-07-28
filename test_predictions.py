from predict import make_prediction

assert make_prediction(
    ['hate horrible']) == 'The tweet has a negative sentiment'

assert make_prediction(['happy love roses happy']
                       ) == 'The tweet has a positive sentiment'

assert make_prediction(['I love life']
                       ) == 'The tweet has a positive sentiment'

assert make_prediction(['Your service was horrible, never again']
                       ) == 'The tweet has a negative sentiment'

from collections import defaultdict


class Person:
    def __init__(self, badge):
        self.badge = badge
        self.name = "Name"
        self.ratings = [5, 5, 5, 5]  # TODO: double check it's covered
        self.ratings_total = float(0)
        self.magnitudes = list()
        self.weights = list()
        self.scores = defaultdict(set)
        self.preferences = list()

    def setRatings(self, category, rating):
        for i in range(len(self.ratings)):
            self.ratings[category] = float(rating)

    def setRatingsTotal(self):
        for i in self.ratings:
            self.ratings_total += float(i)

    def setMagnitudes(self, MEDIAN, SIZE):
        for i in range(SIZE):
            self.magnitudes.append(abs(self.ratings[i] - MEDIAN))

    def setWeights(self, SIZE):
        for i in range(SIZE):
            self.weights.append(self.magnitudes[i] / self.ratings_total)

    # pass in (multi_data[i], SIZE)
    def calculateScore(self, other_person, SIZE):
        _scores = list()
        for j in range(SIZE):
            _scores.append(other_person[j+1] * self.weights[j])
        # returns value to be used in dict(other_person: total_score)
        return sum(_scores)

    def setScores(self, multi_data, SIZE):
        # iterate through ALL managers/DP's (aka "other_person")
        for i in range(len(multi_data)):
            _name = multi_data[i][0]       # record #i, field 0 is Name
            # field is sum(multi_data[i][1:])
            _final_score = self.calculateScore(multi_data[i], SIZE)
            self.scores[_name] = _final_score

    def setPreferences(self, multi_data, SIZE):
        # converts scores into sorted list
        self.preferences = sorted(self.scores.items(), key=lambda x: x[1])

    def getPreferences(self):
        _tmp = list()
        for i in self.preferences:
            _tmp.append(i[0])
        return _tmp

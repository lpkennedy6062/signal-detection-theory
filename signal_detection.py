import scipy.stats as stats

class SignalDetection:
    def __init__(self, hits, misses, false_alarms, correct_rejections):
        self.hits = hits
        self.misses = misses
        self.false_alarms = false_alarms
        self.correct_rejections = correct_rejections

    def hit_rate(self):
        if (self.hits + self.misses) == 0:
            return 0  # Avoid division by zero
        return self.hits / (self.hits + self.misses)

    def false_alarm_rate(self):
        if (self.false_alarms + self.correct_rejections) == 0:
            return 0  # Avoid division by zero
        return self.false_alarms / (self.false_alarms + self.correct_rejections)

    def d_prime(self):
        H = self.hit_rate()
        FA = self.false_alarm_rate()
        
        # Clip values between 0.01 and 0.99 to avoid infinite z-scores
        H = min(max(H, 0.01), 0.99)
        FA = min(max(FA, 0.01), 0.99)

        return stats.norm.ppf(H) - stats.norm.ppf(FA)

    def criterion(self):
        H = self.hit_rate()
        FA = self.false_alarm_rate()

        # Clip values to avoid extreme cases
        H = min(max(H, 0.01), 0.99)
        FA = min(max(FA, 0.01), 0.99)

        return -0.5 * (stats.norm.ppf(H) + stats.norm.ppf(FA))

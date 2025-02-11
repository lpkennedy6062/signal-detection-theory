from signal_detection import SignalDetection

def main():
    sd = SignalDetection(hits=50, misses=10, false_alarms=5, correct_rejections=35)

    print("Hit Rate:", sd.hit_rate())
    print("False Alarm Rate:", sd.false_alarm_rate())
    print("d-prime:", sd.d_prime())
    print("Criterion:", sd.criterion())

if __name__ == "__main__":
    main()

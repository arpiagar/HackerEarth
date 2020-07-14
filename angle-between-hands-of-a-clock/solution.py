i#https://leetcode.com/problems/angle-between-hands-of-a-clock/submissions/


class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        hour_clock_degree_per_hour = 30
        minute_clock_degree_per_hour = 360
        per_minute_angle_for_minute_hand = 360/60
        per_minute_angle_for_hour_hand = 30/60

        offset_minute_hand = minutes*per_minute_angle_for_minute_hand
        offset_hour_hand = hour_clock_degree_per_hour*hour + minutes*per_minute_angle_for_hour_hand
        diff = abs(offset_minute_hand-offset_hour_hand)
        return min(diff,360-diff)


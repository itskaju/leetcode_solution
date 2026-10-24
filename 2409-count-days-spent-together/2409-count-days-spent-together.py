class Solution:
    def countDaysTogether(
        self,
        arriveAlice: str,
        leaveAlice: str,
        arriveBob: str,
        leaveBob: str
    ) -> int:
        days_in_months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        def day_number(date):
            month, day = map(int, date.split("-"))
            return sum(days_in_months[:month - 1]) + day

        alice_arrival = day_number(arriveAlice)
        alice_leave = day_number(leaveAlice)
        bob_arrival = day_number(arriveBob)
        bob_leave = day_number(leaveBob)

        start = max(alice_arrival, bob_arrival)
        end = min(alice_leave, bob_leave)

        if start > end:
            return 0

        return end - start + 1
import unittest
from bowling import compute_game_score  # make sure bowling.py is in same folder

class TestComputeGameScoreEdgeCases(unittest.TestCase):

    # ---------- Open frames ----------
    def test_all_gutter(self):
        frames = [(0, 0)] * 10
        self.assertEqual(compute_game_score(frames), 0)

    def test_all_ones(self):
        frames = [(1, 1)] * 10
        self.assertEqual(compute_game_score(frames), 20)

    # ---------- Spares ----------
    def test_all_spares_five_five(self):
        frames = [(5, 5)] * 10 + [(5, 0)]  # bonus frame
        self.assertEqual(compute_game_score(frames), 150)

    def test_spare_followed_by_open(self):
        frames = [(7, 3), (4, 2)] + [(0, 0)] * 8
        expected = 14 + 6
        self.assertEqual(compute_game_score(frames), expected)

    def test_spare_followed_by_strike(self):
        frames = [(9, 1), (10, 0)] + [(0, 0)] * 8
        expected = 20 + 10
        self.assertEqual(compute_game_score(frames), expected)

    # ---------- Strikes ----------
    def test_single_strike(self):
        frames = [(10, 0), (3, 4)] + [(0, 0)] * 8
        expected = 17 + 7
        self.assertEqual(compute_game_score(frames), expected)

    def test_double_strike_then_open(self):
        frames = [(10, 0), (10, 0), (4, 2)] + [(0, 0)] * 7
        expected = 24 + 16 + 6
        self.assertEqual(compute_game_score(frames), expected)

    def test_strike_then_spare(self):
        frames = [(10, 0), (7, 3)] + [(0, 0)] * 8 + [(0, 0)]
        expected = 20 + 10
        self.assertEqual(compute_game_score(frames), expected)

    def test_strike_strike_spare(self):
        frames = [(10, 0), (10, 0), (7, 3)] + [(0, 0)] * 7 + [(0, 0)]
        expected = 27 + 20 + 10
        self.assertEqual(compute_game_score(frames), expected)

    # ---------- Perfect game ----------
    def test_perfect_game(self):
        frames = [(10, 0)] * 10 + [(10, 0), (10, 0)]
        self.assertEqual(compute_game_score(frames), 300)

    # ---------- Tenth frame scenarios ----------
    def test_tenth_frame_strike_one_bonus(self):
        frames = [(0, 0)] * 9 + [(10, 0)] + [(7, 0)]
        expected = 17
        self.assertEqual(compute_game_score(frames), expected)

    def test_tenth_frame_strike_two_bonus(self):
        frames = [(0, 0)] * 9 + [(10, 0)] + [(10, 0), (10, 0)]
        expected = 30
        self.assertEqual(compute_game_score(frames), expected)

    def test_tenth_frame_spare_with_bonus(self):
        frames = [(0, 0)] * 9 + [(7, 3)] + [(9, 0)]
        expected = 19
        self.assertEqual(compute_game_score(frames), expected)

    def test_tenth_frame_open(self):
        frames = [(0, 0)] * 9 + [(4, 5)]
        expected = 9
        self.assertEqual(compute_game_score(frames), expected)

    # ---------- Edge cases ----------
    def test_first_frame_strike_last_frame_spare(self):
        frames = [(10, 0), (4, 3)] + [(0, 0)] * 7 + [(7, 3)] + [(5, 0)]
        self.assertEqual(compute_game_score(frames), 39)

    def test_strikes_and_spares_last_three_frames(self):
        # Frame 8: X, Frame 9: 7/ , Frame 10: X + bonus 10,10
        frames = [(0,0)]*7 + [(10,0), (7,3), (10,0), (10,0), (10,0)]
        # Frame 8: 10 + next two rolls (7+3)=20
        # Frame 9: 10 + next roll (10)=20
        # Frame10: 10 + next two rolls (10+10)=30
        expected = 20 + 20 + 30
        self.assertEqual(compute_game_score(frames), expected)

    def test_all_gutter_with_strike_bonus_last_frame(self):
        frames = [(0,0)]*9 + [(10,0)] + [(0,0),(0,0)]
        expected = 10
        self.assertEqual(compute_game_score(frames), expected)


if __name__ == "__main__":
    unittest.main()


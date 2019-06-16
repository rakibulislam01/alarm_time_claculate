import unittest

from AlarmTime import DetectDate


class TestAlarmTime(unittest.TestCase):

    def setUp(self):
        self.alarm = DetectDate()

    def test_correct_date_sentence(self):
        alarm = self.alarm.date_time_detect('detect the date on December 16')
        time_now = alarm.year, alarm.month, alarm.day, alarm.hour
        self.assertEqual((2019, 12, 16, 12), time_now)

    def test_correct_date_after_days(self):
        alarm = self.alarm.date_time_detect('after 700 days')
        time_now = alarm.year, alarm.month, alarm.day, alarm.hour
        self.assertEqual((2021, 5, 16, 14), time_now)

    def test_correct_date_millisecond(self):
        self.assertNotEqual('2019, 12, 16, 0, 0, 0, 487288',
                            self.alarm.date_time_detect('detect the date on December 16'))
    #
    # def test_correct_date_sentence(self):
    #     self.assertNotEqual('2019, 12, 16, 0, 0, 0, 487288',
    #                         self.alarm.date_time_detect('detect the date on December 16'))


class TestGetDifferentTime(unittest.TestCase):

    def setUp(self):
        self.different = DetectDate()

    def test_day_different(self):
        self.assertEqual(1.0, self.different.day_diff_from_now('after 1 days'))

    def test_hour_different(self):
        self.assertEqual(24.0, self.different.hour_diff_from_now('after 1 days'))
        self.assertEqual(0.0, self.different.hour_diff_from_now(''))

    def test_minute_different(self):
        self.assertEqual(1440.0, self.different.minute_diff_from_now('after 1 days'))
        self.assertEqual(0.0, self.different.minute_diff_from_now(''))

    def test_second_different(self):
        self.assertEqual(0.0, self.different.second_diff_from_now(''))
        self.assertEqual(86400.0, self.different.second_diff_from_now('after 1 days'))
        self.assertEqual(0.0, self.different.second_diff_from_now('after days'))

    # def test_millisecond_different(self):
    #     self.assertEqual(1.0, self.different.millisecond_diff_from_now('after 1 days'))


if __name__ == '__main__':
    unittest.main()

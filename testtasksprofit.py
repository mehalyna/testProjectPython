import pytest

from task_test import tasks


class TestTasksProfit:

    @pytest.mark.parametrize("test_input,expected",
                             [
                                 ({"cost_price": 32.67, "sell_price": 45.00, "inventory": 1200}, 14796),
                                 ({"cost_price": 225.89, "sell_price": 550.00, "inventory": 100}, 32411),
                                 ({"cost_price": 2.77, "sell_price": 7.95, "inventory": 8500}, 44030)

                             ])
    def test_profit_nonempty_dict(self, test_input, expected):
        """

        :type expected: object
        """
        assert tasks.profit(test_input) == expected

    def test_profit_empty_dict(self):
        assert tasks.profit({}) == 0

    @pytest.mark.parametrize("test_input, expected",
                             [
                                 ({"cost_price": -32.67, "sell_price": 45.00, "inventory": 1200}, 0),
                                 ({"cost_price": 225.89, "sell_price": -550.00, "inventory": 100}, 0),
                                 ({"cost_price": 2.77, "sell_price": 7.95, "inventory": -8500}, 0)

                             ])
    def test_profit_negative_numbers_dict(self, test_input, expected):
        assert tasks.profit(test_input) == expected

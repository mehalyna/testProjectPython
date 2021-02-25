from task_test import tasks


class TestTasksQuadraticSolutions:
    def test_quadratic_solutions_one_root(self):
        assert tasks.quadratic_solutions(1, 2, 1) == 1

    def test_quadratic_solutions_zero_root(self):
        assert tasks.quadratic_solutions(3, 1, 3) == 0

    def test_quadratic_solutions_two_roots(self):
        assert tasks.quadratic_solutions(3, 10, 3) == 2

import timeit
from typing import Any, Callable, Annotated


def test_time(func: Callable[..., Any]) -> Callable[..., Any]:
    def check_time_work_func(*args: Any, **kwargs: Any) -> Any:
        general_result: float = 0.0

        for i in range(100):
            start_time: float = timeit.default_timer()
            func(*args, **kwargs)
            end_time: float = timeit.default_timer()

            elapsed_time: float = end_time - start_time
            general_result += elapsed_time

        average: float = (general_result / 100) * 1000000
        print(f"{average:.5f} микросекунд - время выполнения функции {func.__name__}")

        result: Any = func(*args, **kwargs)
        return result

    return check_time_work_func

from communication.reindeer import Reindeer


class SantaCommunicator:
    def __init__(self, number_of_days_to_rest: int) -> None:
        self.number_of_days_to_rest = number_of_days_to_rest

    def compose_message(
        self,
        reindeer: Reindeer,
        number_of_days_before_christmas: int,
    ) -> str:
        days_before_return = self._days_before_return(
            reindeer.number_of_days_for_coming_back, number_of_days_before_christmas
        )
        return f"Dear {reindeer.name}, please return from {reindeer.current_location} in {days_before_return} day(s) to be ready and rest before Christmas."

    def is_overdue(
        self,
        reindeer: Reindeer,
        number_of_days_before_christmas: int,
        logger,
    ) -> bool:
        if (
            self._days_before_return(
                reindeer.number_of_days_for_coming_back,
                number_of_days_before_christmas,
            )
            <= 0
        ):
            logger.log(
                f"Overdue for {reindeer.name} located {reindeer.current_location}."
            )
            return True
        return False

    def _days_before_return(
        self, numbers_of_days_for_coming_back: int, number_of_days_before_christmas: int
    ) -> int:
        return (
            number_of_days_before_christmas
            - numbers_of_days_for_coming_back
            - self.number_of_days_to_rest
        )

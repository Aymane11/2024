from typing import Optional

MIN = 1
MAX = 100


class FizzBuzz:
    divisors = {
        3: "Fizz",
        5: "Buzz",
        7: "Whizz",
        11: "Bang",
    }

    @staticmethod
    def convert(input_num: int) -> Optional[str]:
        if FizzBuzz.is_out_of_range(input_num):
            return None
        else:
            return FizzBuzz.convert_safely(input_num)

    @staticmethod
    def convert_safely(input_num: int) -> str:
        output = ""
        for divisor in FizzBuzz.divisors:
            if FizzBuzz.operator(divisor, input_num):
                output += FizzBuzz.divisors[divisor]

        if output == "":
            return str(input_num)
        else:
            return output

    @staticmethod
    def operator(divisor: int, input_num: int) -> bool:
        return input_num % divisor == 0

    @staticmethod
    def is_out_of_range(input_num: int) -> bool:
        return input_num < MIN or input_num > MAX

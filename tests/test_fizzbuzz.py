import fizzbuzz

def test_return_buzz():
  result = fizzbuzz.fizzbuzz(5)
  assert result == "Buzz"

def test_return_fizz():
  assert fizzbuzz.fizzbuzz(12) == "Fizz"

def test_return_fizzbuzz():
  assert fizzbuzz.fizzbuzz(15) == "FizzBuzz"

def test_return_number():
  assert fizzbuzz.fizzbuzz(23) == 23
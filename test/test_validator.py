from guardrails import Guard
from validator import CorrectLanguage

# Create a pydantic model with a field that uses the custom validator
guard = Guard.from_string(
    validators=[CorrectLanguage(expected_language_iso="en", threshold=0.75)]
)


# Test happy path
def test_happy_path():
    response = guard.parse("The hospital is located in the heart of the city.")
    assert(response.validation_passed)


# Test fail path
def test_fail_path():
    res = guard.parse(
        "Das Krankenhaus befindet sich im Herzen der Stadt. Wir haben auch ein Restaurant und eine Bar."
    )
    print(res)
    assert not res.validation_passed
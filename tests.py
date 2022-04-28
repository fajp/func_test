"""
Tests function provided as var {TESTED_FUNC}
"""

import json
import func


# function you want to be tested:
TESTED_FUNC = func.unique_substr_len


def test_func(to_test: func, io_path: str) -> bool:
    """
    Tests function and returns True if no error occurs.
    Returns False otherwise.

    params:
        to_test: function to be tested
        io_path: path to json with exprected io
    """

    ios = json.load(open(io_path, 'r'))

    all_ok = True
    for io in ios:
        output = to_test(io['in'])
        if output == io['out']:
            print(f"{io['desc']}: OK")
        else:
            print(
                f"{io['desc']}: ERROR"
                f"(output: {output}, expected: {io['out']})"
            )
            all_ok = False

    return all_ok

final_result = 'Final result: '
if test_func(TESTED_FUNC, 'io.json'):
    final_result += 'All tests passed OK'
else:
    final_result += 'Errors encountered'

print()
print(final_result)

import sys
import json
import func


def test_func(func_: func, io_path: str) -> bool:
    ios = json.load(open(io_path, 'r'))

    all_ok = True
    for io in ios:
        output = func_(io['in'])
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
if test_func(func.unique_substr_len, 'io.json'):
    final_result += 'All tests passed OK'
else:
    final_result += 'Errors encountered'

print()
print(final_result)

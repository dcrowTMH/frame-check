from frame_check_core import FrameChecker
from frame_check_core.models.diagnostic import Diagnostic, Severity
from frame_check_core.models.region import CodeRegion


def test_conditional_column_assignment():
    code = """
import pandas as pd
df = pd.DataFrame({"a": [1, 2, 3], "b": [4, 5, 6]})
condition = True
if condition:
    df["c"] = [7, 8, 9]
"""
    fc = FrameChecker.check(code)
    assert fc.diagnostics == [
        Diagnostic(
            column_name="c",
            message="Column 'c' exists only if the statement in line 4 is evaluated as True",
            severity=Severity.WARNING,
            region=CodeRegion.from_tuples(
                start=(6, 4),
                end=(6, 22),
            ),
            hint=[],
            definition_region=CodeRegion.from_tuples(
                start=(3, 0),
                end=(3, 48),
            ),
        )
    ]

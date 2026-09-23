# Change CHG 104

Fictional training input. Meridian Support routes tickets using priorities P0 to P3. Input currently arrives in inconsistent case and with stray whitespace. Silent conversion of bad data to P3 hides problems.

Change only src/priority.py. Keep the public function name normalise_priority and its single input argument. Return the canonical uppercase priority for a string that becomes P0, P1, P2 or P3 after stripping surrounding whitespace and converting case. Raise ValueError for every other value, including non-strings. Do not add dependencies or change the tests to make them pass.

Acceptance examples: "p1" becomes "P1"; "  P2\n" becomes "P2"; " p0 " becomes "P0"; "urgent", "P4", empty text, None, booleans and numbers raise ValueError. Internal spaces remain invalid. Preserve all four already valid priorities.

Provide a proposed plan, the change, actual test output, changed-file list and remaining risks. A human reviewer decides whether the patch meets these criteria. Do not claim a deployment or merge.

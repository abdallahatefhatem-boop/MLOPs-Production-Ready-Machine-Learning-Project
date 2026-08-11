import pandas as pd
import json
from evidently import Report
from evidently.metrics import DatasetDriftMetric

ref = pd.DataFrame({"a": [1, 2, 3], "b": [4, 5, 6]})
cur = pd.DataFrame({"a": [1, 5, 6], "b": [7, 8, 9]})

report = Report(metrics=[DatasetDriftMetric()])
snapshot = report.run(reference_data=ref, current_data=cur)
json_report = json.loads(snapshot.json())

with open("scratch_report.json", "w") as f:
    json.dump(json_report, f, indent=4)

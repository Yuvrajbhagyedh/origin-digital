import pandas as pd
from io import StringIO

data = '{"employee_name":"James","email":"james@gmail.com","job_profile":[{"title1":"Team Lead"}]}'

df = pd.read_json(StringIO(data))

print(df)
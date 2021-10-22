import json
import os


config_filepath = "airflow_sandbox/dag_config/"
dag_template_filename = "airflow_sandbox/dag_template.py"

for filename in os.listdir(config_filepath):
    print(filename)
    f = open(config_filepath + filename)
    config = json.load(f)

    new_filename = (
        "dags/dynamic_dags_multiple_files/" + config["DagId"] + ".py"
    )

    with open(dag_template_filename, "r") as template:
        with open(new_filename, "w+") as dag_file:
            for line in template.readlines():
                line = line.replace("dag_id_placeholder", config["DagId"])
                line = line.replace("schedule_placeholder", config["Schedule"])
                dag_file.write(line)

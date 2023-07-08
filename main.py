from fastapi import FastAPI, Body
from yaml_parse import parse
from search import search_all_dependencies
import json

app = FastAPI()
tasks = parse("build/tasks.yaml", "tasks")
builds = parse("build/builds.yaml", "build")


@app.post("/get_tasks")
def hello(data=Body()):
    try:
        build_name = data["build"]
        all_list = list()
        for task in builds[build_name]:
            all_list.extend(search_all_dependencies(task, tasks))
        answer = {"ans": all_list}
        str_json = json.dumps(answer)
        return json.loads(str_json)
    except KeyError:
        return "data error"

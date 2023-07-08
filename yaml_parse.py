import yaml


def parse(file_path, mode):
    with open(file_path, 'r') as file:
        try:
            yaml_data = yaml.safe_load(file)
            if mode == "tasks":
                tasks_dict = dict()
                for data in yaml_data["tasks"]:
                    name = data["name"]
                    dependencies = data["dependencies"]
                    tasks_dict[name] = dependencies
                return tasks_dict
            else:
                build_dict = dict()
                for data in yaml_data["builds"]:
                    name = data["name"]
                    tasks = data["tasks"]
                    build_dict[name] = tasks
                return build_dict
        except yaml.YAMLError as exc:
            print("Ошибка при загрузке файла YAML:", exc)
            exit(0)

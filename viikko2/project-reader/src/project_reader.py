import toml
from urllib import request
from project import Project


class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")
        print("Raw content:")
        print(content)

        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        parsed_data = toml.loads(content)
        print("Parsed content:")
        print(parsed_data)

        name = parsed_data.get("tool").get("poetry").get("name")
        description = parsed_data.get("tool").get("poetry").get("description")
        license = parsed_data.get("tool").get("poetry").get("license")
        authors = parsed_data.get("tool").get("poetry").get("authors")
        dependencies = parsed_data.get("tool").get("poetry").get("dependencies")
        development_dependencies = parsed_data.get("tool").get("poetry").get("group").get("dev").get("dependencies")

        

        return Project(name, description, license, authors, dependencies, development_dependencies)

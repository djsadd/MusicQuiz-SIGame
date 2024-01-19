import xml.etree.ElementTree as ET

package = ET.Element("package")
package.attrib['name'] = "Вопросы SIGame"
package.attrib['version'] = "5"
package.attrib['id'] = "23d4d970-5e37-49fb-9cc7-80675f5f6754"
package.attrib['date'] = "17.01.2024"
package.attrib['difficulty'] = "5"
package.attrib['xmlns'] = "https://github.com/VladimirKhil/SI/blob/master/assets/siq_5.xs"


# info
info = ET.SubElement(package, "info")
authors = ET.SubElement(info, "authors")
author = ET.SubElement(authors, "author")
author.text = "Лушань"
tree = ET.ElementTree(package)


# Rounds

rounds = ET.SubElement(package, "rounds")
# round = ET.SubElement(rounds, "round")
# themes = ET.SubElement(round, "themes")
# theme = ET.SubElement(themes, "theme")
# questions = ET.SubElement(theme, "questions")
# question = ET.SubElement(questions, "question")
# params = ET.SubElement(question, "params")
# param = ET.SubElement(params, "param")
# item = ET.SubElement(param, "item")
# item.text = "MUSIC"
# right = ET.SubElement(question, "right")
# answer = ET.SubElement(right, "answer")
# answer.text = "ANSWER"


class Generate:
    def __init__(self, rounds_quantity, songs):
        self.rounds = []
        self.songs = songs
        self.tech_theme = None

    def create_question(self):
        pass

    def create_theme(self, rnd):
        for row in self.rounds:
            if row[0] == rnd:
                break

    def create_round(self, name):
        rnd = ET.SubElement(rounds, "round")
        rnd.attrib["name"] = name
        themes = ET.SubElement(rnd, "themes")
        self.rounds.append([rnd, themes])
        return rnd


with open("example.xml", "wb") as file:
    tree.write(file, encoding="utf-8", xml_declaration=True)

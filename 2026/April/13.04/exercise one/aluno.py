from dataclasses import dataclass, field

from disciplina import subject


@dataclass
class student:
    name: str
    subjects: dict[str, subject] = field(default_factory=dict)

    def add_subject(self, subject_name, modules):
        if subject_name not in self.subjects:
            self.subjects[subject_name] = subject(subject_name)
        self.subjects[subject_name].add_modules(modules)

    def add_grade(self, subject_name, module_name, grade):
        subject_item = self.subjects.get(subject_name)
        if not subject_item:
            return False
        return subject_item.add_grade(module_name, grade)

    def subject_average(self, subject_name):
        subject_item = self.subjects.get(subject_name)
        if not subject_item:
            return None
        return subject_item.average()

    def overall_average(self):
        averages = [item.average() for item in self.subjects.values() if item.average() is not None]
        if not averages:
            return None
        return sum(averages) / len(averages)

    def to_dict(self):
        return {
            "name": self.name,
            "subjects": {name: item.to_dict() for name, item in self.subjects.items()},
        }

    @classmethod
    def from_dict(cls, data):
        item = cls(name=data["name"])
        raw_subjects = data.get("subjects", {})
        for name, subject_data in raw_subjects.items():
            item.subjects[name] = subject.from_dict(subject_data)
        return item

from __future__ import annotations

from dataclasses import dataclass, field

from disciplina import subject


@dataclass
class student:
    name: str
    subjects: dict[str, subject] = field(default_factory=dict)

    def add_subject(self, subject_name: str, modules: list[str]) -> None:
        if subject_name not in self.subjects:
            self.subjects[subject_name] = subject(subject_name)
        self.subjects[subject_name].add_modules(modules)

    def add_grade(self, subject_name: str, module_name: str, grade: float) -> bool:
        subject_item = self.subjects.get(subject_name)
        if not subject_item:
            return False
        return subject_item.add_grade(module_name, grade)

    def subject_average(self, subject_name: str) -> float | None:
        subject_item = self.subjects.get(subject_name)
        if not subject_item:
            return None
        return subject_item.average()

    def overall_average(self) -> float | None:
        averages = [item.average() for item in self.subjects.values() if item.average() is not None]
        if not averages:
            return None
        return sum(averages) / len(averages)

    def to_dict(self) -> dict:
        return {
            "name": self.name,
            "subjects": {name: item.to_dict() for name, item in self.subjects.items()},
        }

    @classmethod
    def from_dict(cls, data: dict) -> "student":
        item = cls(name=data["name"])
        raw_subjects = data.get("subjects", {})
        for name, subject_data in raw_subjects.items():
            item.subjects[name] = subject.from_dict(subject_data)
        return item

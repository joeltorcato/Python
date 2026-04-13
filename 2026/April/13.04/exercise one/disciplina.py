from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class subject:
    name: str
    modules: dict[str, float | None] = field(default_factory=dict)

    def add_modules(self, modules: list[str]) -> None:
        for module in modules:
            module_name = module.strip()
            if module_name and module_name not in self.modules:
                self.modules[module_name] = None

    def add_grade(self, module_name: str, grade: float) -> bool:
        if module_name not in self.modules:
            return False
        self.modules[module_name] = grade
        return True

    def average(self) -> float | None:
        grades = [grade for grade in self.modules.values() if grade is not None]
        if not grades:
            return None
        return sum(grades) / len(grades)

    def to_dict(self) -> dict:
        return {
            "name": self.name,
            "modules": self.modules,
        }

    @classmethod
    def from_dict(cls, data: dict) -> "subject":
        item = cls(name=data["name"])
        item.modules = data.get("modules", {})
        return item

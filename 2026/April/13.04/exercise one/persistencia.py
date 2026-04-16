import json
from pathlib import Path

from aluno import student


def load_students(file_path):
    path = Path(file_path)
    if not path.exists():
        return {}

    content = path.read_text(encoding="utf-8").strip()
    if not content:
        return {}

    data = json.loads(content)
    return {name: student.from_dict(student_data) for name, student_data in data.items()}


def save_students(file_path, students):
    path = Path(file_path)
    data = {name: item.to_dict() for name, item in students.items()}
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")

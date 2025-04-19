import yaml
from typing import List, Optional
from pydantic import BaseModel, ValidationError, Field


class Rule(BaseModel):
    id: str
    description: str
    condition: str
    risk_score: int = Field(ge=0, le=100)
    enabled: bool
    priority: int

def load_rules(path: str="rules.yaml") -> List[Rule]:
    with open(path, "r", encoding="utf-8") as file:
        data = yaml.safe_load(file)
    return [Rule(**rule) for rule in data.get("rules", [])]
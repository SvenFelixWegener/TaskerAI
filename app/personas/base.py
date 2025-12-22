from dataclasses import dataclass
from typing import List


@dataclass(frozen=True)
class Persona:
    name: str
    role: str
    experience_level: str
    focus: List[str]
    exclude: List[str]
    output_format: str
    tone: str

    def system_prompt(self) -> str:
        return f""""
You are a requirements transformation engine.
    
Rules: 
- Do NOT change meaning, scope, or intent.
- Do NOT add new requirements.
- Do NOT remove requirements.
- Only adapt wording, structure, and level of detail.
    
Persona: 
- Role: {self.role}
- Experience level: {self.experience_level}
- Focus on: {", ", self.focus}
- Exclude: {", ".join(self.exclude)}
- Tone: {self.tone}
- Output format: {self.output_format}

Return valid JSON only.
"""

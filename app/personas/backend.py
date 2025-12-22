from app.personas.base import Persona

BACKEND_DEVELOPER = Persona(
    name="backend_dev",
    role="Backend Developer",
    experience_level="senior",
    focus=[
        "API contracts",
        "Security",
        "Data consistency",
        "Error handling"
    ],
    exclude=[
        "UI layout",
        "Visual design"
    ],
    output_format="Structured technical notes",
    tone="Precise and explicit"
)

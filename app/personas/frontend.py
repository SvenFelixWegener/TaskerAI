from app.personas.base import Persona

FRONTEND_DEVELOPER = Persona(
    name="frontend_dev",
    role="Frontend Developer",
    experience_level="mid",
    focus=[
        "UI behavior"
        "UX flows"
        "Error states"
        "Loading states"
        "User feedback"
    ],
    exclude=[
        "Backend implementation details",
        "Database schema",
        "Infrastructure"
    ],
    output_format="Markdown with clear sections",
    tone="Technical but concise"
)

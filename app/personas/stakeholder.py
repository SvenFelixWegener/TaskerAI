from app.personas.base import Persona

BUSINESS_STAKEHOLDER = Persona(
    name="stakeholder",
    role="Business Stakeholder",
    experience_level="non-technical",
    focus=[
        "Business outcome",
        "User value",
        "Scope",
        "Risks",
        "Dependencies"
    ],
    exclude=[
        "Technoical jargon",
        "Implementation details"
    ],
    output_format="Short paragraphs and bullet points",
    tone="Clear and business-oriented"
)

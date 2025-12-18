from openai import OpenAI

client = OpenAI()  # liest OPENAI_API_KEY aus der Umgebung

resp = client.responses.create(
    model="gpt-4.1-mini",
    input="Sag 'Hallo Sven' und dann eine kurze Idee für ein AI-Jira Tool."
)

print(resp.output_text)

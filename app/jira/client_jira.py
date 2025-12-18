import os
import httpx
from dotenv import load_dotenv

load_dotenv()

JIRA_BASE_URL = os.environ["JIRA_BASE_URL"].rstrip("/")
JIRA_EMAIL = os.environ["JIRA_EMAIL"]
JIRA_API_TOKEN = os.environ["JIRA_API_TOKEN"]


def adf_doc(text: str) -> dict:
    # Jira ADF: doc -> paragraph -> text
    return {
        "type": "doc",
        "version": 1,
        "content": [
            {
                "type": "paragraph",
                "content": [{"type": "text", "text": text}]
            }
        ]
    }

def jira_client() -> httpx.Client:
    # Jira Cloud: Basic Auth mit E-Mail + API Token :contentReference[oaicite:4]{index=4}
    return httpx.Client(
        base_url=JIRA_BASE_URL,
        auth=(JIRA_EMAIL, JIRA_API_TOKEN),
        headers={"Accept": "application/json", "Content-Type": "application/json"},
        timeout=30.0,
    )


def get_issue(issue_key: str) -> dict:
    with jira_client() as c:
        r = c.get(f"/rest/api/3/issue/{issue_key}")  # v3 API :contentReference[oaicite:5]{index=5}
        r.raise_for_status()
        return r.json()


def search_issues(jql: str, max_results: int = 10) -> dict:
    with jira_client() as c:
        r = c.get("/rest/api/3/search", params={"jql": jql, "maxResults": max_results})
        r.raise_for_status()
        return r.json()


def add_comment(issue_key: str, comment_text: str) -> dict:
    with jira_client() as c:
        payload = {"body": adf_doc(comment_text)}
        r = c.post(f"/rest/api/3/issue/{issue_key}/comment", json=payload)
        if r.status_code >= 400:
            print("Status:", r.status_code)
            print("Response:", r.text)
        r.raise_for_status()
        return r.json()


def update_description(issue_key: str, new_description: str) -> None:
    with jira_client() as c:
        payload = {"fields": {"description": new_description}}
        r = c.put(f"/rest/api/3/issue/{issue_key}", json=payload)
        r.raise_for_status()

def update_summary(issue_key: str, new_summary: str) -> None:
    with jira_client() as c:
        payload = {"fields": {"summary": new_summary}}
        r = c.put(f"/rest/api/3/issue/{issue_key}", json=payload)
        if r.status_code >= 400:
            print("Status:", r.status_code)
            print("Response:", r.text)
        r.raise_for_status()

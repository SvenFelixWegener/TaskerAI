from app.jira.client_jira import get_issue, add_comment_to_issue, update_summary
from app.ai.client_openai import correct_writing_from_string

if __name__ == "__main__":
    # Issue Key for manipulation
    issue_key = "DEV-2"
    issue = get_issue(issue_key)
    initial_summary_content = issue["fields"]["summary"]

    print("Unkorrigiert: " + initial_summary_content)
    corrected_summary_content: str = correct_writing_from_string(initial_summary_content)

    print("Korrigiert: " + corrected_summary_content)

    add_comment_to_issue(issue_key, "Corrected summary, please check!")

    update_summary(issue_key, corrected_summary_content)

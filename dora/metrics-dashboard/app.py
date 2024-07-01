from flask import Flask, render_template
import requests
import os
from collections import defaultdict
from datetime import datetime, timedelta, timezone

app = Flask(__name__)


def get_builds(base_url, job_name):
    """
    Fetch builds information for a specific job using the Jenkins API with depth=1.
    """
    api_url = f"{base_url}/job/{job_name}/api/json?depth=1"
    response = requests.get(api_url)
    builds = response.json()["builds"]
    return builds


def generate_last_six_months():
    """
    Generate a list of the last six months as strings in YYYY-MM format.
    """
    current_date = datetime.now()
    months = [current_date - timedelta(days=30 * i) for i in range(6)]
    return [month.strftime("%Y-%m") for month in reversed(months)]


def aggregate_data_by_month(builds):
    """
    Organize build data by month and ensure all last six months are displayed.
    """
    last_six_months = generate_last_six_months()
    data = {
        month: {"total_builds": 0, "failed_builds": 0, "rate": 0.0}
        for month in last_six_months
    }

    for build in builds:
        timestamp = build.get("timestamp",0)
        if timestamp:
            date = datetime.fromtimestamp(timestamp / 1000.0, timezone.utc)
            month = date.strftime("%Y-%m")
            if month in data:
                data[month]["total_builds"] += 1
                if build["result"] == "FAILURE":
                    data[month]["failed_builds"] += 1

    # Calculate the change failure rate for each month
    for month in data:
        total = data[month]["total_builds"]
        failed = data[month]["failed_builds"]
        data[month]["rate"] = (failed / total * 100) if total > 0 else 0

    return [{"month": month, **data[month]} for month in last_six_months]


@app.route("/")
def dashboard():
    """
    Render dashboard.html
    """
    base_url = os.getenv("JENKINS_BASE_URL", "http://localhost:8080")
    job_name = os.getenv("JENKINS_JOB_NAME", "Hello World")

    builds = get_builds(base_url, job_name)
    month_data = aggregate_data_by_month(builds)

    return render_template("dashboard.html", month_data=month_data)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)

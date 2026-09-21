from django.shortcuts import render

# Create your views here.
from .models import EmailScan
from django.shortcuts import render
from openai import OpenAI
import json
import os
client = OpenAI(api_key=os.environ.get('OPENAI_API_KEY'))

def email_scanner(request):

    result = None

    if request.method == "POST":

        email_text = request.POST.get("email_content")

        prompt = f"""
Analyze the following email for phishing threats.

Email Content:
{email_text}

Return ONLY valid JSON in this format:

{{
    "risk":"Low/Medium/High",
    "report":"Detailed explanation",
    "recommendation":"Security advice"
}}
"""

        try:
            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {
                        "role": "system",
                        "content": "You are a cybersecurity expert specializing in phishing detection."
                    },
                    {
                        "role": "user",
                        "content": prompt
                    }
                ]
            )

            result = json.loads(
                response.choices[0].message.content
            )

            # SAVE RESULT TO DATABASE
            EmailScan.objects.create(
                email_content=email_text,
                risk=result.get("risk"),
                report=result.get("report"),
                recommendation=result.get("recommendation")
            )

        except Exception as e:
            result = {
                "risk": "Unknown",
                "report": str(e),
                "recommendation": "Unable to analyze email."
            }

    return render(
        request,
        "credential/credential.html",
        {
            "result": result
        }
    )


from .models import EmailScan

def view_reports(request):

    reports = EmailScan.objects.all().order_by('-scan_id')

    return render(
        request,
        "credential/view_security_reports.html",
        {
            "reports": reports
        }
    )

from .models import Credential
from django.shortcuts import render
from .models import Credential, EmailScan

def monitor(request):

    reports = EmailScan.objects.all().order_by('-scan_id')
    breaches = Credential.objects.all()

    total_reports = reports.count()
    total_breaches = breaches.count()

    safe_count = reports.filter(risk='Low').count()
    high_count = reports.filter(risk='High').count()

    return render(
        request,
        "credential/monitor.html",
        {
            "reports": reports,
            "breaches": breaches,
            "total_reports": total_reports,
            "total_breaches": total_breaches,
            "safe_count": safe_count,
            "high_count": high_count,
        }
    )
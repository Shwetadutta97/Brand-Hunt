import smtplib
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from datetime import datetime


def _build_html(brands):
    today = datetime.now().strftime("%B %d, %Y")

    if not brands:
        body = "<p style='color:#555;'>No new funding news found in the last 24 hours. Check back tomorrow!</p>"
    else:
        rows = ""
        for b in brands:
            rows += f"""
            <tr>
              <td style="padding:14px 10px; border-bottom:1px solid #eee; vertical-align:top;">
                <a href="{b['link']}" style="font-size:15px; font-weight:bold; color:#c0392b; text-decoration:none;">
                  {b['title']}
                </a><br>
                <span style="font-size:12px; color:#888;">
                  {b['source']} &nbsp;|&nbsp; {b['published']}
                </span><br>
                <span style="font-size:13px; color:#444; margin-top:4px; display:block;">
                  {b['summary']}
                </span>
              </td>
            </tr>"""
        body = f"<table width='100%' cellpadding='0' cellspacing='0'>{rows}</table>"

    return f"""
    <html><body style="margin:0;padding:0;background:#f4f4f4;font-family:Arial,sans-serif;">
      <table width="100%" cellpadding="0" cellspacing="0" bgcolor="#f4f4f4">
        <tr><td align="center" style="padding:30px 10px;">
          <table width="650" cellpadding="0" cellspacing="0" style="background:#fff;border-radius:10px;overflow:hidden;box-shadow:0 2px 8px rgba(0,0,0,.1);">

            <tr>
              <td style="background:#c0392b;padding:24px 28px;">
                <h1 style="margin:0;color:#fff;font-size:22px;">🚀 Brand Hunt — Daily Digest</h1>
                <p  style="margin:6px 0 0;color:#f5b7b1;font-size:14px;">{today} &nbsp;|&nbsp; {len(brands)} new funding stories</p>
              </td>
            </tr>

            <tr>
              <td style="padding:20px 28px;">
                <p style="color:#333;font-size:14px;margin-top:0;">
                  Hi Shweta 👋, here are today's newly funded brands spotted across
                  <strong>Inc42, YourStory, Entrackr, StartupTalky & SutraHR</strong>:
                </p>
                {body}
              </td>
            </tr>

            <tr>
              <td style="background:#fafafa;padding:14px 28px;border-top:1px solid #eee;">
                <p style="margin:0;font-size:11px;color:#aaa;">
                  Brand Hunt Digest &nbsp;·&nbsp; Auto-generated every morning &nbsp;·&nbsp;
                  Sources: Inc42 · YourStory · Entrackr · StartupTalky · SutraHR
                </p>
              </td>
            </tr>

          </table>
        </td></tr>
      </table>
    </body></html>
    """


def send_email(brands):
    sender   = os.environ["EMAIL_SENDER"]
    password = os.environ["EMAIL_PASSWORD"]
    receiver = os.environ.get("EMAIL_RECEIVER", sender)

    msg = MIMEMultipart("alternative")
    msg["Subject"] = f"🚀 Brand Hunt Digest — {datetime.now().strftime('%d %b %Y')} | {len(brands)} Funded Brands"
    msg["From"]    = f"Brand Hunt <{sender}>"
    msg["To"]      = receiver

    msg.attach(MIMEText(_build_html(brands), "html"))

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(sender, password)
        server.sendmail(sender, receiver, msg.as_string())

    print(f"[emailer] Email sent to {receiver} with {len(brands)} brands.")

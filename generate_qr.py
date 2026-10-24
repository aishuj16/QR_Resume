
import qrcode
website_url = "https://your-real-resume-site.example.com/"
img = qrcode.make(website_url)
img.save("resume.png")
print("QR code generated successfully!")
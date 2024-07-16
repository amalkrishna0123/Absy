from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.core.mail import send_mail
from .models import Contact
from .serializers import ContactSerializer

class ContactView(APIView):
    def post(self, request):
        serializer = ContactSerializer(data=request.data)
        if serializer.is_valid():
            contact = serializer.save()
            # Send email
            send_mail(
                subject=f"New Contact Form Submission from {contact.name}",
                message=f"Name: {contact.name}\nEmail: {contact.email}\nPhone: {contact.phone}\nSubject: {contact.subject}\nMessage: {contact.message}",
                from_email='amalkrishna2001ma@gmail.com',
                recipient_list=['amalkrishna1437@gmail.com'],
            )
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

from django.db import models


class File(models.Model):
    file = models.FileField(upload_to='files')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    processed = models.BooleanField(default=False)

    def to_dict(self):
        return {
            'id': self.id,
            'file_name': self.file.name,
            'uploaded_at': self.uploaded_at,
            'processed': self.processed,
        }

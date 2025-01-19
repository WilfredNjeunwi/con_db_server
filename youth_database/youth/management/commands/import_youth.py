import csv
from django.core.management.base import BaseCommand
from youth.models import Youth

class Command(BaseCommand):
    help = 'Import youths from a CSV file'

    def add_arguments(self, parser):
        parser.add_argument('file_path', type=str, help='The path to the CSV file')

    def handle(self, *args, **kwargs):
        file_path = kwargs['file_path']

        with open(file_path, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                # Clean up header keys by stripping spaces
                cleaned_row = {key.strip(): value.strip() for key, value in row.items()}

                name = cleaned_row.get('NAME', '')
                phone_number = cleaned_row.get('PHONE NUMBER', '')
                orphan_status = cleaned_row.get('ORPHANT', '').strip().lower() == 'yes'
                blood_group = cleaned_row.get('BLOOD GROUP', '') or None

                # Log the values to debug
                self.stdout.write(self.style.NOTICE(f'Name: "{name}", Phone Number: "{phone_number}", Orphan: "{orphan_status}"'))

                # Check if name or phone is missing
                if not name or not phone_number:
                    self.stdout.write(self.style.WARNING(f'Skipping youth due to missing name or phone: {cleaned_row}'))
                    continue  # Skip this record if essential fields are missing

                # Create a new Youth instance
                youth = Youth(
                    name=name,
                    phone_number=phone_number,
                    quarter=cleaned_row.get('QUARTER', ''),
                    birthday=cleaned_row.get('BIRTHDAY', ''),
                    field_of_study=cleaned_row.get('FIELD OF STUDY', ''),
                    profession=cleaned_row.get('PROFESSION', ''),
                    talent_1=cleaned_row.get('TALENT 1', ''),
                    talent_2=cleaned_row.get('TALENT 2', ''),
                    talent_3=cleaned_row.get('TALENT 3', ''),
                    gift_1=cleaned_row.get('GIFT 1', ''),
                    gift_2=cleaned_row.get('GIFT 2', ''),
                    gift_3=cleaned_row.get('GIFT 3', ''),
                    orphant=orphan_status,
                    blood_group=blood_group
                )
                youth.save()
                self.stdout.write(self.style.SUCCESS(f'Successfully added youth: {youth.name}'))
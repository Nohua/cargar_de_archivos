import _csv, io
from django.contrib import messages
from django.shortcuts import render
from tablib import Dataset
from .resource import PersonaResource
from .models import Persona


def personas_carga(request):

    prompt = {
       'Orden': 'El csv debe seguir el siguiente orden: RUT, nombre y telefono',
    }
    if request.method == 'GET':
        return render(request, "uploadfiles/personas_cargar.html", prompt)

    csv_file = request.FILES['file']

    if not csv_file.name.endswith('.csv'):
        messages.error(request, 'Solo se aceptan archivos .CSV')

    data_set = csv_file.read().decode('UTF-8')
    io_string = io.StringIO(data_set)
    next(io_string)
    for column in _csv.reader(io_string, delimiter=',', quotechar='|'):
        created = Persona.objects.create(
            nombre=column[0],
            paterno=column[1],
            materno=column[2]
        )
        print(column[0])
    context = {}

    return render(request, "uploadfiles/personas_cargar.html", context)


def carga_simple(request):

    if request.method == 'POST':
        person_resource = PersonaResource()
        dataset = Dataset()
        new_persona = request.FILES['file']

        imported_data = dataset.load(new_persona.read())
        result = person_resource.import_data(dataset, dry_run=True)

        if not result.has_errors():
            person_resource.import_data(dataset, dry_run=False)

    return render(request, 'uploadfiles/import.html')

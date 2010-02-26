# Create your views here.
import datetime
import json
from django.http import Http404, HttpResponse
from django.shortcuts import render_to_response

from packages.models import Os, Host, Package

def submit(request, checksum):
    if request.method != 'POST' and not request.POST.get('json'):
        return Http404

    raw_data = request.POST['json']

    data = json.loads(raw_data)
    meta = data['meta']

    os, created = Os.objects.get_or_create(
        name=meta['operatingsystem'],
        version=meta['lsbdistrelease'],
        code_name=meta['lsbdistcodename'],
        architecture=meta['architecture']
    )

    host, created = Host.objects.get_or_create(
        name=meta['fqdn'],
        os=os
    ) 
    host.seen=datetime.datetime.now()
    host.save()
    host.packages.clear()

    for name, version in data['packages'].items():
        package, created = Package.objects.get_or_create(
            name=name,
            version=version
        )
        host.packages.add(package)

    return HttpResponse('ok')



def host_differences(request, source_name, comparator_name):
    source = Host.objects.get(name=source_name)
    comparator = Host.objects.get(name=comparator_name)

    packages = Package.objects.filter(host=source).exclude(host=comparator)

    return render_to_response('packages.html', {'source':source,
                                                'comparator':comparator,
                                                'packages':packages})

def version_differences(request, source_name, comparator_name):
    source = Host.objects.get(name=source_name)
    comparator = Host.objects.get(name=comparator_name)

    source_packages = Package.objects.filter(host=source).exclude(host=comparator)
    compare_packages = Package.objects.filter(host=comparator).exclude(host=source)
    
    package_dict = {}
    for package in source_packages:
        package_dict[package.name] = [package.version]

    for package in compare_packages:
        package_dict.setdefault(package.name, ['']).append(package.version)

    packages = sorted(package_dict.items(), key=lambda p:p[0])

    return render_to_response('versions.html', {'source':source,
                                                'comparator':comparator,
                                                'packages':packages})

from setuptools import setup, find_packages

template_patterns = [
    'templates/*.html',
    'templates/*/*.html',
]

packages = find_packages('.')

setup(
    name='django-podcast',
    version='0.5.0',
    description='Django podcast app',
    packages=packages,
    package_data={
        package_name: template_patterns for package_name in packages
    },
    url='https://github.com/jefftriplett/django-podcast',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
    ],
)

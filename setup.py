
m setuptools import setup, find_packages

version = '1.0'

LONG_DESCRIPTION = """
Using django-files
===================

"""

setup(
    name='django-files',
    version=version,
    description="django-files",
    long_description=LONG_DESCRIPTION,
    classifiers=[
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Framework :: Django",
        "Environment :: Web Environment",
    ],
    keywords='files,django',
    author='',
    author_email='',
    url='https://github.com/GeoNodeChile/django-files',
    license='BSD',
    packages=find_packages(),
    package_data = {
        'files': [
            'templates/files/*.html',
            #'locale/*/LC_MESSAGES/*',
            #'media/avatar/img/default.jpg'
        ],
    },
    include_package_data=True,
    zip_safe=False,
)



from setuptools import setup
import os

def get_long_description():
    with open(
        os.path.join(os.path.dirname(os.path.abspath(__file__)), "README.md"),
        encoding="utf8",
    ) as fp:
        return fp.read()

setup(
    name="openrefine-demo",
    packages= ['openrefine_demo'],
    version='0.0.5',
    include_package_data=True,
    install_requires=[
        'jupyter-server-proxy',
        'notebook'
    ],
    #extras_require={'pyclient':['git+https://github.com/dbutlerdb/refine-client-py']},
    #extras_require={'pyclient':['openrefine-client']},
    url="https://github.com/Nithiya2223/openrefine_demo",
    author="Tony Hirst",
    description="Jupyter server proxy wrapper for Open Refine",
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    entry_points={
        'jupyter_serverproxy_servers': [
            'openrefine = openrefine_demo:setup_openrefine',
        ]
    },
    package_data={
        'openrefine_demo': ['icons/*'],
    },
)

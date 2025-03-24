from setuptools import setup, find_packages

setup(
    name="COALA",
    version="1.0",
    description="COlorectal CAncer Liver metastasis Assessment",
    author="Jacqueline Bereska",
    author_email="j.i.bereska@gmail.com",
    url="https://github.com/JackieBereska/COALA/",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "acvl_utils==0.2",
        "batchgenerators==0.25",
        "dynamic_network_architectures==0.2",
        "nibabel==5.1.0",
        "numpy==1.24.1",
        "openpyxl==3.1.2",
        "pandas==2.0.3",
        "pingouin==0.5.4",
        "scipy==1.11.1",
        "SimpleITK==2.2.1",
        "scikit-image==0.22.0",
        "torch==2.0.1+cu117",
        "tqdm==4.66.1"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)

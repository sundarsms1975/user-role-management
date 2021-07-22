import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="user-role-mgmt-pkg-deputy",
    version="0.0.1",
    author="Sundar SM",
    author_email="sundarsms2001@outlook.com",
    description="User Role Management Utility",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/sundarsms1975/user-role-management",
    project_urls={
        "Bug Tracker": "https://github.com/sundarsms1975/user-role-management/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "user_role_mgmt"},
    packages=setuptools.find_packages(where="user_role_mgmt"),
    python_requires=">=3.6",
)

FROM python
WORKDIR /resrs_project/
COPY requirements.txt .
RUN pip install -r requirements.txt
ENV ENV=dev
CMD python -m pytest -s --alluredir=tests_results/ /tests_project/tests/

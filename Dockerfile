FROM python:3.10

RUN mkdir -p /selenium_examples/

WORKDIR /selenium_examples/

COPY . /selenium_examples/

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "test_practice_form_page.py"]
FROM python
ENV PORT 80
EXPOSE 80
WORKDIR /usr/src/app

COPY . .
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install jupyter
RUN pip install nbconvert
# Running the nbconvert script
RUN jupyter nbconvert --to script SampleModelGeneratorScriptCopy.ipynb
RUN python SampleModelGeneratorScriptCopy.py
RUN python modelUpload.py

ENTRYPOINT ["python"]
CMD ["app.py"]
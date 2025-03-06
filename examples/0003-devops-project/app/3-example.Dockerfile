FROM gcr.io/distroless/python3-debian11

COPY main.py .

# -u flag see print statements in container
ENTRYPOINT ["python3", "-u", "main.py"]

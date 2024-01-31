FROM nvidia/cuda:12.3.1-runtime-ubuntu20.04
WORKDIR /app
RUN apt update && \
    apt install --no-install-recommends -y build-essential python3 python3-pip && \
    apt clean && rm -rf /var/lib/apt/lists/*
RUN apt-get update && apt-get install -y gcc python3-dev
RUN apt-get clean && rm -rf /var/lib/apt/lists/*
RUN apt update
COPY . .
RUN pip install --no-cache-dir --upgrade -r requirements.txt
RUN python3 model_initializer.py
EXPOSE 5000
CMD [ "flask", "run", "--host=::"]
